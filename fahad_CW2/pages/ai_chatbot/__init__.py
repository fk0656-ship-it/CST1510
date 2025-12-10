import streamlit as st
import random

def show_ai_chat():
    st.title("🤖 Mock AI Assistant")
    st.write("Ask a question about IT, Data Science, or Cybersecurity, and get a random response!")

    # Initialize chat session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Predefined random responses
    responses = [
        "That's interesting! You should check the logs.",
        "I recommend optimizing your code for better performance.",
        "Have you tried turning it off and on again?",
        "Data quality is key! Always check for missing values.",
        "Security first! Make sure passwords are strong.",
        "Collaboration with the team can improve efficiency.",
        "This looks like a common issue; monitor it closely.",
        "Try filtering the dataset before analysis.",
        "Remember to back up your files regularly!",
        "Keep learning and experimenting, it's the best way!"
    ]

    # User input
    user_input = st.text_input("You:", key="input")
    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Random response
        reply = random.choice(responses)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

    # Clear chat
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()
