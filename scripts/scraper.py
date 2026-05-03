import asyncio
import json
from playwright.async_api import async_playwright

async def scrape_ml_monitors():
    url = "https://listado.mercadolibre.com.ar/monitor-led"
    products = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="networkidle")

        # Wait for the product cards to load
        await page.wait_for_selector(".ui-search-result__wrapper")

        # Extract the first 10 products
        items = await page.query_selector_all(".ui-search-result__wrapper")
        
        for item in items[:10]:
            try:
                title_el = await item.query_selector(".ui-search-item__title")
                title = await title_el.inner_text() if title_el else "N/A"

                price_el = await item.query_selector(".andes-money-amount__fraction")
                price = await price_el.inner_text() if price_el else "N/A"

                link_el = await item.query_selector(".ui-search-link")
                link = await link_el.get_attribute("href") if link_el else "N/A"

                img_el = await item.query_selector(".ui-search-result__thumb")
                img = await img_el.get_attribute("src") if img_el else "N/A"

                products.append({
                    "title": title,
                    "price": price,
                    "link": link,
                    "image": img
                })
            except Exception as e:
                print(f"Error scraping item: {e}")

        await browser.close()

    return products

async def main():
    try:
        data = await scrape_ml_monitors()
        with open("ml-monitors-clone/products.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Successfully scraped {len(data)} products and saved to products.json")
    except Exception as e:
        print(f"Global error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
