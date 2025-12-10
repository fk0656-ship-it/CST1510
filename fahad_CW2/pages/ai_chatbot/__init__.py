import streamlit as st
import random

def show_ai_chat():
    st.title("🤖 Mock AI Assistant")
    st.write("Ask a question about IT, Data Science, or Cybersecurity!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    responses = [
        "💡 Check logs regularly.", "🔒 Ensure passwords are strong.",
        "📊 Clean your data for better results.", "⚡ Optimize your workflow.",
        "✅ Keep backups of important files.", "🤔 Monitor security alerts frequently."
    ]

    user_input = st.text_input("You:", key="input")
    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        reply = random.choice(responses)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()
