import numpy as np
import pickle
from tensorflow.keras.models import load_model
from utils.preprocess import clean_text

# 🔥 Load model
model = load_model("model/review_model.h5")

# 🔥 Load vectorizer (PUT IT HERE)
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def predict_review(review):
    review = clean_text(review)
    vector = vectorizer.transform([review]).toarray()

    prediction = model.predict(vector)[0][0]

    if prediction > 0.5:
        return "Genuine Review ✅", round(prediction * 100, 2)
    else:
        return "Fake Review ⚠️", round((1 - prediction) * 100, 2)
def analyze_multiple_reviews(reviews):
    scores = []

    for review in reviews:
        review = clean_text(review)
        vector = vectorizer.transform([review]).toarray()
        prediction = model.predict(vector)[0][0]
        scores.append(prediction)

    avg_score = sum(scores) / len(scores)

    return round(avg_score * 100, 2)    