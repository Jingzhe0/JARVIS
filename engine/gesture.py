import cv2
import mediapipe as mp
import pyautogui
import time

def start_gesture_control(mode=1):
    """
    mode = 1 → Mouse control
    mode = 2 → Keyboard control
    """

    screen_w, screen_h =    pyautogui.size()

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

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]

                # ===== MOUSE CONTROL =====
                if mode == 1:
                    index_finger = hand.landmark[8]
                    x = int(index_finger.x * screen_w)
                    y = int(index_finger.y * screen_h)
                    pyautogui.moveTo(x, y)

                    thumb = hand.landmark[4]
                    if abs(index_finger.x - thumb.x) < 0.03:
                        pyautogui.click()
                        time.sleep(0.3)

                # ===== KEYBOARD CONTROL =====
                else:
                    fingers = count_fingers(hand)
                    now = time.time()

                    if now - prev_action_time > 0.3:
                        if fingers == 1:
                            pyautogui.press("up")
                        elif fingers == 2:
                            pyautogui.press("down")
                        elif fingers == 3:
                            pyautogui.press("right")
                        elif fingers == 4:
                            pyautogui.press("left")
                        elif fingers == 5:
                            pyautogui.press("space")

                        prev_action_time = now

                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Jarvis Gesture Control", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()