from pynput import keyboard, mouse
import time

def start_input_logger(log_buffer, lock):
    """
    Listens for keyboard and mouse events.
    Logs only the occurrence of events (not actual keys).
    """

    def on_key_press(key):
        entry = f"[{time.ctime()}] Keyboard event detected"
        with lock:
            log_buffer.append(entry)
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(entry + "\n")


    def on_mouse_click(x, y, button, pressed):
        if pressed:
            entry = f"[{time.ctime()}] Mouse click detected"
            with lock:
                log_buffer.append(entry)
            with open("logs.txt", "a", encoding="utf-8") as f:
                f.write(entry + "\n")


    keyboard.Listener(on_press=on_key_press).start()
    mouse.Listener(on_click=on_mouse_click).start()
