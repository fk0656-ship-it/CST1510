# app/chatbot.py
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_ai_response(prompt):
    """Call OpenAI API and return the response text"""
    completion = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message["content"]

def show_chatbot():
    """Streamlit page for chatbot"""
    st.subheader("AI Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat messages
    for msg in st.session_state.messages:
        with st.chat_message("user"):
            st.markdown(msg["user"])
        with st.chat_message("assistant"):
            st.markdown(msg["assistant"])

    # User input
    prompt = st.chat_input("Hello, how can I help you today?")

    if prompt:
        response = get_ai_response(prompt)
        st.session_state.messages.append({"user": prompt, "assistant": response})

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)
