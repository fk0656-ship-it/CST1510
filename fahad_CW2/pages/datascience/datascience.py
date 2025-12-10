import streamlit as st
import pandas as pd

def show_datascience():
    st.title("Data Science Dashboard")
    st.write("Dataset quality and analysis")

    df = pd.read_csv("data/sample.csv")
    st.line_chart(df)
