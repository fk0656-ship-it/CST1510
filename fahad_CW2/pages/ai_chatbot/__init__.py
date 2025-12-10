import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def show_ai_chat():
    st.title("AI Chatbot")
    st.write("Ask questions about IT operations, cybersecurity, or data science!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # User input
    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Send request to OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})

    # Display chat
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")
