import streamlit as st

# Sample user database
USERS = {
    "fahad": "mypassword",
    "user1": "pass1",
    "user2": "pass2"
}

def show_login():
    st.title("🔐 Login Page")
    st.write("Enter your username and password to access the CW2 dashboard.")

    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""

    if not st.session_state.logged_in:
        # User input fields
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        show_pass = st.checkbox("Show password")
        if show_pass:
            password = st.text_input("Password (visible)", value=password)

        # Login button
        if st.button("Login"):
            if username in USERS and USERS[username] == password:
                st.success(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("❌ Invalid username or password. Try again.")

    else:
        st.info(f"You're already logged in as **{st.session_state.username}**.")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()
