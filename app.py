import streamlit as st
from model.predict import analyze_multiple_reviews

st.title("🛒 TrustCart AI")

st.write("Enter multiple reviews (one per line)")

reviews_input = st.text_area("Reviews")

if st.button("Analyze"):
    reviews = reviews_input.split("\n")

    if len(reviews) == 0 or reviews[0].strip() == "":
        st.warning("Please enter reviews")
    else:
        score = analyze_multiple_reviews(reviews)

        st.info(f"Overall Trust Score: {score}%")

        if score > 80:
            st.success("🟢 Safe to Buy")
        elif score > 60:
            st.warning("🟡 Buy with Caution")
        else:
            st.error("🔴 Not Recommended")