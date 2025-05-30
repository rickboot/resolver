from playwright.sync_api import sync_playwright

def scrape_website(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, timeout=30000, wait_until="domcontentloaded")

            # get page metadata
            title = page.title()
            desc_locator = page.locator('meta[name="description"]')
            description = desc_locator.get_attribute('content') if desc_locator.count() > 0 else None

            og_title_locator = page.locator('meta[property="og:title"]')
            og_title = og_title_locator.get_attribute('content') if og_title_locator.count() > 0 else None

            og_desc_locator = page.locator('meta[property="og:description"]')
            og_description = og_desc_locator.get_attribute('content') if og_desc_locator.count() > 0 else None

            # get image urls
            image_urls = page.eval_on_selector_all('img', 'els => els.map(el => el.src)')

            return {
                "title": title,
                "description": description,
                "og_title": og_title,
                "og_description": og_description,
                "image_urls": image_urls
            }
            
        except Exception as e:
            print(f"[Scraper Error] {e}")
            return {"error": str(e)}

        finally:
            browser.close()