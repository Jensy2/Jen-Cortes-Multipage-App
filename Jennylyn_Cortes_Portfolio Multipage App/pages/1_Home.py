import streamlit as st

# Homepage Title
st.title("🏠 Welcome to My Homepage")

# Simple introduction
st.write("Hello! This is my simple Streamlit homepage.")

# Add a header
st.header("About")
st.write("This app is created using Streamlit.")

# Add a button
if st.button("Click Me"):
    st.success("You clicked the button!")

# Add a text input
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋")