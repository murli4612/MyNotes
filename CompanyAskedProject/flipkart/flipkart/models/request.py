from datetime import datetime
import uuid

class Request:
    def __init__(self, project, developer):
        self.id = str(uuid.uuid4())
        self.project = project
        self.developer = developer
        self.status = "Pending"
        self.timestamp = datetime.now()