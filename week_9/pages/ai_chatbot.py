import streamlit as st

# Try importing OpenAI safely
try:
    from openai import OpenAI
    client = OpenAI(api_key=st.secrets["openai"]["api_key"])
    openai_available = True
except ModuleNotFoundError:
    openai_available = False

def show_ai_chat():
    st.subheader("AI Chat")
    if not openai_available:
        st.warning("OpenAI module not installed. AI chat is unavailable.")
    else:
        if 'messages' not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            st.chat_message(msg['role']).write(msg['content'])

        if prompt := st.chat_input("Ask me anything"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            with st.spinner("AI is thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=st.session_state.messages
                )
                answer = response.choices[0].message["content"]
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.chat_message("assistant").write(answer)
