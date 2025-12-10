import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_cybersecurity():
    st.title("🛡 Cybersecurity Dashboard")
    st.write("Track threats and incidents interactively!")

    threats = ["Malware", "Phishing", "Ransomware", "DDoS"]
    df = pd.DataFrame({
        "Threat Type": np.random.choice(threats, 100),
        "Incidents": np.random.randint(1, 50, 100),
        "Severity": np.random.randint(1, 10, 100)
    })

    st.sidebar.header("Filters")
    selected_threat = st.sidebar.selectbox("Select Threat", df["Threat Type"].unique())
    filtered_df = df[df["Threat Type"] == selected_threat]

    st.subheader(f"Filtered Data: {selected_threat}")
    st.dataframe(filtered_df.head(10))

    col1, col2 = st.columns(2)
    col1.metric("Max Incidents", filtered_df["Incidents"].max())
    col2.metric("Average Severity", round(filtered_df["Severity"].mean(), 2))

    st.subheader("Incidents Chart")
    chart = alt.Chart(filtered_df).mark_bar().encode(
        x="Threat Type",
        y="Incidents",
        color="Threat Type"
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
