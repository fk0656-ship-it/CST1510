import streamlit as st
import pandas as pd
import altair as alt

def show_cybersecurity():
    st.subheader("Cybersecurity Analytics")
    df = pd.DataFrame({'Attacks': [5,10,7,15,6], 'Week':[1,2,3,4,5]})
    chart = alt.Chart(df).mark_line().encode(x='Week', y='Attacks')
    st.altair_chart(chart)
    st.write("Analyze phishing attack trends and workflow issues.")
