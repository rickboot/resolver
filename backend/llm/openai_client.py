from openai import OpenAI
from dotenv import load_dotenv
from backend.llm.base import LLMClient
import os

class OpenAIClient(LLMClient):
    def __init__(self, model: str = "gpt-4o-mini"):
        load_dotenv()
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()

