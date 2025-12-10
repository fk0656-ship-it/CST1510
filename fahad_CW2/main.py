import streamlit as st

from pages.home import show_home
from pages.itoperations import show_itoperations
from pages.datascience import show_datascience
from pages.cybersecurity import show_cybersecurity
from pages.ai_chatbot import show_ai_chat
from pages.database import show_database

st.set_page_config(page_title="CW2 Interactive App", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Page",
    ["Home", "IT Operations", "Data Science", "Cybersecurity", "AI Chatbot", "Database"]
)

if page == "Home":
    show_home()
elif page == "IT Operations":
    show_itoperations()
elif page == "Data Science":
    show_datascience()
elif page == "Cybersecurity":
    show_cybersecurity()
elif page == "AI Chatbot":
    show_ai_chat()
elif page == "Database":
    show_database()
