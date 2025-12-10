import streamlit as st

def show_widgets():
    st.title("🧩 Interactive Widgets Page")

    st.write("Try out the improved widgets below.")

    # ----- TEXT INPUT -----
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! 👋")

    st.markdown("---")

    # ----- BUTTON -----
    if st.button("Click for a Message"):
        st.info("You clicked the button!")

    st.markdown("---")

    # ----- SLIDER -----
    age = st.slider("Select your age", 0, 100, 20)
    st.write("Your age:", age)

    st.markdown("---")

    # ----- RADIO -----
    choice = st.radio("Choose your plan:", ["Basic", "Premium", "Ultimate"])
    st.write(f"Plan selected: **{choice}**")

    st.markdown("---")

    # ----- SELECTBOX -----
    country = st.selectbox("Select your country:", ["UAE", "UK", "USA", "India"])
    st.write(f"You selected: {country}")
