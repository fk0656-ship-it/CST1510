import streamlit as st

st.title("Streamlit Test App")

st.write("Hello! This is a minimal Streamlit app to test your setup.")

name = st.text_input("Enter your name:")
if st.button("Greet me"):
    st.success(f"Hello, {name}!")
