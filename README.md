Gesture Control Application - README
Overview
This Python program uses computer vision and hand-tracking to implement gesture-based control for window navigation and management. It utilizes the MediaPipe library for hand gesture recognition, OpenCV for video capture and display, and PyAutoGUI for automating keyboard shortcuts.

Features
Swipe Gestures:
Swipe Right: Switch to the next application window.
Swipe Left: Switch to the previous application window.
Thumbs-Up Gesture:
Close the currently active application window.
Prerequisites
Python 3.7 or later
A webcam for video input
The following Python libraries:
opencv-python
mediapipe
pyautogui
Additional system-specific dependencies:
Windows: pywin32
macOS: pyobjc
Linux: xdotool (install via sudo apt-get install xdotool)
Installation
Clone the repository:
bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install dependencies:
bash
Copy code
pip install opencv-python mediapipe pyautogui
Install system-specific dependencies if required:
Windows: Install pywin32:
bash
Copy code
pip install pywin32
macOS: Install pyobjc:
bash
Copy code
pip install pyobjc
Linux: Install xdotool:
bash
Copy code
sudo apt-get install xdotool
Usage
Run the program:

bash
Copy code
python gesture_control.py
Ensure your webcam is active and facing your hand.

Perform gestures:

Swipe Right: Switch to the next window.
Swipe Left: Switch to the previous window.
Thumbs-Up: Close the active window.
Exit the program by pressing the q key.

How It Works
Hand Tracking: The program uses MediaPipe's Hands module to track hand landmarks in real-time.
Gesture Detection:
Swipe: Detected based on the horizontal movement of the wrist landmark.
Thumbs-Up: Detected when the thumb tip is positioned above the index finger MCP joint.
Window Management:
The program identifies the currently active window using platform-specific methods.
Executes system-specific keyboard shortcuts using PyAutoGUI to perform actions.
Customization
Restricted Windows: The program skips gesture controls for specified applications. Modify the restricted_windows list to add or remove application names:
python
Copy code
restricted_windows = ["Visual Studio Code", "Gesture Control"]
Gesture Sensitivity:
Adjust the swipe sensitivity by modifying the thresholds:
python
Copy code
if current_x - prev_x > 0.05:  # Swipe Right
Notes
The program may behave differently depending on the platform. Modify keyboard shortcuts (pyautogui.hotkey()) for macOS or Linux if necessary.
Ensure a clutter-free background for better hand-tracking performance.
The program currently supports one hand at a time.






