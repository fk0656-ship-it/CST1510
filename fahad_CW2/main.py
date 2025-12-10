import streamlit as st

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


from pages.home import show_home
from pages.cybersecurity import show_cybersecurity
from pages.datascience import show_datascience
from pages.itoperations import show_itoperations
from pages.ai_chatbot import show_ai_chat

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    # Sidebar navigation
    import streamlit as st

    from pages.home import show_home
    from pages.cybersecurity import show_cybersecurity
    from pages.datascience import show_datascience
    from pages.itoperations import show_itoperations
    from pages.ai_chatbot import show_ai_chat

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a Page",
        ["Home", "Cybersecurity", "Data Science", "IT Operations", "AI Chatbot"]
    )

    # Show the selected page
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
