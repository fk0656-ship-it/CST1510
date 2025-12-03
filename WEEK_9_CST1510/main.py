import streamlit as st
import importlib

st.set_page_config(page_title="Week 9 App", layout="wide")

# Keep login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ---------------- #
def login_page():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Enter both username and password")

# ---------------- APP PAGES ---------------- #
def run_app():
    st.sidebar.title("Navigation")

    page = st.sidebar.selectbox(
        "Go to:",
        ["Home", "Charts", "Layout", "Mini Dashboard", "Widgets", "Logout"]
    )

    if page == "Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()

    module_map = {
        "Charts": "app.charts",
        "Layout": "app.layout",
        "Mini Dashboard": "app.mini_dashboard",
        "Widgets": "app.widget"
    }

    st.title(f"📄 {page}")

    if page == "Home":
        st.write("🏠 **Welcome to Week 9 Streamlit App!**")

    elif page in module_map:
        module = importlib.import_module(module_map[page])
        module.show()

# ---------------- RUN ---------------- #
if st.session_state.logged_in:
    run_app()
else:
    login_page()
# main.py snippet for sidebar
demo_mapping = {
    "Home": "app.home",
    "Charts": "app.charts",
    "Layout": "app.layout",
    "Mini Dashboard": "app.mini_dashboard",
    "Widgets": "app.widgets"
}

demo = st.sidebar.selectbox(
    "Choose a demo to run:",
    list(demo_mapping.keys())
)
