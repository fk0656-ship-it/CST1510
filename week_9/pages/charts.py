import streamlit as st
import pandas as pd
import altair as alt

st.title("Charts Page")
df = pd.DataFrame({'x': range(10), 'y':[i**2 for i in range(10)]})
st.altair_chart(alt.Chart(df).mark_line().encode(x='x',y='y'), use_container_width=True)
