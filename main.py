import audioCommands
import time
import facial
import cv2

# aud = audioCommands.Recog()


video_capture = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("data/cacades/haarcascade_frontalface_default.xml")

i = 0
name = ""
set = (0,0,0,0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    cv2.imshow('Video', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    if i % 10 == 0:
        for (x,y,w,h) in faces:
            a = frame[y:y+h, x:x+w]
            name = facial.identifyFace(a)
            set = (x,y,w,h)

    if name == "carson":
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        y = y - 15 if y - 15 > 15 else y + 15
        cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    i = i + 1

    cv2.imshow('Modified', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

# https://medium.com/@stepanfilonov/tracking-your-eyes-with-python-3952e66194a6