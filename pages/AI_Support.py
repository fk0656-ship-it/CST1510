import streamlit as st
from google import genai


def userGeminiAPI(queryText):
    # FIXED: replaced curly quotes with normal quotes
    client = genai.Client(api_key="AIzaSyDu62CzQy1t1Yr2w63qpOq_n2OpyWnZmVs")

    # FIXED: correct call to generate content
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=queryText
    )
    return response


# Streamlit UI
st.title("Gemini AI Support")

# Initialize chat history
if "message" not in st.session_state:
    st.session_state.message = []
if "response" not in st.session_state:
    st.session_state.response = []


# Display previous chat messages
for user_msg, bot_msg in zip(st.session_state.message, st.session_state.response):
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)


# Chat input
prompt = st.chat_input("Hello, please type your query here!")

if prompt:
    # Store user message
    st.session_state.message.append(prompt)

    # Call Gemini API
    ai_response = userGeminiAPI(prompt)

    # Extract response text correctly
    try:
        reply_text = ai_response.text
    except:
        reply_text = "⚠️ Unable to read AI response format."

    st.session_state.response.append(reply_text)

    # Display live
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(reply_text)


# OPTIONAL: Button to print history in terminal
if st.button("Copy the response"):
    print(st.session_state.response)
