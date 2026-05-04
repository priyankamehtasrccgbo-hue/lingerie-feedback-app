import streamlit as st

st.title("Lingerie Feedback Analyzer (Free Version)")

reviews_input = st.text_area("Paste multiple reviews (one per line)")

# keyword rules
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

    # sentiment
    sentiment = "Neutral"
    if any(word in text_lower for word in positive_words):
        sentiment = "Positive"
    if any(word in text_lower for word in negative_words):
        sentiment = "Negative"

    # topics
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

        st.subheader("Sentiment Summary")
        st.write(sentiment_count)

        st.subheader("Top Topics")
        st.write(topic_count)

    else:
        st.warning("Paste some reviews")
