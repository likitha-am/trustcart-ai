import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

def load_and_preprocess(path):
    df = pd.read_csv(path)

    print("Columns:", df.columns)

    # Select columns
    df = df[['text_', 'label']]
    df.columns = ['review', 'label']

    # Convert labels
    df['label'] = df['label'].map({'CG': 0, 'OR': 1})

    # Clean text
    df['review'] = df['review'].apply(clean_text)

    return df