import os
from dotenv import load_dotenv
from backend.llm.base import LLMClient
from backend.llm.openai_client import OpenAIClient
from backend.llm.deepseek_client import DeepSeekClient

load_dotenv()

def get_llm_client() -> LLMClient:
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openai":
        return OpenAIClient()
    elif provider == "deepseek":
        return DeepSeekClient()
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
    
