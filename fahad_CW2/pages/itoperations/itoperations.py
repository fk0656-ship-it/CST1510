import streamlit as st
import pandas as pd

def show_itoperations():
    st.title("IT Operations Dashboard")
    st.write("Helpdesk performance insights")

    df = pd.read_csv("data/sample.csv")
    st.area_chart(df)
