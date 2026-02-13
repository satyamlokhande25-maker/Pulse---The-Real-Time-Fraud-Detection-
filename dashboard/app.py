import streamlit as st
import requests

st.set_page_config(page_title="Pulse Market Sentiment", layout="centered")

st.title("📊 Pulse – Market Sentiment Dashboard")

API_URL = "http://127.0.0.1:8000/reddit"

subreddit = st.text_input("Enter Subreddit", value="bitcoin")
limit = st.slider("Number of posts", 1, 20, 5)

if st.button("Analyze Sentiment"):
    response = requests.get(f"{API_URL}/{subreddit}", params={"limit": limit})

    if response.status_code == 200:
        data = response.json()
        results = data["results"]

        pos = sum(1 for r in results if r["sentiment"] == "positive")
        neg = sum(1 for r in results if r["sentiment"] == "negative")
        neu = sum(1 for r in results if r["sentiment"] == "neutral")

        st.subheader("Overall Sentiment")
        st.write(f"Positive: {pos}")
        st.write(f"Negative: {neg}")
        st.write(f"Neutral: {neu}")

        st.subheader("Post Analysis")
        for r in results:
            st.markdown(f"**{r['title']}**")
            st.write(f"Sentiment: {r['sentiment']} | Score: {r['score']}")
            st.divider()
    else:
        st.error("API error")
