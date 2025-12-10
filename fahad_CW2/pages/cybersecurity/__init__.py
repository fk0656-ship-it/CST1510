import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_cybersecurity():
    st.title("Cybersecurity Page")
    st.write("Interactive Cybersecurity Dashboard")

    st.sidebar.header("Filters")
    n_rows = st.sidebar.slider("Rows to display", 5, 50, 10)

    df = pd.DataFrame({
        "Threat Type": np.random.choice(["Malware", "Phishing", "Ransomware", "DDoS"], 100),
        "Incidents": np.random.randint(1, 50, 100),
        "Severity": np.random.randint(1, 10, 100)
    })

    st.subheader("Threat Incidents Data")
    st.dataframe(df.head(n_rows))

    chart = alt.Chart(df.head(n_rows)).mark_line(point=True).encode(
        x='Threat Type',
        y='Incidents',
        color='Threat Type'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    selected_threat = st.sidebar.selectbox("Select Threat Type", df['Threat Type'].unique())
    filtered_df = df[df['Threat Type'] == selected_threat]

    st.subheader(f"Filtered: {selected_threat}")
    st.dataframe(filtered_df)

    col1, col2 = st.columns(2)
    col1.metric("Max Incidents", filtered_df['Incidents'].max())
    col2.metric("Avg Severity", filtered_df['Severity'].mean())
