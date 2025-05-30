from backend.scraper.web_scraper import scrape_website
from backend.llm.openai_analyzer import analyze_text
import sys

def main():
    # todo: remove hard-coded url after dev
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://razer.com'

    scrape_result = scrape_website(url)

    if "error" in scrape_result:
        print("Scrape failed: {scrape_result['error']}")
        return

    # print("Scraped data:")
    # for key, value in scrape_result.items():
    #     print(f"{key}: {value}")


    analyze_result = analyze_text(scrape_result['text_content'])
    print("Analyzed data:")
    print(analyze_result)

if __name__ == "__main__":
    main()
