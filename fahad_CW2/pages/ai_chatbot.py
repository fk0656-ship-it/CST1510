import streamlit as st
from openai import OpenAI

def show_ai_chat():
    st.title("AI Assistant")

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    question = st.text_input("Ask anything:")

    if question:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        st.write(response.choices[0].message.content)
