import cv2
import numpy as np
import mediapipe as mp
import time
import pyautogui  # NEW: for full screen capture

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

canvas = None
prev_x, prev_y = 0, 0
brush_color = (255, 0, 255)
brush_thickness = 5
eraser_thickness = 30
last_save_time = 0

def fingers_up(hand):
    tips = [8, 12, 16, 20]
    fingers = []
    fingers.append(hand.landmark[4].x < hand.landmark[3].x)
    for tip in tips:
        fingers.append(1 if hand.landmark[tip].y < hand.landmark[tip-2].y else 0)
    return fingers

cap = cv2.VideoCapture(0)
exit_air_write = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            lm = hand.landmark
            x = int(lm[8].x * w)
            y = int(lm[8].y * h)

            fingers = fingers_up(hand)

            # 1 finger → draw
            if fingers[1] == 1 and fingers[2] == 0:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y
                cv2.line(canvas, (prev_x, prev_y), (x, y), brush_color, brush_thickness)
                prev_x, prev_y = x, y

            # 2 fingers → erase
            elif fingers[1] == 1 and fingers[2] == 1 and not (fingers[3] == 1 and fingers[4] == 1):
                cv2.circle(canvas, (x, y), eraser_thickness, (0,0,0), -1)
                prev_x, prev_y = 0, 0

            # 5 fingers → exit air writing mode
            elif sum(fingers) == 5:
                print("5 fingers detected: exiting Air Writing mode")
                exit_air_write = True
                break

            # 4 fingers → save full screen screenshot
            elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                if time.time() - last_save_time > 2:
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.png")
                    print("Saved full screen screenshot!")
                    last_save_time = time.time()
                prev_x, prev_y = 0, 0

            else:
                prev_x, prev_y = 0, 0

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        if exit_air_write:
            break

    # Merge canvas with camera frame
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("Air Writing", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Close if window close button (X) is clicked
    if cv2.getWindowProperty("Air Writing", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()