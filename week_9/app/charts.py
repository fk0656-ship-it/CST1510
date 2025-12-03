# app/charts.py
import streamlit as st

def show():
    st.header("Charts Demo")
    st.write("A placeholder chart demo (no pandas needed).")

    # Simple data as a dictionary
    data = {
        "Day 1": 10,
        "Day 2": 25,
        "Day 3": 30,
        "Day 4": 20,
        "Day 5": 40
    }

    st.line_chart(data)
    st.write("✅ Chart should now be visible!")
