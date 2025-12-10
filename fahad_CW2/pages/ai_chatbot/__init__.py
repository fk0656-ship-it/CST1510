import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_ai_chat():
    st.title("AI Chatbot Page")
    st.write("Interactive AI Chatbot Dashboard")

    st.sidebar.header("Settings")
    n_rows = st.sidebar.slider("Number of messages to simulate", 5, 50, 10)

    df = pd.DataFrame({
        "User": np.random.choice(["Alice", "Bob", "Charlie"], 100),
        "Message Length": np.random.randint(1, 200, 100),
        "Sentiment": np.random.choice(["Positive", "Neutral", "Negative"], 100)
    })

    st.subheader("Chat Message Data")
    st.dataframe(df.head(n_rows))

    chart = alt.Chart(df.head(n_rows)).mark_bar().encode(
        x='User',
        y='Message Length',
        color='Sentiment'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    selected_user = st.sidebar.selectbox("Select User", df['User'].unique())
    filtered_df = df[df['User'] == selected_user]

    st.subheader(f"Filtered Messages: {selected_user}")
    st.dataframe(filtered_df)

    col1, col2 = st.columns(2)
    col1.metric("Max Message Length", filtered_df['Message Length'].max())
    col2.metric("Positive Sentiment Count", (filtered_df['Sentiment']=="Positive").sum())
