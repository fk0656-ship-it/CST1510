import streamlit as st
from openai import OpenAI


def show_ai_chat():
    st.subheader("AI Chat Assistant")

    if "openai" not in st.secrets or "api_key" not in st.secrets["openai"]:
        st.warning("OpenAI API key not found. AI is disabled.")
        return

    client = OpenAI(api_key=st.secrets["openai"]["api_key"])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**AI:** {msg['content']}")

    user_input = st.text_input("Ask AI:")
    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        ai_reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        st.experimental_rerun()
