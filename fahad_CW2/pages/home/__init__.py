import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_home():
    st.title("Home Page")
    st.write("Welcome to the interactive Home Page!")

    # Sidebar filters
    st.sidebar.header("Filters")
    n_rows = st.sidebar.slider("Number of rows to show", 5, 50, 10)

    # Sample data
    df = pd.DataFrame({
        "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], 100),
        "Value": np.random.randint(1, 100, 100),
        "Score": np.round(np.random.rand(100)*100, 2)
    })

    st.subheader("Raw Data")
    st.dataframe(df.head(n_rows))

    # Interactive chart
    st.subheader("Value by Department")
    chart = alt.Chart(df.head(n_rows)).mark_bar().encode(
        x='Department',
        y='Value',
        color='Department'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    # Filtered data
    selected_dept = st.sidebar.selectbox("Select Department", df['Department'].unique())
    filtered_df = df[df['Department'] == selected_dept]

    st.subheader(f"Filtered Data: {selected_dept}")
    st.dataframe(filtered_df)

    # Metrics
    col1, col2 = st.columns(2)
    col1.metric("Max Value", filtered_df['Value'].max())
    col2.metric("Average Score", filtered_df['Score'].mean())
