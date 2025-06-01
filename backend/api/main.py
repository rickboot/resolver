from fastapi import FastAPI
from pydantic import BaseModel
from backend.scraper.web_scraper import scrape_website
from backend.llm.factory import get_llm_client
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()

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

    return {
        "url": request.url,
        "company_name": scraped.get("company_name"),
        "title": scraped.get("title"),
        "description": scraped.get("description"),
        "og_title": scraped.get("og_title"),
        "og_description": scraped.get("og_description"),
        "target_audience": scraped.get("target_audience"),
        "writing_style": scraped.get("writing_style"),
        "website_url": scraped.get("website_url"),
        "brand_colors": scraped.get("brand_colors"),
        "social_media_links": scraped.get("social_media_links"),
        "image_urls": scraped.get("image_urls"),
        "logo_urls": scraped.get("logo_urls"),
        "fonts": scraped.get("fonts")
    }