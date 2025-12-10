# week_9/pages/ai_chatbot.py
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = None
if "openai" in st.secrets and "api_key" in st.secrets["openai"]:
    client = OpenAI(api_key=st.secrets["openai"]["api_key"])
else:
    st.warning("OpenAI API key not found! Chatbot will be disabled.")

def show_ai_chat():
    st.subheader("AI Chat")

    if client is None:
        st.info("Chatbot is disabled because OpenAI API key is missing.")
        return

    # Initialize session state for messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display previous chat messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**AI:** {msg['content']}")

    # Form for user input
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Your question:")
        submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Call OpenAI Chat API
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )

            # FIX: Use .content, not ["content"]
            answer = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": answer})

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()
