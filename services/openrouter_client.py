import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv

load_dotenv()


class OpenRouterClient:
    def __init__(
        self,
        token: str,
        model: Optional[str] = os.getenv("OPENROUTER_DEFAULT_MODEL"),
        url: Optional[str] = os.getenv("OPENROUTER_URI"),
    ):
        self.name: str = "OpenRouter"
        self.token: str = token
        self.model: Optional[str] = model
        self.url: Optional[str] = url

    def generate_file_response(self, prompt: str, file: str) -> Any:
        if not self.url:
            raise ValueError("OPENROUTER_URI environment variable is not set")
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
