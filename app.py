from utils.preprocess import load_and_preprocess

df = load_and_preprocess("data/fake_reviews.csv")

print(df.head())