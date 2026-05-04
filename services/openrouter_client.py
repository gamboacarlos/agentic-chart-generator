import os

import requests
from dotenv import load_dotenv

load_dotenv()


class OpenRouterClient:
    def __init__(
        self,
        token: str,
        model=os.getenv("OPENROUTER_DEFAULT_MODEL"),
        url=os.getenv("OPENROUTER_URI"),
    ):
        self.name: str = "OpenRouter"
        self.token: str = token
        self.model: str = model
        self.url: str = url

    def generate_file_response(self, prompt: str, file) -> requests.Response:
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
