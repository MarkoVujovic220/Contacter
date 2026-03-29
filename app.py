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
        sender = "oltenweb@gmail.com"
        receiver = "oltenweb@gmail.com"
        password = "gwldbkignvdibssr" #os.getenv("EMAIL_PASSWORD")

        message = "Subject: Test Email\n\nThis is a test email from your app 🚀"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message)

        return {"status": "email sent"}

    except smtplib.SMTPAuthenticationError as auth_err:
        # Gmail login failed
        print("SMTPAuthenticationError:", auth_err)
        return {"error": "Authentication failed. Check App Password", "details": str(auth_err)}

    except smtplib.SMTPConnectError as conn_err:
        # Connection to Gmail failed
        print("SMTPConnectError:", conn_err)
        return {"error": "Connection to SMTP server failed", "details": str(conn_err)}

    except Exception as e:
        # Catch all other errors
        print("Other error:", e)
        return {"error": "Something went wrong", "details": str(e)}
