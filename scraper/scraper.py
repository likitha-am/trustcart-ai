import requests
from bs4 import BeautifulSoup

def get_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    reviews = []

    # Amazon review class (may change!)
    review_blocks = soup.find_all("span", {"data-hook": "review-body"})

    for review in review_blocks:
        text = review.get_text(strip=True)
        reviews.append(text)

    return reviews[:10]  # limit for now