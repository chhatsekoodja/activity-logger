import smtplib
from email.mime.text import MIMEText

EMAIL_SENDER = "unnati.singhal2025@vitstudent.ac.in"
EMAIL_PASSWORD = "iopo liuf eaae allb"
EMAIL_RECEIVER = "unnati.singhal2025@vitstudent.ac.in"

# Create a simple plain text message
msg = MIMEText("This is a test email from Python.")
msg['Subject'] = "Test Email - Activity Logger"
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_RECEIVER

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.set_debuglevel(1)  # Prints SMTP conversation
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Test email sent successfully!")
except Exception as e:
    print(f"Failed to send test email: {repr(e)}")
