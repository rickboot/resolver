import os
from openai import OpenAI
from dotenv import load_dotenv
from backend.llm.base import LLMClient

class DeepSeekClient(LLMClient):
    def __init__(self, model: str = "deepseek-chat"):
        load_dotenv()
        self.model = model
        self.client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
    
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()

