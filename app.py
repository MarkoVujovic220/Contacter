from fastapi import FastAPI
import smtplib
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/send")
def send_email():
    try:
        sender = "markovujovic522@gmail.com"
        receiver = "markovujovic522@gmail.com"
        password = os.getenv("EMAIL_PASSWORD")

        message = "Subject: Test Email\n\nThis is a test email from your app 🚀"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message)

        return {"status": "email sent"}

    except Exception as e:
        return {"error": str(e)}
