import streamlit as st

def show():
    st.header(" Layout ")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Left column content")
        st.button("Left button")

    with col2:
        st.write("Right column content")
        st.button("Right button")