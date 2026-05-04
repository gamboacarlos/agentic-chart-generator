import os

import requests
from dotenv import load_dotenv

load_dotenv()


class MiniMaxClient:
    def __init__(
        self,
        token: str,
        model=os.getenv("MINIMAX_DEFAULT_MODEL"),
        url=os.getenv("MINIMAX_URI"),
    ):
        self.name: str = "MiniMax"
        self.token: str = token
        self.model: str = model
        self.url: str = url

    def generate_response(self, prompt: str) -> requests.Response:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(self.url, json=payload, headers=headers)

        return response.json()
