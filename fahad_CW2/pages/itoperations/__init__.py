import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_itoperations():
    st.title("🖥 IT Operations: Helpdesk Ticket Analysis")
    st.write("""
    Discover which staff or steps are slowing down helpdesk ticket resolution.
    Use buttons to explore the data and metrics interactively.
    """)

    # --- Sample Helpdesk Data ---
    staff = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    steps = ["Submit Ticket", "Assign Staff", "Resolve Issue", "Follow-up"]
    np.random.seed(42)

    df = pd.DataFrame({
        "Ticket ID": range(1, 101),
        "Staff": np.random.choice(staff, 100),
        "Step": np.random.choice(steps, 100),
        "Time Taken (hours)": np.random.randint(1, 72, 100)  # simulate ticket resolution time
    })

    st.subheader("Preview Helpdesk Tickets")
    st.dataframe(df.head(10))

    # --- Buttons for Interactivity ---
    col1, col2, col3 = st.columns(3)

    if col1.button("Show Raw Data"):
        st.write(df)

    if col2.button("Staff Performance Metrics"):
        st.write("Average Time Taken per Staff:")
        staff_metrics = df.groupby("Staff")["Time Taken (hours)"].mean().reset_index()
        st.dataframe(staff_metrics)

    if col3.button("Step Analysis"):
        st.write("Average Time Taken per Step:")
        step_metrics = df.groupby("Step")["Time Taken (hours)"].mean().reset_index()
        st.dataframe(step_metrics)

    # --- Visual Charts ---
    st.subheader("Visualize Staff Performance")
    staff_chart = alt.Chart(df.groupby("Staff")["Time Taken (hours)"].mean().reset_index()).mark_bar().encode(
        x='Staff',
        y='Time Taken (hours)',
        color='Staff'
    ).interactive()
    st.altair_chart(staff_chart, use_container_width=True)

    st.subheader("Visualize Step Duration")
    step_chart = alt.Chart(df.groupby("Step")["Time Taken (hours)"].mean().reset_index()).mark_bar(color='orange').encode(
        x='Step',
        y='Time Taken (hours)',
        tooltip=['Step', 'Time Taken (hours)']
    ).interactive()
    st.altair_chart(step_chart, use_container_width=True)

    # --- Optional: Identify bottleneck ---
    slowest_staff = df.groupby("Staff")["Time Taken (hours)"].mean().idxmax()
    slowest_step = df.groupby("Step")["Time Taken (hours)"].mean().idxmax()

    st.info(f"⚠️ Staff causing most delays: {slowest_staff}")
    st.info(f"⚠️ Step taking the longest time: {slowest_step}")
