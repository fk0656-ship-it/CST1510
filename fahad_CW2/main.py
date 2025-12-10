import streamlit as st
import bcrypt
import os

from pages.home import show_home
from pages.cybersecurity import show_cybersecurity
from pages.datascience import show_datascience
from pages.itoperations import show_itoperations
from pages.ai_chatbot import show_ai_chat

USER_DATA_FILE = "users.txt"


def hash_password(pw):
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()


def verify_password(pw, hashed):
    return bcrypt.checkpw(pw.encode(), hashed.encode())


def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE) as f:
        for line in f:
            if line.strip().split(",")[0] == username:
                return True
    return False


def register_user(username, password):
    hashed = hash_password(password)
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{hashed}\n")


def authenticate(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE) as f:
        for line in f:
            u, h = line.strip().split(",")
            if u == username and verify_password(password, h):
                return True
    return False


# --- SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""


# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.title("CW2 Multi-Domain Dashboard")
    mode = st.radio("Choose an option:", ["Login", "Register"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Submit"):

        if mode == "Register":
            if user_exists(username):
                st.error("Username already exists.")
            else:
                register_user(username, password)
                st.success("Registration successful. Please login.")

        else:
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

else:
    # --------- AFTER LOGIN -----------
    st.sidebar.write(f"Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    page = st.sidebar.radio(
        "Select Page:",
        ["Home", "Cybersecurity", "Data Science", "IT Operations", "AI Chat"]
    )

    if page == "Home":
        show_home()
    elif page == "Cybersecurity":
        show_cybersecurity()
    elif page == "Data Science":
        show_datascience()
    elif page == "IT Operations":
        show_itoperations()
    elif page == "AI Chat":
        show_ai_chat()
