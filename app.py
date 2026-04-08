import streamlit as st
from model.predict import predict_review

st.title("🛒 TrustCart AI - Review Analyzer")

review = st.text_area("Enter Product Review")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        result = predict_review(review)
        st.success(f"Result: {result}")