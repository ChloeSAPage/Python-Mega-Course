import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Contact Me", layout="wide")

st.title("Contact me!")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    message = f"""\
Subject: New email from Streamlit Portfolio
{user_message} 
from {user_email}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully")