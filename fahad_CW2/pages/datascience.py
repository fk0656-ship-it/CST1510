import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_datascience():
    st.subheader("Data Science Analytics")
    df = pd.DataFrame({'X': range(10), 'Y': np.random.randint(1,50,10)})
    chart = alt.Chart(df).mark_bar().encode(x='X', y='Y')
    st.altair_chart(chart)
    st.write("Explore large datasets and improve data quality.")
