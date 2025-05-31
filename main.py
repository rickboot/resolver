from backend.scraper.web_scraper import scrape_website
from backend.llm.factory import get_llm_client

import sys

def main():
    # todo: remove hard-coded url after dev
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://razer.com'

    llm_client = get_llm_client()
    scrape_result = scrape_website(url, llm_client)

    if "error" in scrape_result:
        print("Scrape failed: {scrape_result['error']}")
        return

    print("\n\n=======Scraped data=======\n\n")
    for key, value in scrape_result.items():
        print(f"{key}:\n{value}\n\n")
    print("==========================\n\n")

if __name__ == "__main__":
    main()
