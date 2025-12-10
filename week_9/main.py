import streamlit as st
import pandas as pd
import altair as alt
import sqlite3
from openai import OpenAI

# OpenAI Client
# --------------------------
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# --------------------------
# LOGIN SIMULATION
# --------------------------
USERS = {
    "user1": "pass1",
    "fahad": "mypassword"
}

st.title("Week 9 App")

# Session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Incorrect username or password")
else:
    st.sidebar.write(f"Logged in as: {st.session_state.username}")

    # --------------------------
    # Navigation
    # --------------------------
    page = st.sidebar.radio("Select Page", ["Home", "Charts", "Dashboard", "AI Chat"])

    if page == "Home":
        st.subheader("Home Page")
        st.write("Welcome to your Week 9 app!")

    elif page == "Charts":
        st.subheader("Charts Page")
        # Example chart
        df = pd.DataFrame({
            'x': range(10),
            'y': [i ** 2 for i in range(10)]
        })
        chart = alt.Chart(df).mark_line().encode(
            x='x', y='y'
        )
        st.altair_chart(chart, use_container_width=True)

    elif page == "Dashboard":
        st.subheader("Mini Dashboard")
        st.write("Here you can add your widgets and data insights")

    elif page == "AI Chat":
        st.subheader("Chat with AI")
        if 'messages' not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            st.chat_message(message['role']).write(message['content'])

        if prompt := st.chat_input("Ask me anything"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.spinner("AI is thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=st.session_state.messages
                )
                answer = response.choices[0].message["content"]
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.chat_message("assistant").write(answer)
