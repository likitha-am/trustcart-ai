# TrustCart AI

### E-Commerce Review Authenticity and Trust Analyzer

---

## Overview

TrustCart AI is a machine learning-based web application designed to analyze product reviews and determine whether they are genuine or potentially fake.

The project was built as an exploration into neural networks and natural language processing, with the goal of understanding how models learn from text data and make decisions in real-world scenarios.

In simple terms, it tries to answer a very practical question:
*“Can we trust these reviews, or are we being fooled?”*

---

## Features

* Detects fake vs genuine reviews
* Computes an overall trust score
* Supports multiple reviews as input
* Provides a final recommendation (Safe / Caution / Not Recommended)
* Interactive web interface using Streamlit

---

## How It Works

1. User inputs multiple product reviews
2. Text is cleaned and preprocessed
3. Reviews are converted into numerical form using TF-IDF
4. A neural network model predicts authenticity
5. Scores are aggregated into a final trust score
6. A recommendation is generated

---

## Project Structure

```
trustcart-ai/
│
├── data/              
├── model/             
│   ├── train_model.py
│   ├── predict.py
│   ├── review_model.h5
│   └── vectorizer.pkl
│
├── utils/             
│   └── preprocess.py
│
├── scraper/           
│   └── scraper.py
│
├── app.py             
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/your-username/trustcart-ai.git
cd trustcart-ai

pip install -r requirements.txt
```

---

## Run the Application

```bash
python -m streamlit run app.py
```

---

## Model Details

* Model Type: Feedforward Neural Network
* Vectorization: TF-IDF
* Optimizer: Adam
* Loss Function: Binary Crossentropy

---

## Example Output

```
Overall Trust Score: 78%

Buy with Caution
```

---

## Challenges Faced

* Handling noisy and inconsistent real-world text data
* Ensuring consistent preprocessing between training and prediction
* Understanding why models sometimes behave confidently but incorrectly
* Attempting web scraping and being politely rejected by Amazon

---

## Motivation

This project was built as part of a deeper attempt to understand neural networks beyond theory.

Instead of just learning how models work, the goal was to build something end-to-end — from data preprocessing to deployment — and observe how each component contributes to the final decision.

It reflects a growing interest in exploring how machine learning systems can be applied to practical, everyday problems.

---

## Future Improvements

* Direct product link analysis
* Better review authenticity detection using advanced models
* Visualization dashboard for insights
* Integration with modern NLP models for explanation generation

---

## Tech Stack

* Python
* TensorFlow / Keras
* scikit-learn
* Streamlit
* BeautifulSoup (experimental)


