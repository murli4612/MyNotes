import uuid
import queue

from talent_pool.models.enums import DeveloperStatus

class User:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name

class Lead(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.projects = []
        self.notifications = queue.Queue()

class Developer(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.status = DeveloperStatus.AVAILABLE
        self.current_project = None
        self.completed_projects = []
        self.skills = set()
        self.rating = 0.0
        self.ratings = []
        self.notifications = queue.Queue()

    def add_skill(self, skill):
        self.skills.add(skill)

    def update_rating(self, rating: int):
        self.ratings.append(rating)
        self.rating = sum(self.ratings) / len(self.ratings)