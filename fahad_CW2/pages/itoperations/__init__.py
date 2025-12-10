import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_itoperations():
    st.title("IT Operations Dashboard")
    st.write("Monitor server performance and IT metrics interactively!")

    # Sample server data
    servers = ["Server-01", "Server-02", "Server-03", "Server-04", "Server-05"]
    df = pd.DataFrame({
        "Server": np.random.choice(servers, 100),
        "CPU Usage (%)": np.random.randint(10, 100, 100),
        "Memory Usage (%)": np.random.randint(20, 100, 100),
        "Disk Usage (%)": np.random.randint(10, 90, 100),
        "Network Traffic (MB/s)": np.random.randint(5, 500, 100)
    })

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_server = st.sidebar.selectbox("Select Server", df['Server'].unique())
    n_rows = st.sidebar.slider("Number of rows to display", 5, 50, 10)

    filtered_df = df[df["Server"] == selected_server]

    # Display filtered data
    st.subheader(f"Performance Data: {selected_server}")
    st.dataframe(filtered_df.head(n_rows))

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Max CPU (%)", filtered_df["CPU Usage (%)"].max())
    col2.metric("Max Memory (%)", filtered_df["Memory Usage (%)"].max())
    col3.metric("Max Disk (%)", filtered_df["Disk Usage (%)"].max())
    col4.metric("Max Network (MB/s)", filtered_df["Network Traffic (MB/s)"].max())

    # Charts
    st.subheader("CPU and Memory Usage Chart")
    chart = alt.Chart(filtered_df.head(n_rows)).transform_fold(
        ["CPU Usage (%)", "Memory Usage (%)"]
    ).mark_line(point=True).encode(
        x="index:Q",
        y="value:Q",
        color="key:N"
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
