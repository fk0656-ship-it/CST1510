import streamlit as st
import pandas as pd

def show_layout():
    st.title("🎨 Page Layout & UI Components")

    st.write("Below is an improved layout demonstrating modern UI blocks.")

    # ----- METRIC CARDS -----
    col1, col2, col3 = st.columns(3)

    col1.metric("Daily Visitors", 2450, "+12%")
    col2.metric("Active Users", 530, "+8%")
    col3.metric("Bounce Rate", "32%", "-4%")

    st.markdown("---")

    # ----- DATA TABLE -----
    st.subheader("Student Scores Table")

    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Score": [85, 90, 78, 92],
        "Status": ["Pass", "Pass", "Pass", "Pass"]
    })

    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # ----- BUTTONS & COLUMNS -----
    colA, colB = st.columns(2)

    with colA:
        st.success("This is left column")
        st.button("Left Button")

    with colB:
        st.info("This is right column")
        st.checkbox("Enable Option")
