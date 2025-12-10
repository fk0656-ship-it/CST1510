import streamlit as st
st.title("Dashboard Page")
kpi = st.slider("Select KPI value", 0,100,50)
st.metric("KPI", kpi)
