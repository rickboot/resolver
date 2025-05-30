from backend.scraper.web_scraper import scrape_website

def main():
    url = input("Enter a website URL: ").strip()

    result = scrape_website(url)

    if "error" in result:
        print("Scrape failed: {result['error']}")
    else:
        print("Scraped data:")
        for key, value in result.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
