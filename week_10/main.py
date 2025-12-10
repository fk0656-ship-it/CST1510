import streamlit as st
from openai import OpenAI
import pandas as pd
import numpy as np

# ----------------------
# OpenAI client
# ----------------------
if "openai" in st.secrets and "api_key" in st.secrets["openai"]:
    client = OpenAI(api_key=st.secrets["openai"]["api_key"])
else:
    client = None
    st.warning("OpenAI API key not found! Chatbot disabled.")

# ----------------------
# Login
# ----------------------
USERS = {"fahad": "FAHAD123@", "user2": "password"}

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if not st.session_state['logged_in']:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")
else:
    st.title(f"Dashboard - {st.session_state['username']}")
    page = st.sidebar.selectbox("Select Page", [
        "Home", "Charts", "Layout", "Mini Dashboard", "Widgets", "Chatbot"
    ])
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()

    # ----------------------
    # Home Page
    # ----------------------
    if page == "Home":
        st.subheader("Welcome to your Dashboard")
        st.markdown("""
        This is your interactive dashboard. Use the sidebar to navigate between pages:
        - Charts
        - Layout
        - Mini Dashboard
        - Widgets
        - Chatbot
        """)

    # ----------------------
    # Charts Page
    # ----------------------
    elif page == "Charts":
        st.subheader("Sales and Revenue Charts")
        data = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
            "Sales": [150, 200, 180, 220, 210],
            "Revenue": [1000, 1500, 1200, 1800, 1600]
        }).set_index("Month")
        st.line_chart(data)
        st.bar_chart(data)

    # ----------------------
    # Layout Page
    # ----------------------
    elif page == "Layout":
        st.subheader("Metrics Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Users", 1234, 50)
        col2.metric("Revenue", "$12,345", "+3%")
        col3.metric("Orders", 234, -5)

        st.markdown("### Quick Stats")
        col1, col2 = st.columns(2)
        col1.write("Active Users: 102")
        col2.write("Pending Orders: 23")

    # ----------------------
    # Mini Dashboard Page
    # ----------------------
    elif page == "Mini Dashboard":
        st.subheader("Mini Dashboard Widgets")
        col1, col2 = st.columns(2)
        col1.metric("Revenue", "$7,890", "+5%")
        col2.metric("Profit", "$3,210", "+8%")
        st.line_chart(np.random.randn(10, 2), use_container_width=True)

    # ----------------------
    # Widgets Page
    # ----------------------
    elif page == "Widgets":
        st.subheader("Interactive Widgets")
        st.checkbox("Check me!")
        st.radio("Pick an option:", ["Option 1", "Option 2", "Option 3"])
        st.selectbox("Choose one:", ["A", "B", "C"])
        st.slider("Select a number", 0, 100, 50)
        st.text_area("Write something:")

    # ----------------------
    # Chatbot Page
    # ----------------------
    elif page == "Chatbot":
        if client is None:
            st.info("Chatbot is disabled because OpenAI API key is missing.")
        else:
            st.subheader("Chatbot - Ask AI anything")

            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                else:
                    st.markdown(f"**AI:** {msg['content']}")

            # Form for safe input
            with st.form(key="chat_form", clear_on_submit=True):
                user_input = st.text_input("Your question:")
                submit_button = st.form_submit_button("Send")

                if submit_button and user_input:
                    st.session_state.messages.append({"role": "user", "content": user_input})

                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=st.session_state.messages
                    )

                    ai_reply = response.choices[0].message.content
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

            if st.button("Clear Chat"):
                st.session_state.messages = []
                st.experimental_rerun()
