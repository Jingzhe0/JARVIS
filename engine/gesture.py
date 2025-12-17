# engine/gesture.py
import cv2
import mediapipe as mp
import pyautogui
import time
from multiprocessing import Event

def gesture_controller(stop_event, mode=1):
    screen_w, screen_h = pyautogui.size()

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    def count_fingers(hand):
        fingers = 0
        tips = [8, 12, 16, 20]

        if hand.landmark[4].x < hand.landmark[3].x:
            fingers += 1

        for tip in tips:
            if hand.landmark[tip].y < hand.landmark[tip - 2].y:
                fingers += 1

        return fingers

    with mp_hands.Hands(
        max_num_hands=1 if mode == 1 else 2,
        min_detection_confidence=0.8,
        min_tracking_confidence=0.7
    ) as hands:

        prev_action_time = 0

        while not stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]

                # Mouse mode
                if mode == 1:
                    index = hand.landmark[8]
                    x = int(index.x * screen_w)
                    y = int(index.y * screen_h)
                    pyautogui.moveTo(x, y)

                # Keyboard mode
                else:
                    fingers = count_fingers(hand)
                    now = time.time()
                    if now - prev_action_time > 0.3:
                        keys = {1: "up", 2: "down", 3: "right", 4: "left", 5: "space"}
                        if fingers in keys:
                            pyautogui.press(keys[fingers])
                        prev_action_time = now

                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Jarvis Gesture Control", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
