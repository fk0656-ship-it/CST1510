import streamlit as st

def show():
    st.header(" Dashboard")

    st.write("Simple dashboard-like boxes:")

    col1, col2, col3 = st.columns(3)
    col1.metric("Users", "120")
    col2.metric("Active", "57")
    col3.metric("Errors", "3")
