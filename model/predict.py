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
    
    # Convert text → vector using SAME vectorizer
    vector = vectorizer.transform([review]).toarray()

    prediction = model.predict(vector)[0][0]

    if prediction > 0.5:
        return "Genuine Review ✅"
    else:
        return "Fake Review ⚠️"