import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Lingerie Feedback Analyzer (Insights Mode)")

reviews_input = st.text_area("Paste multiple reviews (one per line)")

def analyze_review(text):
    prompt = f"""
You are analyzing lingerie product reviews.

Return in JSON:
{{
  "sentiment": "Positive/Neutral/Negative",
  "topics": ["fit","comfort","size","fabric","straps"]
}}

Review: "{text}"
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if st.button("Analyze Reviews"):
    if reviews_input:
        reviews = reviews_input.split("\n")

        results = []
        sentiment_count = {"Positive":0, "Neutral":0, "Negative":0}
        topic_count = {"fit":0, "comfort":0, "size":0, "fabric":0, "straps":0}

        for r in reviews:
            if r.strip() == "":
                continue

            output = analyze_review(r)

            # basic parsing (not perfect but works for demo)
            if "Positive" in output:
                sentiment_count["Positive"] += 1
            elif "Negative" in output:
                sentiment_count["Negative"] += 1
            else:
                sentiment_count["Neutral"] += 1

            for t in topic_count.keys():
                if t in output.lower():
                    topic_count[t] += 1

        st.subheader("Sentiment Summary")
        st.write(sentiment_count)

        st.subheader("Top Topics")
        st.write(topic_count)

    else:
        st.warning("Paste some reviews")
