# Hand Gesture Volume Control

This project demonstrates a **Hand Gesture Volume Control** system using **Python**, **OpenCV**, and **MediaPipe**. The program uses a webcam to detect hand gestures and controls the system volume based on specific gestures like a fist, pinch, or open palm.

## Features

1. **Fist Gesture**: Toggles mute/unmute.
2. **Pinch Gesture**: Decreases the system volume.
3. **Open Palm Gesture**: Increases the system volume.

## Prerequisites

Before running the program, make sure to install the following dependencies:

- **Python 3.7 or above**
- **OpenCV**: For real-time image processing
  ```bash
  pip install opencv-python
  ```
- **MediaPipe**: For hand gesture detection
  ```bash
  pip install mediapipe
  ```
- **PyAutoGUI**: For controlling system volume
  ```bash
  pip install pyautogui
  ```

## Code Explanation

### **1. Import Libraries**
The required libraries are imported:
```python
import cv2
import mediapipe as mp
import pyautogui
```

### **2. Initialize MediaPipe Hands**
The MediaPipe Hands solution is used for hand detection and landmark tracking:
```python
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
```

### **3. Gesture Detection**
Two custom functions are defined:

- **`calculate_distance(point1, point2, img_width, img_height)`**: Calculates the Euclidean distance between two points in the image.
- **`is_fist(hand_landmarks, img_width, img_height)`**: Checks if the hand gesture resembles a fist by comparing distances from fingertips to the wrist.

### **4. Webcam Input**
The program captures frames from the webcam:
```python
cap = cv2.VideoCapture(0)
```

### **5. Gesture Recognition and Volume Control**
The program processes each frame to:

1. Detect hand landmarks.
2. Identify gestures (fist, pinch, open palm).
3. Trigger volume control actions using **PyAutoGUI**.

### **6. Display Output**
The hand landmarks and gesture information are displayed on the screen using OpenCV functions.


### **7. Exit Mechanism**
Press **'q'** to exit the program and release resources:
```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
```

## How to Run

1. Clone the repository or download the script.
2. Ensure all dependencies are installed (refer to the **Prerequisites** section).
3. Run the program:
   ```bash
   python hand_gesture_volume_control.py
   ```
4. Allow webcam access and make gestures like a fist, pinch, or open palm to control the volume.

## Gestures and Their Actions

| **Gesture**      | **Action**               |
|-------------------|--------------------------|
| Fist             | Toggle mute/unmute       |
| Pinch            | Decrease volume          |
| Open Palm        | Increase volume          |

## Important Notes

- **Threshold Adjustments**: Modify the distance thresholds in the code to fine-tune gesture recognition based on your setup.
- **System Compatibility**: The volume control functionality depends on the compatibility of **PyAutoGUI** with your operating system.
- **Lighting Conditions**: Ensure adequate lighting for accurate hand detection.

## Example Output

- **Fist Gesture**: The text "Fist Gesture: Muting" is displayed on the screen, and the system mutes or unmutes.
- **Pinch Gesture**: The text "Pinch Gesture: Volume Down" appears, and the system volume decreases.
- **Open Palm Gesture**: The text "Open Palm Gesture: Volume Up" is shown, and the system volume increases.

## License
This project is open-source and available for personal and educational use.

---

Enjoy controlling your system volume with just your hand gestures!
