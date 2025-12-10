import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_datascience():
    st.title("📊 Data Science: Tame Large Datasets & Improve Data Quality")
    st.write("""
    This page lets you explore a dataset, detect missing values, remove duplicates, 
    and visualize data quality interactively.
    """)

    # --- Sample large dataset ---
    np.random.seed(42)
    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 500),
        "Salary": np.random.randint(3000, 12000, 500),
        "Experience (Years)": np.random.randint(1, 20, 500),
        "Performance Score": np.round(np.random.rand(500)*100, 2)
    })

    st.subheader("Preview Dataset")
    st.dataframe(df.head(10))

    # --- Buttons for interactivity ---
    col1, col2 = st.columns(2)

    if col1.button("Check Missing Values"):
        st.write("Missing values in each column:")
        st.dataframe(df.isnull().sum())

    if col2.button("Remove Duplicate Rows"):
        before = df.shape[0]
        df.drop_duplicates(inplace=True)
        after = df.shape[0]
        st.success(f"Removed {before - after} duplicate rows!")

    # --- Metrics ---
    st.subheader("Dataset Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Average Salary", round(df["Salary"].mean(), 2))

    # --- Simple chart ---
    st.subheader("Salary Distribution by Department")
    chart = alt.Chart(df).mark_bar().encode(
        x='Department',
        y='mean(Salary)',
        color='Department'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    # --- Filter by Department ---
    st.subheader("Filter Department Data")
    selected_dept = st.selectbox("Select Department", df["Department"].unique())
    filtered_df = df[df["Department"] == selected_dept]
    st.dataframe(filtered_df.head(10))

    # --- Button for basic summary stats ---
    if st.button(f"Show Summary Statistics for {selected_dept}"):
        st.write(filtered_df.describe())
