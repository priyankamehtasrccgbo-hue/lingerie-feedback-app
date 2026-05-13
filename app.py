import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("🛍️ AI Product Attribute Extractor")

user_input = st.text_area("Enter product description:")

if st.button("Extract Attributes"):
    if user_input:
        prompt = f"""
        Extract structured attributes from the product description below.
        Return JSON with keys like fabric, padding, support, wire, use_case.

        Description:
        {user_input}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        st.code(response.choices[0].message.content, language="json")
