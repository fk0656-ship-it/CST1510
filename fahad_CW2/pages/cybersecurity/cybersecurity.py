import streamlit as st
import pandas as pd

def show_cybersecurity():
    st.title("Cybersecurity Dashboard")
    st.write("Phishing incident monitoring")

    df = pd.read_csv("data/sample.csv")
    st.bar_chart(df)
