import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def show_ai_chat():
    st.title("🤖 AI Chatbot")
    st.write("Ask questions about IT, Data Science, or Cybersecurity!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")
