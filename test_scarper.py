from scraper.scraper import get_reviews

url = "https://www.amazon.in/HiPer-Microfoliant-Resurfacing-Skin-Sphingolipids/dp/B0DP9ZM7BJ"  # any product

reviews = get_reviews(url)

print("Reviews:", reviews)