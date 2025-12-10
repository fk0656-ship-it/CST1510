import streamlit as st

def show_widget():
    st.subheader("Widget Page")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=120)
    if st.button("Submit"):
        st.write(f"Hello {name}, you are {age} years old!")
