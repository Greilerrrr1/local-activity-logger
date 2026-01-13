\# Local Activity Logger (Educational / Defensive Demo)



This repository contains a Python-based \*\*local monitoring demo\*\* intended for cybersecurity learning, digital forensics awareness, and understanding how endpoint monitoring components work internally.



It captures:

\- Keyboard events (logged to a local file)

\- Periodic screenshots

\- Periodic webcam images



\## Important Legal / Ethical Notice



This code must be used \*\*only\*\* on a machine you own \*\*or\*\* on systems where you have \*\*explicit written permission\*\* to test. Using any kind of monitoring or logging tool on devices you do not own (or without consent) may be illegal and unethical.



If you are using this for coursework or a lab, keep the work strictly inside a controlled environment (e.g., your own VM or test machine) and treat all collected output as sensitive.



---



\## What This Project Demonstrates (High Level)



This script is useful for understanding:

\- How keyboard event listeners work at the OS level (via `pynput`)

\- How periodic screen capture can be implemented (via `mss` + Pillow)

\- How to access a webcam stream and save frames (via OpenCV)

\- How to run concurrent tasks safely using threads

\- Basic file/folder organization for logging artifacts



---



\## How It Works (Code Overview)



When the script starts, it:

1\. Creates three local directories (if they do not exist):

&nbsp;  - `logs/` for keystroke output

&nbsp;  - `screenshots/` for screen captures

&nbsp;  - `webcam/` for camera images

2\. Starts two background threads:

&nbsp;  - \*\*Screen capture loop\*\* (default interval: 30 seconds)

&nbsp;  - \*\*Webcam capture loop\*\* (default interval: 60 seconds)

3\. Starts a keyboard listener on the main thread:

&nbsp;  - Appends readable keystrokes to `logs/keylog.txt`

4\. Shuts down cleanly when interrupted:

&nbsp;  - Sets a shared `running = False` flag to stop loops

&nbsp;  - Releases the webcam resource



---



\## Output Files and Locations



This project writes output under the project directory:



\- `logs/keylog.txt`

&nbsp; - Stores keyboard activity in a readable format

&nbsp; - Examples: spaces, new lines, `\[TAB]`, `\[BACKSPACE]`



\- `screenshots/screen\_YYYY-MM-DD\_HH-MM-SS.png`

&nbsp; - Timestamped full-screen screenshots



\- `webcam/webcam\_YYYY-MM-DD\_HH-MM-SS.jpg`

&nbsp; - Timestamped webcam still images



\*\*Note:\*\* These artifacts can contain sensitive personal information. Handle carefully.



---



\## Configuration



You can adjust capture intervals by changing the thread arguments:



\- Screenshot capture interval is set here:

&nbsp; - `screen\_capture\_loop(interval=30)`



\- Webcam capture interval is set here:

&nbsp; - `webcam\_capture\_loop(interval=60)`



Intervals are in seconds.



---



\## Dependencies



This project uses:

\- Python 3.x

\- `pynput` (keyboard event listener)

\- `mss` (fast screen capture)

\- `Pillow` (image conversion/saving)

\- `opencv-python` (`cv2`) (webcam access + image writing)

\- `numpy` (dependency used by imaging stack / OpenCV workflows)



---



\## Recommended Repo Hygiene (Do NOT Upload Captured Data)



The folders `logs/`, `screenshots/`, and `webcam/` are generated output and typically should \*\*not\*\* be committed to GitHub.



Use a `.gitignore` like the following:



```gitignore

logs/

screenshots/

webcam/

\*.png

\*.jpg

\*.jpeg



