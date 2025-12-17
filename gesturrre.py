# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# # Screen size
# screen_w, screen_h = pyautogui.size()

# # MediaPipe setup
# mp_hands = mp.solutions.hands
# mp_draw = mp.solutions.drawing_utils

# #   Input
# hands_mode = int(input("Enter number of hands (1 or 2): "))

# cap = cv2.VideoCapture(0)

# # ===================== FINGER COUNT FUNCTION =====================
# def count_fingers(hand):
#     fingers = 0

#     # Finger tips (index, middle, ring, pinky)
#     tips = [8, 12, 16, 20]

#     # Threshold
#     if hand.landmark[4].x < hand.landmark[3].x:  # Thumb
#         fingers += 1

#     for tip in tips:
#         if hand.landmark[tip].y < hand.landmark[tip - 2].y:
#             fingers += 1

#     return fingers

# # ===================== HAND TRACKING =====================
# with mp_hands.Hands(
#         max_num_hands=hands_mode,
#         min_detection_confidence=0.8,
#         min_tracking_confidence=0.7) as hands:

#     prev_action_time = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame = cv2.flip(frame, 1)
#         h, w, _ = frame.shape

#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(rgb)

#         if results.multi_hand_landmarks:

#             # ================== TWO HANDS → KEYBOARD ==================
#             if hands_mode == 2:
#                 hand = results.multi_hand_landmarks[0]
#                 fingers = count_fingers(hand)

#                 current_time = time.time()
#                 if current_time - prev_action_time > 0.3:

#                     if fingers == 1:
#                         pyautogui.press("up")

#                     elif fingers == 2:
#                         pyautogui.press("down")

#                     elif fingers == 3:
#                         pyautogui.press("right")

#                     elif fingers == 4:
#                         pyautogui.press("left")

#                     elif fingers == 5:
#                         pyautogui.press("space")

#                     prev_action_time = current_time

#                 mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

#             # ================== ONE HAND → MOUSE ==================
#             elif hands_mode == 1:
#                 hand = results.multi_hand_landmarks[0]

#                 # Index finger tip
#                 index_finger = hand.landmark[8]

#                 x = int(index_finger.x * screen_w)
#                 y = int(index_finger.y * screen_h)

#                 pyautogui.moveTo(x, y)

#                 # Optional click (thumb + index close)
#                 thumb_tip = hand.landmark[4]
#                 if abs(index_finger.x - thumb_tip.x) < 0.03:
#                     pyautogui.click()
#                     time.sleep(0.3)

#                 mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

#         cv2.imshow("Hand Control System", frame)

#         if cv2.waitKey(1) & 0xFF == 27:
#             break

# cap.release()
# cv2.destroyAllWindows()




# engine/gesture.py




start_gesture_control()