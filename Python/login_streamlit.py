# login_streamlit

import streamlit as st

st.title("Login Portal")

correct_password = "10"
max_attempts = 5

# Use session state to keep track of attempts and lock status
if "attempt" not in st.session_state:
    st.session_state.attempt = 0
if "locked" not in st.session_state:
    st.session_state.locked = False

if st.session_state.locked:
    st.error("The portal has locked. Try again after a few minutes.")
else:
    password = st.text_input("Enter the password:", type="password")
    if st.button("Login"):
        if password == correct_password:
            st.success("Login Successfully, Welcome!")
        else:
            st.session_state.attempt += 1
            st.warning("The pin is incorrect. Try again.")
            if st.session_state.attempt >= max_attempts:
                st.session_state.locked = True
                st.error("The portal has locked. Try again after a few minutes.")         