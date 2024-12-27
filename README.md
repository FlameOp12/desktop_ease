# Gesture-Based Window Control

This project implements gesture-based control of your computer's windows using hand tracking and gesture recognition via a webcam. By utilizing MediaPipe for hand landmark detection and PyAutoGUI for automating keyboard shortcuts, the script allows users to interact with their system using intuitive hand gestures.

---

## Features

- **Swipe Right Gesture:** Switch to the next window (equivalent to Alt + Tab on Windows/Linux or Cmd + Tab on macOS).
- **Swipe Left Gesture:** Switch to the previous window (equivalent to Alt + Tab on Windows/Linux or Cmd + Tab on macOS).
- **Thumbs-Up Gesture:** Close the currently active window (Alt + F4 on Windows/Linux or Cmd + W on macOS).

---

## Prerequisites

Before running the script, ensure you have the following:

### Hardware
- A webcam for capturing gestures.

### Software
- Python 3.7 or later.
- Required Python libraries (installation steps provided below).
- Platform-specific dependencies:
  - **Windows:** Requires the `pypiwin32` library for window detection.
  - **macOS:** Requires the `pyobjc-framework-AppKit` library for active window detection.
  - **Linux:** Requires `xdotool` for window management.

---

## Installation

### Step 1: Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/yourusername/gesture-control.git
cd gesture-control
