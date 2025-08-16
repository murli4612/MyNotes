import threading
import time
import uuid
import queue
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from collections import defaultdict
from ..models.user import Lead, Developer
from ..models.project import Project
from ..models.request import Request
from ..models.enums import ProjectStatus, DeveloperStatus, ProjectCategory

class ThrivePlatform:
    def __init__(self):
        self.leads: Dict[str, Lead] = {}
        self.developers: Dict[str, Developer] = {}
        self.projects: Dict[str, Project] = {}
        self.requests: Dict[str, Request] = {}
        self.lock = threading.Lock()
        self._start_expiry_checker()

    def _start_expiry_checker(self):
        def check_expired_projects():
            while True:
                time.sleep(10)
                with self.lock:
                    expired_projects = [
                        p for p in self.projects.values() 
                        if p.status in [ProjectStatus.OPEN, ProjectStatus.REQUESTED] and p.is_expired()
                    ]
                    for project in expired_projects:
                        self._cancel_project(project, "Project expired")

        thread = threading.Thread(target=check_expired_projects, daemon=True)
        thread.start()

    def register_lead(self, name: str) -> str:
        with self.lock:
            if name in [lead.name for lead in self.leads.values()]:
                raise ValueError(f"Lead {name} already registered")
            lead = Lead(name)
            self.leads[lead.id] = lead
            return f"{name} lead registered"

    def register_developer(self, name: str, skills: List[ProjectCategory] = None) -> str:
        with self.lock:
            if name in [dev.name for dev in self.developers.values()]:
                raise ValueError(f"Developer {name} already registered")
            dev = Developer(name)
            if skills:
                for skill in skills:
                    dev.add_skill(skill)
            self.developers[dev.id] = dev
            return f"{name} developer registered"

    def register_project(self, lead_name: str, project_name: str, category: ProjectCategory, expiry_minutes: int = None) -> str:
        with self.lock:
            lead = next((l for l in self.leads.values() if l.name == lead_name), None)
            if not lead:
                raise ValueError(f"Lead {lead_name} not found")
            
            project = Project(project_name, lead, category)
            lead.projects.append(project)
            self.projects[project.id] = project
            return f"{project_name} project with id {project.id} registered by {lead_name}"

    def get_available_projects(self) -> List[Dict]:
        with self.lock:
            return [
                {
                    "id": p.id,
                    "name": p.name,
                    "lead": p.lead.name,
                    "category": p.category.value,
                    "status": p.status.value
                }
                for p in self.projects.values()
                if p.status == ProjectStatus.OPEN and not p.is_expired()
            ]

    def request_project(self, dev_name: str, project_id: str) -> str:
        with self.lock:
            dev = next((d for d in self.developers.values() if d.name == dev_name), None)
            if not dev:
                raise ValueError(f"Developer {dev_name} not found")
            
            if dev.status == DeveloperStatus.WORKING:
                raise ValueError(f"Developer {dev_name} is already working on a project")
            
            project = self.projects.get(project_id)
            if not project:
                raise ValueError(f"Project {project_id} not found")
            
            if project.status != ProjectStatus.OPEN:
                raise ValueError(f"Project {project.name} is not available for requests")
            
            if project.is_expired():
                self._cancel_project(project, "Project expired")
                raise ValueError(f"Project {project.name} has expired")
            
            request = Request(project, dev)
            self.requests[request.id] = request
            project.requests.append(request)
            project.status = ProjectStatus.REQUESTED
            dev.status = DeveloperStatus.WORKING
            
            project.lead.notifications.put(f"New request from {dev_name} for project {project.name}")
            return f"Request with id {request.id} for {project_id} is registered for {dev_name}"

    def accept_request(self, lead_name: str, request_id: str) -> str:
        with self.lock:
            lead = next((l for l in self.leads.values() if l.name == lead_name), None)
            if not lead:
                raise ValueError(f"Lead {lead_name} not found")
            
            request = self.requests.get(request_id)
            if not request:
                raise ValueError(f"Request {request_id} not found")
            
            project = request.project
            if project.lead.id != lead.id:
                raise ValueError(f"Lead {lead_name} is not the owner of this project")
            
            if project.status != ProjectStatus.REQUESTED:
                raise ValueError(f"Project {project.name} is not in requestable state")
            
            dev = request.developer
            if dev.status != DeveloperStatus.WORKING or dev.current_project:
                raise ValueError(f"Developer {dev.name} is not available")
            
            project.assigned_developer = dev
            project.status = ProjectStatus.ASSIGNED
            dev.current_project = project
            request.status = "Approved"
            
            for req in project.requests:
                if req.id != request_id:
                    req.status = "Rejected"
                    req.developer.status = DeveloperStatus.AVAILABLE
                    req.developer.notifications.put(f"Your request for project {project.name} was rejected")
            
            dev.notifications.put(f"Your request for project {project.name} was approved!")
            return f"{dev.name} request is accepted to work on {project.name}"

    def _cancel_project(self, project: Project, reason: str):
        with project.lock:
            if project.status in [ProjectStatus.ASSIGNED, ProjectStatus.IN_PROGRESS, ProjectStatus.COMPLETED]:
                raise ValueError(f"Cannot cancel project in {project.status} state")
            
            project.status = ProjectStatus.CANCELLED
            
            for request in project.requests:
                if request.status == "Pending":
                    request.developer.status = DeveloperStatus.AVAILABLE
                    request.developer.notifications.put(f"Project {project.name} was cancelled: {reason}")
            
            project.lead.notifications.put(f"Project {project.name} was cancelled: {reason}")

    def cancel_project(self, lead_name: str, project_id: str) -> str:
        with self.lock:
            lead = next((l for l in self.leads.values() if l.name == lead_name), None)
            if not lead:
                raise ValueError(f"Lead {lead_name} not found")
            
            project = self.projects.get(project_id)
            if not project:
                raise ValueError(f"Project {project_id} not found")
            
            if project.lead.id != lead.id:
                raise ValueError(f"Lead {lead_name} is not the owner of this project")
            
            self._cancel_project(project, "Cancelled by lead")
            return f"{project.name} is cancelled"

    def start_project(self, dev_name: str, project_id: str) -> str:
        with self.lock:
            dev = next((d for d in self.developers.values() if d.name == dev_name), None)
            if not dev:
                raise ValueError(f"Developer {dev_name} not found")
            
            project = self.projects.get(project_id)
            if not project:
                raise ValueError(f"Project {project_id} not found")
            
            if project.assigned_developer.id != dev.id:
                raise ValueError(f"Developer {dev_name} is not assigned to this project")
            
            if project.status != ProjectStatus.ASSIGNED:
                raise ValueError(f"Project is not in assignable state")
            
            project.status = ProjectStatus.IN_PROGRESS
            dev.notifications.put(f"You have started working on project {project.name}")
            project.lead.notifications.put(f"Developer {dev_name} has started working on project {project.name}")
            return f"Project {project.name} marked as In Progress"

    def complete_project(self, dev_name: str, project_id: str, rating: Optional[int] = None) -> str:
        with self.lock:
            dev = next((d for d in self.developers.values() if d.name == dev_name), None)
            if not dev:
                raise ValueError(f"Developer {dev_name} not found")
            
            project = self.projects.get(project_id)
            if not project:
                raise ValueError(f"Project {project_id} not found")
            
            if project.assigned_developer.id != dev.id:
                raise ValueError(f"Developer {dev_name} is not assigned to this project")
            
            if project.status != ProjectStatus.IN_PROGRESS:
                raise ValueError(f"Project is not in progress")
            
            project.status = ProjectStatus.COMPLETED
            dev.status = DeveloperStatus.AVAILABLE
            dev.current_project = None
            dev.completed_projects.append(project)
            
            if rating is not None and 1 <= rating <= 5:
                dev.update_rating(rating)
                project.lead.notifications.put(f"You rated {dev_name} with {rating} stars for project {project.name}")
            
            dev.notifications.put(f"You have completed project {project.name}!")
            project.lead.notifications.put(f"Project {project.name} has been completed by {dev_name}")
            return f"{project.name} is marked completed"

    def get_developer_details(self, dev_name: str) -> Dict:
        with self.lock:
            dev = next((d for d in self.developers.values() if d.name == dev_name), None)
            if not dev:
                raise ValueError(f"Developer {dev_name} not found")
            
            return {
                "name": dev.name,
                "status": dev.status.value,
                "current_project": {
                    "id": dev.current_project.id,
                    "name": dev.current_project.name,
                    "status": dev.current_project.status.value
                } if dev.current_project else None,
                "skills": [skill.value for skill in dev.skills],
                "rating": dev.rating,
                "completed_projects": len(dev.completed_projects)
            }

    def get_project_details(self, project_id: str) -> Dict:
        with self.lock:
            project = self.projects.get(project_id)
            if not project:
                raise ValueError(f"Project {project_id} not found")
            
            return {
                "id": project.id,
                "name": project.name,
                "lead": project.lead.name,
                "category": project.category.value,
                "status": project.status.value,
                "assigned_developer": {
                    "id": project.assigned_developer.id,
                    "name": project.assigned_developer.name
                } if project.assigned_developer else None,
                "request_count": len(project.requests)
            }

    def get_developer_notifications(self, dev_name: str) -> List[str]:
        dev = next((d for d in self.developers.values() if d.name == dev_name), None)
        if not dev:
            raise ValueError(f"Developer {dev_name} not found")
        
        notifications = []
        while not dev.notifications.empty():
            notifications.append(dev.notifications.get())
        return notifications

    def get_lead_notifications(self, lead_name: str) -> List[str]:
        lead = next((l for l in self.leads.values() if l.name == lead_name), None)
        if not lead:
            raise ValueError(f"Lead {lead_name} not found")
        
        notifications = []
        while not lead.notifications.empty():
            notifications.append(lead.notifications.get())
        return notifications

    def get_top_developers(self, strategy: str = "completed_projects", limit: int = 5) -> List[Dict]:
        with self.lock:
            devs = list(self.developers.values())
            
            if strategy == "completed_projects":
                devs.sort(key=lambda d: len(d.completed_projects), reverse=True)
            elif strategy == "rating":
                devs.sort(key=lambda d: d.rating, reverse=True)
            else:
                raise ValueError(f"Unknown strategy: {strategy}")
            
            return [{
                "name": d.name,
                "completed_projects": len(d.completed_projects),
                "rating": d.rating,
                "skills": [s.value for s in d.skills]
            } for d in devs[:limit]]