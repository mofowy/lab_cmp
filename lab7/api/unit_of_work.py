from .repository import PostRepository
from .client import APIClient

class UnitOfWork:
    def __init__(self):
        self.client = APIClient()
        self.repository = PostRepository(self.client)

    def fetch_and_commit(self):
        return self.repository.get_all_posts()