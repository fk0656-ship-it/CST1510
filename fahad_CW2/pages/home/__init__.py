import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_home():
    st.title("🏠 Home Page")
    st.write("""
    Welcome to your **Interactive CW2 Dashboard**!  
    Explore departments, key metrics, and simple data analytics.
    """)

    # --- Overview Metrics ---
    st.subheader("📊 Overview Metrics")
    total_departments = 4
    total_records = 100
    avg_score = round(np.random.rand() * 100, 2)
    max_value = np.random.randint(80, 100)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Departments", total_departments)
    col2.metric("Total Records", total_records)
    col3.metric("Average Score", avg_score)
    col4.metric("Max Value", max_value)

    # --- Sample Data ---
    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 100),
        "Value": np.random.randint(1, 100, 100),
        "Score": np.round(np.random.rand(100)*100, 2)
    })

    # Sidebar filters
    st.sidebar.header("Home Page Filters")
    n_rows = st.sidebar.slider("Number of rows to show", 5, 50, 10)
    selected_dept = st.sidebar.selectbox("Select Department", df["Department"].unique())

    # Filter data
    filtered_df = df[df["Department"] == selected_dept].head(n_rows)
    filtered_df = filtered_df.reset_index()  # Fix for Altair line chart

    st.subheader(f"Filtered Data: {selected_dept}")
    st.dataframe(filtered_df)

    # Metrics for selected department
    st.subheader("Metrics")
    col1, col2 = st.columns(2)
    col1.metric("Max Value", filtered_df['Value'].max())
    col2.metric("Average Score", round(filtered_df['Score'].mean(), 2))

    # --- Charts ---
    st.subheader("Value by Department (Bar Chart)")
    bar_chart = alt.Chart(filtered_df).mark_bar().encode(
        x='Department',
        y='Value',
        color='Department'
    ).interactive()
    st.altair_chart(bar_chart, use_container_width=True)

    st.subheader("Score Trends (Line Chart)")
    line_chart = alt.Chart(filtered_df).mark_line(point=True, color='green').encode(
        x=alt.X('index', title='Row Number'),  # Use index column
        y=alt.Y('Score', title='Performance Score'),
        tooltip=['Score']
    ).interactive()
    st.altair_chart(line_chart, use_container_width=True)

    # --- Informative Section ---
    st.subheader("ℹ️ About This Page")
    st.write("""
    - Use the sidebar to filter the number of rows and select departments.  
    - Metrics and charts help you quickly identify performance trends.  
    - This page is beginner-friendly and perfect for CW2 analytics.
    """)
