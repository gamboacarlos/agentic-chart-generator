import os

from dotenv import load_dotenv

from prompts.create_chart_prompt import create_chart_prompt
from services.minimax_client import MiniMaxClient

load_dotenv()

minimax_token = os.getenv("MINIMAX_API_KEY")
client = MiniMaxClient(minimax_token)


def generate_chart_code(out_path: str) -> str:
    instructions = "Create a plot comparing Q1 coffee sales in 2024 and 2025 using the data in coffeeshop_sales.csv."
    prompt = create_chart_prompt(out_path, instructions)
    response = client.generate_response(prompt)

    return response["choices"][0]["message"]["content"]
