import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_datascience():
    st.title("📊 Data Science Page")
    st.write("Explore datasets and visualize key metrics!")

    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 100),
        "Salary": np.random.randint(3000, 10000, 100),
        "Experience (Years)": np.random.randint(1, 20, 100)
    })

    st.subheader("Raw Data")
    st.dataframe(df.head(10))

    st.sidebar.header("Filters")
    selected_dept = st.sidebar.selectbox("Select Department", df["Department"].unique())
    filtered_df = df[df["Department"] == selected_dept]

    st.subheader(f"Filtered Data: {selected_dept}")
    st.dataframe(filtered_df)

    col1, col2 = st.columns(2)
    col1.metric("Max Salary", filtered_df["Salary"].max())
    col2.metric("Average Experience", round(filtered_df["Experience (Years)"].mean(), 1))

    st.subheader("Salary vs Experience Chart")
    chart = alt.Chart(filtered_df).mark_circle(size=100).encode(
        x="Experience (Years)",
        y="Salary",
        color="Department",
        tooltip=["Salary", "Experience (Years)"]
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
