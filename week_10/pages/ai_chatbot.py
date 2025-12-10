import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def show_ai_chatbot():
    st.subheader("AI Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**AI:** {msg['content']}")

    # Get user input
    prompt = st.chat_input("Ask me anything")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("AI is thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )

            # Correct way to access response text
            answer = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": answer})

        st.markdown(f"**You:** {prompt}")
        st.markdown(f"**AI:** {answer}")
