import time
import smtplib
from email.mime.text import MIMEText
from config import (
    EMAIL_INTERVAL,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
    SMTP_SERVER,
    SMTP_PORT,
)

def start_email_scheduler(log_buffer, lock):
    """
    Sends activity logs via email at fixed intervals.
    """
    while True:
        time.sleep(EMAIL_INTERVAL)

        with lock:
            if not log_buffer:
                continue
            content = "\n".join(log_buffer)
            log_buffer.clear()

        try:
            msg = MIMEText(content)
            msg["Subject"] = "Activity Logger Report"
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()

        except Exception:
            pass
