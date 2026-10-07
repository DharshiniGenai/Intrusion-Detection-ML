import streamlit as st

st.title("Button Test")

st.write("If you can see this, the page is working.")

if st.button("TEST BUTTON"):
    st.success("BUTTON WORKS!")