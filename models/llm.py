from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

def get_llm():
    return client


def generate_response(prompt: str) -> str:
    response = client.text_generation(
        model="google/flan-t5-base",
        prompt=prompt,
        max_new_tokens=256,
        temperature=0.2
    )
    return response