from fastapi import FastAPI
from pydantic import BaseModel
from backend.scraper.web_scraper import scrape_website
from backend.llm.factory import get_llm_client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_client = get_llm_client()

class ScrapeRequest(BaseModel):
    url: str

@app.post("/analyze")
def analyze(request: ScrapeRequest):
    scraped = scrape_website(request.url, llm_client)

    return {
        "url": request.url,
        "company_name": scraped["company_name"],
        "target_audience": scraped["target_audience"],
        "writing_style": scraped["writing_style"]
    }