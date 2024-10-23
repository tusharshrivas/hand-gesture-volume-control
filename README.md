This project uses Python, OpenCV, and MediaPipe to control system volume through hand gestures captured by a webcam. It detects gestures such as a fist (for mute/unmute), pinch (for volume down), and open palm (for volume up).

Features
Fist Gesture: Mutes or unmutes the system volume.
Pinch Gesture: Decreases the system volume.
Open Palm Gesture: Increases the system volume.
Requirements
Python 3.x
OpenCV
MediaPipe
PyAutoGUI
Install Dependencies
To install the required Python libraries, run:
pip install opencv-python mediapipe pyautogui
Control system volume using hand gestures:

Fist Gesture: Mute or unmute the volume.
Pinch Gesture: Lower the volume.
Open Palm Gesture: Raise the volume.
Exit the program:

Press 'q' to exit the program and stop the webcam feed.

How It Works

The script captures video from your webcam and processes the video stream using OpenCV.
MediaPipe is used to detect hand landmarks in real-time. Specific hand landmarks (such as thumb and index finger tips) are tracked to recognize gestures.
The system volume is controlled by simulating keypress events with PyAutoGUI based on the detected gestures:
Fist: All finger tips are close to the wrist, indicating a mute/unmute action.
Pinch: Thumb and index finger tips are close together, indicating a volume down action.
Open Palm: All fingers are extended and separated, indicating a volume up action.
