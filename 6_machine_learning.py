import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
mpDrawing = mp.solutions.drawing_utils

tracker = mpHands.Hands(
    max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5
)

cam = cv2.VideoCapture(2)

while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results = tracker.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDrawing.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hands!", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
