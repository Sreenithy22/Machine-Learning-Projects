<<<<<<< HEAD
import streamlit as st
from transformers import pipeline

# Load pretrained sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

st.title("🛒 E-Commerce Review Analysis using LLM")

st.write("Enter a customer review and the model will analyze its sentiment.")

review = st.text_area("Enter Product Review")

if st.button("Analyze Review"):

    if review.strip() != "":
        result = sentiment_model(review)

        label = result[0]['label']
        score = result[0]['score']

        if label == "POSITIVE":
            st.success(f"😊 Positive Review (Confidence: {score:.2f})")
        else:
            st.error(f"😠 Negative Review (Confidence: {score:.2f})")

    else:
=======
import streamlit as st
from transformers import pipeline

# Load pretrained sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

st.title("🛒 E-Commerce Review Analysis using LLM")

st.write("Enter a customer review and the model will analyze its sentiment.")

review = st.text_area("Enter Product Review")

if st.button("Analyze Review") :

    if review.strip() != "":
        result = sentiment_model(review)

        label = result[0]['label']
        score = result[0]['score']

        if label == "POSITIVE":
            st.success(f"😊 Positive Review (Confidence: {score:.2f})")
        else:
            st.error(f"😠 Negative Review (Confidence: {score:.2f})")

    else:
>>>>>>> d86f6603683785944a36d5b2d16bc6dc012fb0b2
        st.warning("Please enter a review.")