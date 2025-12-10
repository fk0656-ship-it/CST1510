import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_datascience():
    st.title("📊 Data Science Dashboard")
    st.write("Explore large datasets, check for missing values, and improve data quality.")

    # Sample dataset
    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 500),
        "Salary": np.random.randint(3000, 12000, 500),
        "Experience": np.random.randint(1, 20, 500),
        "Performance": np.round(np.random.rand(500)*100, 2)
    })

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))

    # Buttons
    col1, col2, col3 = st.columns(3)

    if col1.button("Check Missing Values"):
        st.dataframe(df.isnull().sum())

    if col2.button("Remove Duplicates"):
        before = df.shape[0]
        df.drop_duplicates(inplace=True)
        after = df.shape[0]
        st.success(f"Removed {before - after} duplicate rows!")

    if col3.button("Show Summary Stats"):
        st.write(df.describe())

    # Filter by Department
    dept = st.selectbox("Select Department", df["Department"].unique())
    dept_df = df[df["Department"] == dept]
    st.dataframe(dept_df.head(10))

    # Chart: Average Salary per Department
    chart = alt.Chart(df).mark_bar().encode(
        x='Department',
        y='mean(Salary)',
        color='Department'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
