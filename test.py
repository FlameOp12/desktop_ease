import cv2
import mediapipe as mp
import pyautogui
import math
import platform
import subprocess

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Variables for gesture tracking
prev_x = None  # For swipe detection
gesture_start_time = None

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

def get_active_window():
    """Get the name of the active window."""
    system = platform.system()
    if system == "Windows":
        import win32gui
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    elif system == "Darwin":  # macOS
        from AppKit import NSWorkspace
        window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    else:
        window = subprocess.run(["xdotool", "getactivewindow", "getwindowname"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    return window.strip()

def is_restricted_window(active_window_name):
    """Check if the active window should be excluded."""
    restricted_windows = ["Visual Studio Code", "Gesture Control"]  # Add other restricted apps here
    return any(name in active_window_name for name in restricted_windows)

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and process the frame
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates for swipe detection
            current_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x

            # Swipe Gesture Detection
            if prev_x is not None:
                active_window = get_active_window()
                if not is_restricted_window(active_window):
                    if current_x - prev_x > 0.05:  # Swipe Right
                        print("Swipe Right - Next Window")
                        pyautogui.hotkey('alt', 'tab')  # Use 'cmd' for Mac
                    elif prev_x - current_x > 0.05:  # Swipe Left
                        print("Swipe Left - Previous Window")
                        pyautogui.hotkey('alt', 'tab')  # Use 'cmd' for Mac

            # Update previous x-coordinate
            prev_x = current_x

            # Detect Thumbs-Up for Closing Window
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

            # Check if the thumb is raised above the index MCP (thumbs up)
            if thumb_tip.y < index_mcp.y:  # Lower y means higher in the frame
                active_window = get_active_window()
                if not is_restricted_window(active_window):
                    print("Thumbs-Up detected - Closing Window")
                    pyautogui.hotkey('alt', 'f4')  # Use 'cmd', 'w' for Mac

    else:
        prev_x = None  # Reset swipe tracking if no hand detected

    # Display the frame
    cv2.imshow("Gesture Control", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
