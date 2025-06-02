from playwright.sync_api import sync_playwright
from backend.llm.llm_analyzer import analyze_target_audience, analyze_writing_style
from backend.llm.base import LLMClient

def scrape_website(url: str, llm_client: LLMClient) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url, timeout=30000, wait_until="domcontentloaded")

            # get page metadata - title, company name, description
            title = page.title()
            company_name_locater = page.locator('meta[property="og:site_name"]')
            company_name = company_name_locater.get_attribute('content') if company_name_locater.count() > 0 else None

            desc_locator = page.locator('meta[name="description"]')
            description = desc_locator.get_attribute('content') if desc_locator.count() > 0 else None

            # og title and description
            og_title_locator = page.locator('meta[property="og:title"]')
            og_title = og_title_locator.get_attribute('content') if og_title_locator.count() > 0 else None

            og_desc_locator = page.locator('meta[property="og:description"]')
            og_description = og_desc_locator.get_attribute('content') if og_desc_locator.count() > 0 else None

            # get image urls
            image_urls = page.eval_on_selector_all('img', 'els => els.map(el => el.src)')

            # logo urls
            # TODO: improve svg extraction - ex: https://nvidia.com
            logo_urls = page.eval_on_selector_all(
                'img[alt*="logo"], img[src*="logo"], img[class*="logo"], span[class*="logo"] svg',
                '''
                els => els.map(el => {
                    let url = el.getAttribute('src') || el.getAttribute('href');
                    if (!url) {
                        const svg = new XMLSerializer().serializeToString(el);
                        url = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
                    }
                    return url;
                })
                '''
            )

            # brand colors = colors used in the website buttons, headers, and links
            # TODO: improve brand colors extraction - perhaps use of color by element type? frequency?
            brand_colors = page.eval_on_selector_all(
                'button, h1, h2, a',
                '''
                (elements) => {
                function colorToHex(color) {
                    if (color.startsWith('#')) return color;
                    color = color.replace(/\\s/g, '').toLowerCase();
                    if (color.startsWith('rgb')) {
                    const rgbValues = color.match(/\\d+/g).slice(0, 3);
                    const hexValues = rgbValues.map((value) => {
                        const hex = parseInt(value).toString(16);
                        return hex.length === 1 ? '0' + hex : hex;
                    });
                    return '#' + hexValues.join('');
                    }
                    return null;
                }

                const colors = [];
                elements.forEach((el) => {
                    const styles = window.getComputedStyle(el);
                    const bgColor = colorToHex(styles.backgroundColor);
                    const fontColor = colorToHex(styles.color);
                    if (bgColor && !colors.includes(bgColor)) colors.push(bgColor);
                    if (fontColor && !colors.includes(fontColor)) colors.push(fontColor);
                });
                return colors;
                }
                '''
            )

            # fonts
            # TODO: improve font extraction = see razer.com and allbirds.com
            fonts = page.eval_on_selector_all(
                'link[type="font/woff2"], link[type="font/woff"], link[type="font/otf"], link[type="font/ttf"], style[href*="font"]',
                'els => Array.from(new Set(els.map(el => el.href)))'
            )

            # social media links
            social_media_links = page.eval_on_selector_all(
                'a[href*="facebook"], a[href*="twitter"], a[href*="instagram"], a[href*="linkedin"], a[href*="youtube"]',
                '''
                els => Array.from(new Set(
                    els
                    .map(link => link.getAttribute('href'))
                    .filter(url => url !== null)
                ))
                '''
            )
            
            # userland text
            page_text = page.eval_on_selector_all(
                'p, h1, h2, h3, h4, h5, h6',
                'els => els.map(el => el.textContent.trim()).join("\\n")'
            )

            return {
                "company_name": locals().get("company_name", ""),
                "website_url": url,
                "title": locals().get("title", ""),
                "description": locals().get("description", ""),
                "og_title": locals().get("og_title", ""),
                "og_description": locals().get("og_description", ""),
                "page_text": locals().get("page_text", ""),
                "brand_colors": locals().get("brand_colors", []),
                "image_urls": locals().get("image_urls", []),
                "logo_urls": locals().get("logo_urls", []),
                "social_media_links": locals().get("social_media_links", []),
                "fonts": locals().get("fonts", []),  
            }

        except Exception as e:
            print(f"[Scraper Error] {e}")
            return {"error": str(e)}

        finally:
            browser.close()
