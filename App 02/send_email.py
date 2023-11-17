import smtplib, ssl
import os

def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465

    username = "chloe.s.a.page@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")

    receiver = "chloe.s.a.page@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)
