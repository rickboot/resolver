from backend.scraper.web_scraper import scrape_website
from backend.llm.openai_analyzer import analyze_writing_style, analyze_target_audience
import sys

def main():
    # todo: remove hard-coded url after dev
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://razer.com'

    scrape_result = scrape_website(url)

    if "error" in scrape_result:
        print("Scrape failed: {scrape_result['error']}")
        return

    print("\n\n=======Scraped data=======\n\n")
    for key, value in scrape_result.items():
        print(f"{key}:\n{value}\n\n")
    print("==========================\n\n")

if __name__ == "__main__":
    main()
