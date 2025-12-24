import time
import platform

# Platform-specific imports
if platform.system() == "Windows":
    import win32gui
    import win32process
    import psutil


def get_active_window_title():
    """
    Returns the title of the currently active window (Windows).
    """
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid)
    return process.name()


def start_window_tracker(log_buffer, lock, interval=5):
    """
    Tracks changes in the active window at fixed intervals.
    """
    last_window = None

    while True:
        try:
            current_window = get_active_window_title()
            if current_window != last_window:
                with lock:
                    log_buffer.append(
                        f"[{time.ctime()}] Active window changed to: {current_window}"
                    )
                last_window = current_window
        except Exception:
            pass

        time.sleep(interval)
