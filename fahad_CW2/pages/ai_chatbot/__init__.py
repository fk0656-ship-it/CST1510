import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def show_ai_chat():
    st.title("🤖 AI Chatbot Helper")
    st.write("Ask about IT Operations, Data Science, or Cybersecurity!")

    # Initialize chat session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # User input
    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})

    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

    # Optional: Clear chat
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()
