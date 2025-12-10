from services.user_service import register_user, login_user
# Import your modules from the data package
try:
    from data.users import register_user, login_user
except ModuleNotFoundError:
    st.error("Could not find data modules. Make sure the data folder is next to app.py and lowercase.")

st.title("Week 8 CST1510 Streamlit App")

# --- User Section ---
st.header("User Registration & Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Register"):
    try:
        msg = register_user(username, password)
        st.success(msg)
    except Exception as e:
        st.error(f"Error in register_user: {e}")

if st.button("Login"):
    try:
        msg = login_user(username, password)
        st.info(msg)
    except Exception as e:
        st.error(f"Error in login_user: {e}")
