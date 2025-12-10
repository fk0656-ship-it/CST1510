import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_itoperations():
    st.title("IT Operations Page")
    st.write("Interactive IT Operations Dashboard")

    st.sidebar.header("Filters")
    n_rows = st.sidebar.slider("Rows to display", 5, 50, 10)

    df = pd.DataFrame({
        "Server": np.random.choice(["Server1", "Server2", "Server3", "Server4"], 100),
        "CPU Usage": np.random.randint(1, 100, 100),
        "Memory Usage": np.random.randint(1, 100, 100)
    })

    st.subheader("Server Performance Data")
    st.dataframe(df.head(n_rows))

    chart = alt.Chart(df.head(n_rows)).mark_line(point=True).encode(
        x='Server',
        y='CPU Usage',
        color='Server'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    selected_server = st.sidebar.selectbox("Select Server", df['Server'].unique())
    filtered_df = df[df['Server'] == selected_server]

    st.subheader(f"Filtered: {selected_server}")
    st.dataframe(filtered_df)

    col1, col2 = st.columns(2)
    col1.metric("Max CPU", filtered_df['CPU Usage'].max())
    col2.metric("Max Memory", filtered_df['Memory Usage'].max())
