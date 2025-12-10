import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_itoperations():
    st.title("🖥 IT Operations Dashboard")
    st.write("Analyze helpdesk tickets and discover bottlenecks.")

    staff = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    steps = ["Submit Ticket", "Assign Staff", "Resolve Issue", "Follow-up"]

    df = pd.DataFrame({
        "Ticket ID": range(1, 101),
        "Staff": np.random.choice(staff, 100),
        "Step": np.random.choice(steps, 100),
        "Time Taken": np.random.randint(1, 72, 100)
    })

    st.subheader("Sample Tickets")
    st.dataframe(df.head(10))

    # Buttons
    col1, col2, col3 = st.columns(3)
    if col1.button("Show Raw Data"):
        st.dataframe(df)
    if col2.button("Staff Metrics"):
        st.dataframe(df.groupby("Staff")["Time Taken"].mean().reset_index())
    if col3.button("Step Metrics"):
        st.dataframe(df.groupby("Step")["Time Taken"].mean().reset_index())

    # Charts
    staff_chart = alt.Chart(df.groupby("Staff")["Time Taken"].mean().reset_index()).mark_bar().encode(
        x='Staff',
        y='Time Taken',
        color='Staff'
    ).interactive()
    st.altair_chart(staff_chart, use_container_width=True)

    step_chart = alt.Chart(df.groupby("Step")["Time Taken"].mean().reset_index()).mark_bar(color='orange').encode(
        x='Step',
        y='Time Taken'
    ).interactive()
    st.altair_chart(step_chart, use_container_width=True)

    # Bottleneck alerts
    slowest_staff = df.groupby("Staff")["Time Taken"].mean().idxmax()
    slowest_step = df.groupby("Step")["Time Taken"].mean().idxmax()
    st.info(f"⚠️ Staff causing most delays: {slowest_staff}")
    st.info(f"⚠️ Step taking longest time: {slowest_step}")
