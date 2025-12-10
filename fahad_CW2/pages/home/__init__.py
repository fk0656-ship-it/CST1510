import streamlit as st


def show_home():
    st.title("🏠 Home Page")
    st.write("Welcome to your CW2 Interactive Dashboard!")

    st.subheader("Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Servers", 5)
    col2.metric("Total Incidents", 120)
    col3.metric("Datasets Available", 3)

    st.write("Use the sidebar to navigate through different sections of the app!")
