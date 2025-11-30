import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

class LLMClient:
    """
    Wrapper around the OpenAI chat client.
    Uses OPENAI_API_KEY from .env or environment variables.
    """
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        # If OPENAI_API_KEY is set in env, OpenAI() will pick it up automatically
        self.client = OpenAI()

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content
