import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Function to calculate the distance between two points
def calculate_distance(point1, point2, img_width, img_height):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5 * img_width

# Function to check if hand is in a fist gesture
def is_fist(hand_landmarks, img_width, img_height):
    tips = [hand_landmarks.landmark[i] for i in [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]]
    for tip in tips:
        distance_to_wrist = calculate_distance(tip, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST], img_width, img_height)
        if distance_to_wrist > 50:  # Adjust this threshold as needed
            return False
    return True

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a selfie-view display
    image = cv2.flip(image, 1)

    # Get image dimensions
    img_height, img_width, _ = image.shape

    # Convert the image from BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of thumb tip and index finger tip
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate the distance between thumb and index tip (for pinch gesture)
            distance = calculate_distance(thumb_tip, index_tip, img_width, img_height)

            # Check for gestures and control volume
            if is_fist(hand_landmarks, img_width, img_height):  # Fist gesture -> Mute/Unmute
                pyautogui.press("volumemute")
                cv2.putText(image, 'Fist Gesture: Muting', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            elif distance < 40:  # Pinch gesture -> Volume down
                pyautogui.press("volumedown")
                cv2.putText(image, 'Pinch Gesture: Volume Down', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                # Check if hand is open (open palm gesture)
                if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y:
                    pyautogui.press("volumeup")
                    cv2.putText(image, 'Open Palm Gesture: Volume Up', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image with hand landmarks
    cv2.imshow('Hand Gesture Volume Control', image)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
