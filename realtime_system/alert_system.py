import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender = "marpol.alerts@gmail.com"
    receiver = "authority@port.gov"
    password = "your_app_password"
    msg = MIMEText(message)
    msg["Subject"] = "⚠️ MARPOL Violation Detected"
    msg["From"] = sender
    msg["To"] = receiver
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
    print("📧 Alert email sent successfully!")
