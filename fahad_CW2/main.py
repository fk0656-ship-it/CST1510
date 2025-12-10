import streamlit as st
from pages.login import show_login

# -----------------------------
# User Database
# -----------------------------
USERS = {
    "fahad": "mypassword",
    "admin": "admin123"
}

# -----------------------------
# Login Function
# -----------------------------
def login():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

# -----------------------------
# Import Your Pages
# -----------------------------
from pages.home import show_home
from pages.cybersecurity import show_cybersecurity
from pages.datascience import show_datascience
from pages.itoperations import show_itoperations
from pages.ai_chatbot import show_ai_chat

# -----------------------------
# Main App Flow
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    # Sidebar navigation
    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Select a Page",
        ["Login", "Home", "Cybersecurity", "Data Science", "IT Operations", "AI Chatbot"]
    )

    if page == "Login":
        show_login()
    else:
        # Only show other pages if user is logged in
        if "logged_in" in st.session_state and st.session_state.logged_in:
            if page == "Home":
                show_home()
            elif page == "Cybersecurity":
                show_cybersecurity()
            elif page == "Data Science":
                show_datascience()
            elif page == "IT Operations":
                show_itoperations()
            elif page == "AI Chatbot":
                show_ai_chat()
        else:
            st.warning("⚠️ Please log in first to access this page.")
            show_login()
