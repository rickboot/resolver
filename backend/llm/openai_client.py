import os
import openai
from dotenv import load_dotenv
from backend.llm.base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self, model: str = "gpt-4o-mini"):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
    
    def generate(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

