import streamlit as st
import pandas as pd
import altair as alt

def show_itoperations():
    st.subheader("IT Operations Analytics")
    df = pd.DataFrame({'Step': ["Step1","Step2","Step3"], 'Delay':[5,10,3]})
    chart = alt.Chart(df).mark_bar().encode(x='Step', y='Delay')
    st.altair_chart(chart)
    st.write("Discover which staff or steps slow down helpdesk tickets.")

