import unittest
from lab7.api.client import APIClient # type: ignore

class TestAPIClient(unittest.TestCase):
    def test_fetch_posts(self):
        client = APIClient()
        posts = client.fetch_posts()
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)