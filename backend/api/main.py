from fastapi import FastAPI
from pydantic import BaseModel
from backend.scraper.web_scraper import scrape_website
from backend.llm.factory import get_llm_client
from backend.llm.llm_analyzer import generate_brand_summary
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()

#  todo: limit this to client in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)},
    )

llm_client = get_llm_client()

class ScrapeRequest(BaseModel):
    url: str

@app.post("/analyze")
def analyze(request: ScrapeRequest):
    scraped = scrape_website(request.url, llm_client)
    brand_summary = generate_brand_summary(scraped, llm_client)
    return brand_summary
