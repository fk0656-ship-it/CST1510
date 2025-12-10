import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_datascience():
    st.title("Data Science Page")
    st.write("Interactive Data Science Dashboard")

    st.sidebar.header("Settings")
    n_rows = st.sidebar.slider("Rows to show", 5, 50, 10)

    df = pd.DataFrame({
        "Feature": np.random.choice(["Age", "Salary", "Experience", "Score"], 100),
        "Value": np.random.randint(1, 100, 100),
        "Importance": np.random.rand(100)
    })

    st.subheader("Feature Data")
    st.dataframe(df.head(n_rows))

    chart = alt.Chart(df.head(n_rows)).mark_circle(size=100).encode(
        x='Feature',
        y='Value',
        color='Feature',
        tooltip=['Feature', 'Value', 'Importance']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    selected_feature = st.sidebar.selectbox("Select Feature", df['Feature'].unique())
    filtered_df = df[df['Feature'] == selected_feature]

    st.subheader(f"Filtered: {selected_feature}")
    st.dataframe(filtered_df)

    col1, col2 = st.columns(2)
    col1.metric("Max Value", filtered_df['Value'].max())
    col2.metric("Avg Importance", round(filtered_df['Importance'].mean(), 2))
