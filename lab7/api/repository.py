from .client import APIClient

class PostRepository:
    def __init__(self, client):
        self.client = client

    def get_all_posts(self):
        return self.client.fetch_posts()