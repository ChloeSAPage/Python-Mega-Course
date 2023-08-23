import streamlit as st
from send_email import send_email
import pandas

topics = pandas.read_csv("topics.csv")

with st.form(key="email"):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you wish to discuss",
                         topics["topic"])
    text_box = st.text_area("Enter your message")
    message = f"""
    Subject: New email from company website
    From: {user_email}
    Topic: {topic}
    {text_box}"""
    
    button = st.form_submit_button("Submit")
    
    if button:
        send_email(message)
        st.info("Your email has been sent")