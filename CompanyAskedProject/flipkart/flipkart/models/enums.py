from enum import Enum

class ProjectCategory(Enum):
    FRONTEND = "Frontend"
    BACKEND = "Backend"
    DEVOPS = "DevOps"
    MOBILE = "Mobile"
    DATA_SCIENCE = "Data Science"
    ML = "Machine Learning"

class ProjectStatus(Enum):
    OPEN = "Open"
    REQUESTED = "Requested"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class DeveloperStatus(Enum):
    AVAILABLE = "Available"
    WORKING = "Working"