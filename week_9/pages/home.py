import streamlit as st

def show_home():
    st.subheader("Home Page")
    st.write("Welcome to Week 9 app!")
    if st.button("Click me for a greeting"):
        st.success(f"Hello, {st.session_state.username}! Have a great day!")
