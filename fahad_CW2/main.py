import streamlit as st
from pages.home import show_home
from pages.cybersecurity import show_cybersecurity
from pages.datascience import show_datascience
from pages.itoperations import show_itoperations

USERS = {
    "fahad": "FAHAD123",
    "Fahad": "fahad123",
    "hello": "hru"
}

# --- Session state for login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- Login section ---
if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    show_pass = st.checkbox("Show password")
    if show_pass:
        password = st.text_input("Password (visible)", value=password)

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.success(f"✅ Welcome, {username}!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("❌ Invalid username or password")

else:
    # --- Sidebar navigation ---
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a Page",
        ["Home", "Cybersecurity", "Data Science", "IT Operations",]
    )

    # --- Show selected page ---
    if page == "Home":
        show_home()
    elif page == "Cybersecurity":
        show_cybersecurity()
    elif page == "Data Science":
        show_datascience()
    elif page == "IT Operations":
        show_itoperations()

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()
