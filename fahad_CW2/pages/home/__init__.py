import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import random

def show_home():
    st.title("🏠 Home Page")
    st.write("Welcome to your **Interactive CW2 Dashboard**! Explore departments and key metrics.")

    # --- Sample Data ---
    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 100),
        "Value": np.random.randint(1, 100, 100),
        "Score": np.round(np.random.rand(100)*100, 2)
    })

    # Sidebar filters
    st.sidebar.header("Filters")
    n_rows = st.sidebar.slider("Number of rows to show", 5, 50, 10)
    selected_dept = st.sidebar.selectbox("Select Department", df["Department"].unique())
    filtered_df = df[df["Department"] == selected_dept].head(n_rows)
    filtered_df = filtered_df.reset_index()  # For charts

    # --- Buttons ---
    col1, col2, col3 = st.columns(3)

    if col1.button("Show Raw Data"):
        st.subheader(f"Filtered Data for {selected_dept}")
        st.dataframe(filtered_df)

    if col2.button("Show Metrics"):
        st.subheader("Metrics")
        col1m, col2m = st.columns(2)
        col1m.metric("Max Value", filtered_df['Value'].max())
        col2m.metric("Average Score", round(filtered_df['Score'].mean(), 2))

    if col3.button("Show Charts"):
        st.subheader("Charts")
        # Bar Chart
        bar_chart = alt.Chart(filtered_df).mark_bar().encode(
            x='Department',
            y='Value',
            color='Department'
        ).interactive()
        st.altair_chart(bar_chart, use_container_width=True)
        # Line Chart
        line_chart = alt.Chart(filtered_df).mark_line(point=True, color='green').encode(
            x=alt.X('index', title='Row Number'),
            y=alt.Y('Score', title='Performance Score'),
            tooltip=['Score']
        ).interactive()
        st.altair_chart(line_chart, use_container_width=True)

    # --- Fun Random Tip ---
    if st.button("Show a Tip"):
        tips = [
            "💡 Did you know? Always check for outliers in your data!",
            "💡 Tip: Use charts to quickly understand trends.",
            "💡 Reminder: Clean data is high-quality data.",
            "💡 Fun Fact: Random data can simulate real-world scenarios!",
        ]
        st.info(random.choice(tips))

    # --- Extra Info ---
    with st.expander("ℹ️ About This Page"):
        st.write("""
        - Use sidebar filters and buttons to explore data interactively.  
        - Metrics and charts help you identify trends and top-performing departments.  
        - This page is designed for beginners but is fully functional for CW2 analytics.
        """)
