import streamlit as st
import pandas as pd
import altair as alt

def show_mini_dashboard():
    st.title("📌 Mini Dashboard")

    st.write("A compact dashboard with KPIs and charts.")

    # ----- KPIs -----
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales", "$45,200")
    col2.metric("Total Users", "1,280")
    col3.metric("Conversion Rate", "4.8%")

    st.markdown("---")

    # ----- DATA & CHART -----
    df = pd.DataFrame({
        "Metric": ["Sales", "Profit", "Users"],
        "Value": [45200, 9800, 1280]
    })

    st.subheader("Overview Table")
    st.table(df)

    st.subheader("Bar Chart Overview")

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="Metric",
            y="Value",
            tooltip=["Metric", "Value"]
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)
