import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

LOG_FILE = "activity_log.txt"
EMAIL_INTERVAL = 60  # seconds

