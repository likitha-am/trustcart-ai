def analyze_reviews(reviews):
    positive_words = ["good", "great", "excellent", "amazing"]
    negative_words = ["bad", "worst", "poor", "fake"]

    score = 0

    for review in reviews:
        review = review.lower()
        for word in positive_words:
            if word in review:
                score += 1
        for word in negative_words:
            if word in review:
                score -= 1

    # Normalize score
    trust_score = max(0, min(100, (score + len(reviews)) * 50 // len(reviews)))

    return trust_score