import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_home():
    st.title("🏠 Home Page")
    st.write("""
    Welcome to your **Interactive CW2 Dashboard**!  
    This app provides insights into IT Operations, Data Science, Cybersecurity, and AI.  
    Use the sidebar to navigate between pages.
    """)

    # --- Overview Cards ---
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

    # --- Sample Data Analytics ---
    st.subheader("📈 Sample Analytics by Department")

    # Sample dataset
    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 100),
        "Value": np.random.randint(1, 100, 100),
        "Score": np.round(np.random.rand(100)*100, 2)
    })

    # Sidebar filters
    st.sidebar.header("Home Page Filters")
    n_rows = st.sidebar.slider("Number of rows to show", 5, 50, 10)
    selected_dept = st.sidebar.selectbox("Select Department", df['Department'].unique())

    # Display filtered table
    filtered_df = df[df['Department'] == selected_dept]
    st.dataframe(filtered_df.head(n_rows))

    # Metrics for selected department
    st.subheader(f"Metrics for {selected_dept}")
    col1, col2 = st.columns(2)
    col1.metric("Max Value", filtered_df['Value'].max())
    col2.metric("Average Score", round(filtered_df['Score'].mean(), 2))

    # Charts
    st.subheader("Visual Insights")
    # Bar chart for Value by Department
    bar_chart = alt.Chart(filtered_df.head(n_rows)).mark_bar().encode(
        x='Department',
        y='Value',
        color='Department'
    ).interactive()
    st.altair_chart(bar_chart, use_container_width=True)

    # Line chart for Score trends
    line_chart = alt.Chart(filtered_df.head(n_rows)).mark_line(point=True, color='green').encode(
        x=filtered_df.head(n_rows).index,
        y='Score',
        tooltip=['Score']
    ).interactive()
    st.altair_chart(line_chart, use_container_width=True)

    # Informative section
    st.subheader("ℹ️ About This Page")
    st.write("""
    - Use this page to get a quick overview of your departments and key metrics.  
    - Filter by department and adjust the number of rows using the sidebar.  
    - Visual charts help you quickly identify high-performing departments and trends.
    """)
