import streamlit as st
import pandas as pd
import altair as alt

def show_charts():
    st.subheader("Charts Page")
    df = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
    chart = alt.Chart(df).mark_line(color='green').encode(x='x', y='y')
    st.altair_chart(chart, use_container_width=True)
