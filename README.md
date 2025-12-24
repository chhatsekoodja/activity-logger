# Activity Logger (Python)

A cross-platform Python activity logger that monitors **keyboard input**, **mouse clicks**, and **active window changes**, logs events in real time, and **emails logs periodically**. Built to demonstrate Python **threading**, **event handling**, and **secure configuration**.

⚠️ **Ethical use notice:** This project is intended **only for educational purposes** with **explicit user consent**. Do not deploy or use without permission.

## ✨ Features

🧵 **Multithreaded design** (concurrent input tracking & window tracking)
🖱️ Keyboard and mouse event logging
🪟 Active window tracking
📄 Real-time log file (`activity_log.txt`)
📧 Periodic email reporting via SMTP
🔐 Secure secrets using environment variables (`.env`)
🌍 Cross-platform (Windows / macOS / Linux)

## 🧱 Project Structure

activity-logger/
│
├── main.py              # Entry point; starts threads & graceful shutdown
├── input_logger.py      # Keyboard & mouse listeners
├── window_tracker.py    # Active window detection
├── email_sender.py      # SMTP email scheduler
├── config.py            # Configuration (loaded from .env)
├── example.env          # Environment variable template (safe to share)
├── .gitignore           # Prevents secrets & logs from being committed
└── README.md            # Project documentation


## ⚙️ Setup Instructions

### 1️⃣ Clone the repository


git clone https://github.com/<your-username>/activity-logger.git
cd activity-logger


### 2️⃣ Create a virtual environment (recommended)

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

### 3️⃣ Install dependencies

python -m pip install pynput psutil python-dotenv

### 4️⃣ Configure environment variables

Create a `.env` file (do **not** commit it):

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com

For Gmail, use an **App Password** (not your account password).

## ▶️ Running the Application

python main.py

* Logs are written to `activity_log.txt`
* Emails are sent at the interval defined in `config.py`
* Stop the logger with **Ctrl + C** (graceful shutdown)


## 🧠 How It Works

**Thread 1:** Listens for keyboard & mouse events using `pynput`
**Thread 2:** Tracks active window changes
**Thread 3:** Periodically emails logs using SMTP
Threads are coordinated via a shared stop flag for clean termination


## 🔐 Security & Best Practices

* No secrets hardcoded
* `.env` excluded via `.gitignore`
* `example.env` provided for safe sharing
* Runtime artifacts (`__pycache__`, logs) ignored


## 🧪 Testing Email Setup

A separate `email_test.py` script can be used to verify SMTP credentials before running the logger.

## 📌 Configuration

Edit `config.py` to change:

* `EMAIL_INTERVAL` (seconds)
* SMTP server/port (if not using Gmail)
* Log file name


## 🚀 Possible Enhancements

* Log rotation & compression
* Encrypted log storage
* CLI flags for configuration
* GUI consent prompt
* Database-backed logging


## 📄 License

This project is provided for **educational use only**.


## 🙌 Acknowledgements

Built as a systems & Python threading exercise with a focus on clean architecture and security best practices.
