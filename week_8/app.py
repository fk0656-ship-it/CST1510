import streamlit as st
from DATA.users import register_user, login_user
from DATA.incidents import insert_incident, fetch_all_incidents

st.set_page_config(page_title="Cyber Intelligence Platform", layout="wide")

# --------------------- LOGIN / REGISTER UI ---------------------
st.title("🔐 Cyber Intelligence Platform")

menu = ["Login", "Register", "Report Incident", "View Incidents"]
choice = st.sidebar.selectbox("Menu", menu)

# --------------------- REGISTER ---------------------
if choice == "Register":
    st.subheader("Create a new account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        msg = register_user(new_user, new_pass)
        st.success(msg)

# --------------------- LOGIN ---------------------
elif choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login_user(username, password)
        st.info(result)

# --------------------- REPORT INCIDENT ---------------------
elif choice == "Report Incident":
    st.subheader("📝 Report a Cyber Incident")

    date = st.date_input("Incident Date")
    type_ = st.selectbox("Incident Type", ["Malware", "DDoS", "Phishing", "Data Leak"])
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    description = st.text_area("Description")
    reported_by = st.text_input("Reported By (username)")

    if st.button("Submit Incident"):
        incident_id = insert_incident(str(date), type_, severity, description, reported_by)
        st.success(f"Incident submitted! ID: {incident_id}")

# --------------------- VIEW INCIDENTS ---------------------
elif choice == "View Incidents":
    st.subheader("📊 Cyber Incidents Database")

    df = fetch_all_incidents()
    st.dataframe(df)
