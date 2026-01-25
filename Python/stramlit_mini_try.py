import streamlit as st

st.title("Tiny Demo")
name = st.text_input("Name")
qty = st.number_input("Qty", min_value=1, value=1)
if st.button("Add"):
    st.success(f"Added {qty} x {name}")
