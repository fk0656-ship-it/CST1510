import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_cybersecurity():
    st.title("🛡 Cybersecurity Dashboard")
    st.write("Track threats, incidents, and severity interactively!")

    # Sample cybersecurity data
    threats = ["Malware", "Phishing", "Ransomware", "DDoS"]
    df = pd.DataFrame({
        "Threat Type": np.random.choice(threats, 100),
        "Incidents": np.random.randint(1, 50, 100),
        "Severity": np.random.randint(1, 10, 100)
    })

    selected_threat = st.sidebar.selectbox("Select Threat Type", df["Threat Type"].unique())
    filtered_df = df[df["Threat Type"] == selected_threat]

    # Buttons for interactivity
    col1, col2, col3 = st.columns(3)

    if col1.button("Show Raw Data"):
        st.dataframe(filtered_df)

    if col2.button("Show Metrics"):
        col1m, col2m, col3m = st.columns(3)
        col1m.metric("Max Incidents", filtered_df["Incidents"].max())
        col2m.metric("Min Incidents", filtered_df["Incidents"].min())
        col3m.metric("Average Severity", round(filtered_df["Severity"].mean(), 2))

    if col3.button("Show Chart"):
        chart = alt.Chart(filtered_df).mark_bar().encode(
            x='Severity:O',
            y='Incidents',
            color='Severity:O'
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

    # Optional alert
    max_incidents = filtered_df["Incidents"].max()
    if max_incidents > 40:
        st.warning(f"⚠️ High number of incidents for {selected_threat}!")
    elif max_incidents > 20:
        st.info(f"ℹ️ Moderate incidents for {selected_threat}.")
    else:
        st.success(f"✅ Low incidents for {selected_threat}.")
