import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv

load_dotenv()


class MiniMaxClient:
    def __init__(
        self,
        token: str,
        model: Optional[str] = os.getenv("MINIMAX_DEFAULT_MODEL"),
        url: Optional[str] = os.getenv("MINIMAX_URI"),
    ):
        self.name: str = "MiniMax"
        self.token: str = token
        self.model: Optional[str] = model
        self.url: Optional[str] = url

    def generate_response(self, prompt: str) -> Any:
        if not self.url:
            raise ValueError("MINIMAX_URI environment variable is not set")
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(self.url, json=payload, headers=headers)

        return response.json()
