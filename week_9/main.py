import streamlit as st
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
    page = st.sidebar.radio("Select Page", ["Home", "Charts", "Dashboard", "Widget"])

    # Dynamically import selected page
    if page == "Home":
        from pages.home import show_home
        show_home()
    elif page == "Charts":
        from pages.charts import show_charts
        show_charts()
    elif page == "Dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()
    elif page == "Widget":
        from pages.widget import show_widget
        show_widget()
    elif page == "AI Chat":
        from pages.ai_chatbot import show_ai_chat

        show_ai_chat()