import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def call_llm(prompt: str) -> str:
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def analyze_writing_style(text: str) -> str:
    prompt = f"""
    Analyze the writing style of the following text. Describe elements such as tone, voice, syntax, diction, and any notable literary devices or techniques used. Provide an overview of how these elements contribute to the overall impact and effectiveness of the paragraph in 30 words or less.
    {text}
    """
    return call_llm(prompt)

    
def analyze_target_audience(text: str) -> str:
    prompt = f"""
    Analyze the following text and identify the target audience of the company in 30 words or less. Consider factors like demographics (age, income, location), interests, and needs.:\n\n
    {text}
    """
    return call_llm(prompt)
