import streamlit as st

st.title("AI Chatbot Page")
if 'messages' not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt := st.chat_input("Ask me anything"):
    st.chat_message("user").write(prompt)
    answer = f"AI response to: {prompt}"  # placeholder
    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role":"assistant","content":answer})
