import cv2

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

# Eye detector settings
eye_cascade = cv2.CascadeClassifier('C:\Demo\haar\haarcascade_eye.xml')

while True:
    # Camera frame
    ignore,  frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Eye detection 
    eyes = eye_cascade.detectMultiScale(frame_gray,1.02,5)
    for eye in eyes:
        x,y,w,h = eye
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        frame[y:y+h, x:x+w] = (255,0,0)
        #frame[y:y+h, x:x+w] = (0,255,0)
        #frame[y:y+h, x:x+w] = (0,0,255)
        #frame[y:y+h, x:x+w] = (0,0,0)

    
    cv2.imshow('CameraWin', frame)
    cv2.moveWindow('CameraWin',Xpos,Ypos)

    if cv2.waitKey(1) & 0xff== ord('q'):
        break

camera.release()