import streamlit as st
import pandas
from send_email import send_email

# Load topic data from topics file
df = pandas.read_csv("topics.csv")

# Render form
st.header('Contact Us')

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox("Topic", df["topic"])
    raw_message = st.text_area("Your message")

    button = st.form_submit_button("Submit")
    if button:
        # Construct email message
        message = f"""\
Subject: New email from {user_email} regarding {user_topic}

From: {user_email}
Re: {user_topic}
{raw_message}
"""
        # Send email
        send_email(message)

        # Notify user
        st.info("Your email was sent successfully")