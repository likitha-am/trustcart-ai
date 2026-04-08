import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from utils.preprocess import load_and_preprocess
import pickle

# Load data
df = load_and_preprocess("data/fake_reviews.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['review'], df['label'], test_size=0.2, random_state=42
)

# Convert text → numbers
vectorizer = TfidfVectorizer(max_features=5000)

X_train = vectorizer.fit_transform(X_train).toarray()
X_test = vectorizer.transform(X_test).toarray()

# Build Neural Network
model = Sequential([
    Dense(128, activation='relu', input_shape=(5000,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=5, batch_size=32)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print("Accuracy:", accuracy)

model.save("model/review_model.h5")    

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
