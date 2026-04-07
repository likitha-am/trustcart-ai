from utils.review_analyzer import analyze_reviews

reviews = [
    "This product is amazing!",
    "Very good quality",
    "Worst purchase ever",
    "Looks fake to me"
]

score = analyze_reviews(reviews)

print("Review Trust Score:", score)