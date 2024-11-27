import cv2
import numpy as np

# Size of the screen
width = 640
height = 340

# Camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

Xpos = 0                  # Default value for x position of frame window
Ypos = 0                  # Default value for y position of frame window

# Face and eye detector settings
face_cascade = cv2.CascadeClassifier(
    'C:\Demo\haar\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\Demo\haar\haarcascade_eye.xml')

while True:
    # Camera frame
    ignore,  frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(frame_gray, 1.02, 5)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Eye detection
        roi_gray = frame_gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Converting eye roi to GRAY and to BGR to sett the demention of array
            roi_color_gray_eye = cv2.cvtColor(
                roi_color[ey:ey+eh, ex:ex+ew], cv2.COLOR_BGR2GRAY)
            roi_color[ey:ey+eh, ex:ex +
                      ew] = cv2.cvtColor(roi_color_gray_eye, cv2.COLOR_GRAY2BGR)

            #roi_color[ey:ey+eh, ex:ex+ew] = (255,0,0)
            #roi_color[ey:ey+eh, ex:ex+ew] = (0,255,0)
            #roi_color[ey:ey+eh, ex:ex+ew] = (0,0,255)
            #roi_color[ey:ey+eh, ex:ex+ew] = (0,0,0)

    cv2.imshow('CameraWin', frame)
    cv2.moveWindow('CameraWin', Xpos, Ypos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
