from typing import Any

import requests

from config import settings


class OpenRouterClient:
    def __init__(
        self,
        token: str,
        model: str = settings.openrouter_default_model,
        url: str = settings.openrouter_uri,
    ):
        self.name: str = "OpenRouter"
        self.token: str = token
        self.model: str = model
        self.url: str = url

    def generate_file_response(self, prompt: str, file: str) -> Any:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [{"type": "text", "text": prompt}, file],
                },
            ],
        }

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(self.url, json=payload, headers=headers)

        return response.json()
