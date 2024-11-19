import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def fetch_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()
        return response.json()