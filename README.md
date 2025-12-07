A Python-based local monitoring demo that captures keyboard events, periodic screenshots, and webcam images.
This project is built solely for cybersecurity learning, digital forensics awareness, and understanding how monitoring tools function internally.

  This tool is intended ONLY for use on your own machine for educational purposes.
Do NOT use it on any device you do not own or have explicit permission to test.

Features

Keystroke Logging
Records all key presses into a timestamped text file inside the logs/ directory.

Automated Screenshots
Captures the screen at a fixed interval (default: every 30 seconds) and saves them in the screenshots/ folder.

Webcam Image Capture
Captures webcam pictures at a fixed interval (default: every 60 seconds) and stores them in the webcam/ folder.

Threaded Execution
Screen capture and webcam capture run in the background using daemon threads.

Automatic Folder Creation
The script creates all required directories on startup:

logs/

screenshots/

webcam/
