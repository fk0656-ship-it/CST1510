import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page with interactive data!")

    # --- Sidebar filters ---
    st.sidebar.header("Filters")
    n_rows = st.sidebar.slider("Number of rows to show", min_value=5, max_value=50, value=10)

    # --- Sample DataFrame ---
    df = pd.DataFrame({
        "Category": np.random.choice(["A", "B", "C", "D"], size=100),
        "Value": np.random.randint(1, 100, size=100),
        "Score": np.random.rand(100)
    })

    st.subheader("Raw Data")
    st.dataframe(df.head(n_rows))

    # --- Interactive chart ---
    st.subheader("Interactive Chart")
    chart = alt.Chart(df.head(n_rows)).mark_bar().encode(
        x='Category',
        y='Value',
        color='Category'
    ).interactive()  # enables zooming & panning
    st.altair_chart(chart, use_container_width=True)

    # --- Sidebar selection ---
    selected_category = st.sidebar.selectbox("Select category to filter", df['Category'].unique())
    filtered_df = df[df['Category'] == selected_category]

    st.subheader(f"Filtered Data for Category {selected_category}")
    st.dataframe(filtered_df)

    # --- Metrics ---
    st.subheader("Key Metrics")
    st.metric("Max Value", filtered_df['Value'].max())
    st.metric("Average Score", round(filtered_df['Score'].mean(), 2))
