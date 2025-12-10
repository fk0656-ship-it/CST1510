import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_cybersecurity():
    st.title("🛡 Cybersecurity Dashboard")
    st.write("Track threats, incidents, and severity interactively!")

    # --- Sample Cybersecurity Data ---
    threats = ["Malware", "Phishing", "Ransomware", "DDoS"]
    df = pd.DataFrame({
        "Threat Type": np.random.choice(threats, 100),
        "Incidents": np.random.randint(1, 50, 100),
        "Severity": np.random.randint(1, 10, 100)
    })

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_threat = st.sidebar.selectbox("Select Threat Type", df["Threat Type"].unique())

    # Filtered data
    filtered_df = df[df["Threat Type"] == selected_threat]

    # --- Buttons for Interactivity ---
    st.subheader(f"Actions for {selected_threat}")
    col1, col2, col3 = st.columns(3)

    if col1.button("Show Raw Data"):
        st.write("Here’s the raw data for this threat:")
        st.dataframe(filtered_df)

    if col2.button("Show Metrics"):
        st.write("Metrics for this threat:")
        col1_metric, col2_metric, col3_metric = st.columns(3)
        col1_metric.metric("Max Incidents", filtered_df["Incidents"].max())
        col2_metric.metric("Min Incidents", filtered_df["Incidents"].min())
        col3_metric.metric("Average Severity", round(filtered_df["Severity"].mean(), 2))

    if col3.button("Show Chart"):
        st.write("Visualizing incidents by severity")
        chart = alt.Chart(filtered_df).mark_bar().encode(
            x="Severity:O",
            y="Incidents",
            color="Severity:O"
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

    # Optional: Fun alert message based on incidents
    max_incidents = filtered_df["Incidents"].max()
    if max_incidents > 40:
        st.warning(f"⚠️ High number of incidents detected for {selected_threat}!")
    elif max_incidents > 20:
        st.info(f"ℹ️ Moderate number of incidents for {selected_threat}.")
    else:
        st.success(f"✅ Low number of incidents for {selected_threat}.")
