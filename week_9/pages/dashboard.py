import streamlit as st

def show_dashboard():
    st.subheader("Mini Dashboard")
    kpi1 = st.slider("Select KPI 1 value", 0, 100, 50)
    kpi2 = st.slider("Select KPI 2 value", 0, 100, 75)
    st.metric("KPI 1", kpi1)
    st.metric("KPI 2", kpi2)
