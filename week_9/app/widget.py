import streamlit as st

def show():
    st.header(" Widgets")

    name = st.text_input("Enter your name")
    color = st.color_picker("Pick a color")
    agree = st.checkbox("I agree")

    if name and agree:
        st.success(f"Hello {name}! Your selected color is {color}.")
