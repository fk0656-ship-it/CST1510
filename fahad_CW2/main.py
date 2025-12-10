import streamlit as st

from pages.home import show_home
from pages.cybersecurity import show_cybersecurity
from pages.datascience import show_datascience
from pages.itoperations import show_itoperations
from pages.ai_chatbot import show_ai_chat

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Page",
    ["Home", "Cybersecurity", "Data Science", "IT Operations", "AI Chatbot"]
)

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
