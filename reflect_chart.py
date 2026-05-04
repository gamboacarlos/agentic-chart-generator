from config import settings
from prompts.reflect_chart_prompt import reflect_chart_prompt
from services.openrouter_client import OpenRouterClient
from utils import encode_image_b64

client = OpenRouterClient(settings.openrouter_api_key)


def reflect_chart(chart_v1_path: str, out_path_v2: str, code_v1: str) -> str:
    print(chart_v1_path)
    print(out_path_v2)
    instructions = "Create a plot comparing Q1 coffee sales in 2024 and 2025 using the data in coffeeshop_sales.csv."
    base_64_file = encode_image_b64(chart_v1_path)
    prompt = reflect_chart_prompt(out_path_v2, instructions, code_v1)
    response = client.generate_file_response(prompt, base_64_file)

    return response["choices"][0]["message"]["content"]
