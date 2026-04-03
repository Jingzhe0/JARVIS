from sys import flags
import time
import cv2
import pyautogui as p


def AuthenticateFace():

    flag = 0

    # Local Binary Patterns Histograms
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('engine\\auth\\trainer\\trainer.yml')

    cascadePath = "engine\\auth\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    names = ['', 'Sarthak']

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:

        ret, img = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(gray[y:y + h, x:x + w])

            # Convert distance to confidence %
            confidence = 100 - accuracy

            # ✅ Apply threshold (30%)
            if confidence >= 30:
                name = names[id] if id < len(names) else "unknown"
                flag = 1
            else:
                name = "unknown"
                flag = 0

            confidence_text = f"{round(confidence)}%"

            cv2.putText(img, str(name), (x + 5, y - 5),
                        font, 1, (255, 255, 255), 2)
            cv2.putText(img, confidence_text, (x + 5, y + h - 5),
                        font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

        if flag == 1:
            break

    cam.release()
    cv2.destroyAllWindows()

    return flag