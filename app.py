import streamlit as st
import pandas as pd

st.title("Lingerie Feedback Analyzer (Insights Dashboard)")

reviews_input = st.text_area("Paste multiple reviews (one per line)")

positive_words = ["perfect", "comfortable", "soft", "great", "excellent", "nice", "love"]
negative_words = ["tight", "itchy", "pain", "hurt", "poor", "rough", "loose", "bad"]

topics_keywords = {
    "fit": ["fit", "tight", "loose"],
    "comfort": ["comfortable", "uncomfortable", "hurt", "pain"],
    "size": ["size", "small", "big"],
    "fabric": ["fabric", "material", "soft", "itchy", "rough"],
    "straps": ["strap", "straps"]
}

def analyze_review(text):
    text_lower = text.lower()

    sentiment = "Neutral"
    if any(word in text_lower for word in positive_words):
        sentiment = "Positive"
    if any(word in text_lower for word in negative_words):
        sentiment = "Negative"

    topics = []
    for topic, words in topics_keywords.items():
        if any(word in text_lower for word in words):
            topics.append(topic)

    return sentiment, topics


if st.button("Analyze Reviews"):
    if reviews_input:
        reviews = reviews_input.split("\n")

        sentiment_count = {"Positive":0, "Neutral":0, "Negative":0}
        topic_count = {"fit":0, "comfort":0, "size":0, "fabric":0, "straps":0}

        for r in reviews:
            if r.strip() == "":
                continue

            sentiment, topics = analyze_review(r)

            sentiment_count[sentiment] += 1

            for t in topics:
                topic_count[t] += 1

        # 📊 Sentiment chart
        st.subheader("Sentiment Distribution")
        st.bar_chart(pd.DataFrame(sentiment_count, index=[0]))

        # 📊 Topic chart
        st.subheader("Topic Frequency")
        st.bar_chart(pd.DataFrame(topic_count, index=[0]))

        # 🧠 Insight generation
        worst_topic = max(topic_count, key=topic_count.get)
        st.subheader("Key Insight")
        st.write(f"Most mentioned issue area: **{worst_topic}**")

    else:
        st.warning("Paste some reviews")
