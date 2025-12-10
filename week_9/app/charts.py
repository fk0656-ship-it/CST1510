import streamlit as st
import pandas as pd
import altair as alt

def show_charts():
    st.title("📊 Data Visualisation Dashboard")

    st.write("This page demonstrates improved charts with cleaner visuals.")

    # ----- BAR CHART -----
    df_bar = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Value": [12, 25, 8, 19]
    })

    st.subheader("Bar Chart: Category Performance")

    bar_chart = (
        alt.Chart(df_bar)
        .mark_bar()
        .encode(
            x=alt.X("Category", sort=None),
            y="Value",
            tooltip=["Category", "Value"]
        )
        .properties(height=350)
    )

    st.altair_chart(bar_chart, use_container_width=True)

    # ----- LINE CHART -----
    df_line = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [100, 150, 130, 170, 190]
    })

    st.subheader("📈 Line Chart: Monthly Sales Trend")

    line_chart = (
        alt.Chart(df_line)
        .mark_line(point=True)
        .encode(
            x="Month",
            y="Sales",
            tooltip=["Month", "Sales"]
        )
        .properties(height=350)
    )

    st.altair_chart(line_chart, use_container_width=True)
