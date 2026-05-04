import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Lingerie Feedback Analyzer")

review = st.text_area("Enter customer review")

def analyze_review(text):
    prompt = f"""
You are analyzing lingerie product reviews.

Return:
1. Sentiment: Positive / Neutral / Negative
2. Topics: choose only from [fit, comfort, size, fabric, straps]

Review: "{text}"

Give output in this format:
Sentiment: <value>
Topics: <comma separated>
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if st.button("Analyze"):
    if review:
        result = analyze_review(review)
        st.write(result)
