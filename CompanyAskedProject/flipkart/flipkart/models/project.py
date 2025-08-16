import threading
from datetime import datetime, timedelta
import uuid

from talent_pool.models.enums import ProjectStatus

class Project:
    def __init__(self, name: str, lead, category, expiry_minutes=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.lead = lead
        self.category = category
        self.status = ProjectStatus.OPEN
        self.creation_time = datetime.now()
        self.expiry_time = self.creation_time + timedelta(minutes=5)
        self.expiry_minutes = expiry_minutes
        self.requests = []
        self.assigned_developer = None
        self.lock = threading.Lock()

    def is_expired(self):
        return datetime.now() > self.expiry_time
    
  
