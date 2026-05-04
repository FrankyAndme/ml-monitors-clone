import requests
from bs4 import BeautifulSoup
import json

def scrape_ml_monitors():
    url = "https://listado.mercadolibre.com.ar/monitor-led"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Fetching {url}...")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    # Find product cards
    items = soup.find_all("li", class_="ui-search-layout__item")
    
    for item in items[:10]:
        try:
            title_el = item.find("h2", class_="ui-search-item__title")
            title = title_el.text.strip() if title_el else "N/A"

            price_el = item.find("span", class_="andes-money-amount__fraction")
            price = price_el.text.strip() if price_el else "N/A"

            link_el = item.find("a", class_="ui-search-link")
            link = link_el["href"] if link_el else "N/A"

            img_el = item.find("img", class_="ui-search-item__thumbnail")
            img = img_el["src"] if img_el else "N/A"

            products.append({
                "title": title,
                "price": price,
                "link": link,
                "image": img
            })
        except Exception as e:
            print(f"Error scraping item: {e}")

    return products

def main():
    try:
        data = scrape_ml_monitors()
        with open("ml-monitors-clone/products.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Successfully scraped {len(data)} products and saved to products.json")
    except Exception as e:
        print(f"Global error: {e}")

if __name__ == "__main__":
    main()
