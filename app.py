from scraper.scraper import get_reviews

url = "https://www.amazon.in/HiPer-Microfoliant-Resurfacing-Skin-Sphingolipids/dp/B0DP9ZM7BJ"

reviews = get_reviews(url)

for r in reviews:
    print(r)