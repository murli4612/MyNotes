import uuid
from typing import List, Dict
from talent_pool.services.thrive import ThrivePlatform
from talent_pool.models.enums import ProjectCategory

class CLI:
    def __init__(self):
        self.platform = ThrivePlatform()
        self.command_handlers = {
            'register_lead': self._register_lead,
            'register_developer': self._register_developer,
            'register_project': self._register_project,
            'get_available_projects': self._get_available_projects,
            'request_project': self._request_project,
            'accept_request': self._accept_request,
            'get_developer_details': self._get_developer_details,
            'get_project_details': self._get_project_details,
            'cancel_project': self._cancel_project,
            'complete_project': self._complete_project,
        }

    def _register_lead(self, name: str) -> str:
        return self.platform.register_lead(name)

    def _register_developer(self, name: str) -> str:
        return self.platform.register_developer(name)

    def _register_project(self, lead_name: str, project_name: str, skills_str: str) -> str:
        skills = [s.strip().strip('"') for s in skills_str.strip('[]').split(',')]
        category = ProjectCategory(skills[0].upper())
        return self.platform.register_project(lead_name, project_name, category)

    def _get_available_projects(self) -> str:
        projects = self.platform.get_available_projects()
        return "\n".join(
            f"{p['id']}, {p['name']}, [{p['category']}], {p['lead']}"
            for p in projects
        )

    def _request_project(self, dev_name: str, project_id: str) -> str:
        return self.platform.request_project(dev_name, project_id)

    def _accept_request(self, request_id: str, project_id: str, lead_name: str) -> str:
        return self.platform.accept_request(lead_name, request_id)

    def _get_developer_details(self, dev_name: str) -> str:
        details = self.platform.get_developer_details(dev_name)
        if details['current_project']:
            return f"{dev_name} is working on {details['current_project']['name']}"
        return f"{dev_name} has no project assigned"

    def _get_project_details(self, project_id: str) -> str:
        details = self.platform.get_project_details(project_id)
        assigned_dev = details['assigned_developer']['name'] if details['assigned_developer'] else "UnAssigned"
        return (
            f"{project_id}, {details['name']}, [{details['category']}], "
            f"{details['lead']}, {assigned_dev}"
        )

    def _cancel_project(self, lead_name: str, project_id: str) -> str:
        return self.platform.cancel_project(lead_name, project_id)

    def _complete_project(self, dev_name: str, project_id: str) -> str:
        return self.platform.complete_project(dev_name, project_id)

    def process_command(self, command_str: str) -> str:
        try:
            parts = command_str.split('->')
            command = parts[0].strip()
            args = [arg.strip() for arg in parts[1].split(',')] if len(parts) > 1 else []
            
            if command in self.command_handlers:
                return self.command_handlers[command](*args)
            return "Unknown command"
        except Exception as e:
            return f"Error: {str(e)}"