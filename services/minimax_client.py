from typing import Any

import requests

from config import settings


class MiniMaxClient:
    def __init__(
        self,
        token: str,
        model: str = settings.minimax_default_model,
        url: str = settings.minimax_uri,
    ):
        self.name: str = "MiniMax"
        self.token: str = token
        self.model: str = model
        self.url: str = url

    def generate_response(self, prompt: str) -> Any:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(self.url, json=payload, headers=headers)

        return response.json()
