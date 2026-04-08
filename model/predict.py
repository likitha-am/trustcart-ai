import numpy as np
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.preprocess import clean_text

# Load model
model = load_model("model/review_model.h5")

# IMPORTANT: we must use SAME vectorizer
# (for now we re-fit, later we'll save it properly)

vectorizer = TfidfVectorizer(max_features=5000)

# Temporary training data (to fit vectorizer)
sample_data = [
    "this product is amazing",
    "worst item ever",
    "very good quality",
    "completely fake product"
]

vectorizer.fit(sample_data)

def predict_review(review):
    review = clean_text(review)
    vector = vectorizer.transform([review]).toarray()

    prediction = model.predict(vector)[0][0]

    if prediction > 0.5:
        return "Genuine Review ✅"
    else:
        return "Fake Review ⚠️"