import streamlit as st
import pandas as pd
import altair as alt
from openai import OpenAI
# Check if OpenAI is available
try:
    from openai import OpenAI
    client = OpenAI(api_key=st.secrets["openai"]["api_key"])
    openai_available = True
except ModuleNotFoundError:
    openai_available = False

st.title("Week 9 App")

# Session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

USERS = {"user1": "pass1", "fahad": "mypassword"}

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
    page = st.sidebar.radio("Select Page", ["Home", "Charts", "Dashboard", "Widget", "AI Chat"])

    if page == "Home":
        st.subheader("Home Page")
        st.write("Welcome! Explore charts, dashboard, widgets, or chat with AI below.")
        if st.button("Click me for a greeting"):
            st.success(f"Hello, {st.session_state.username}! Have a great day!")

    elif page == "Charts":
        st.subheader("Charts Page")
        df = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
        chart = alt.Chart(df).mark_line(color='green').encode(x='x', y='y')
        st.altair_chart(chart, use_container_width=True)
        st.write("You can update data dynamically:")
        new_val = st.number_input("Add new y-value squared for x=10", value=100)
        if st.button("Add data point"):
            df = pd.concat([df, pd.DataFrame({'x':[10],'y':[new_val]})], ignore_index=True)
            chart = alt.Chart(df).mark_line(color='blue').encode(x='x', y='y')
            st.altair_chart(chart, use_container_width=True)

    elif page == "Dashboard":
        st.subheader("Mini Dashboard")
        st.write("Interactive KPI dashboard")
        kpi1 = st.slider("Select KPI 1 value", 0, 100, 50)
        kpi2 = st.slider("Select KPI 2 value", 0, 100, 75)
        st.metric("KPI 1", kpi1)
        st.metric("KPI 2", kpi2)

    elif page == "Widget":
        st.subheader("Widget Page")
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=1, max_value=120)
        if st.button("Submit"):
            st.write(f"Hello {name}, you are {age} years old!")

    elif page == "AI Chat":
        st.subheader("AI Chat")
        if not openai_available:
            st.warning("OpenAI module not installed. AI chat is not available.")
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
