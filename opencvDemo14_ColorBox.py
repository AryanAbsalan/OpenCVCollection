import cv2
import numpy as np

# Size of the screen
width = 640
height = 360

# camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

e = 0            # Default value for event
x = 0            # Default value for x
y = 0            # Default value for y

def onMouseClick(event, xVal , yVal , flags, params):
    global e 
    global x 
    global y 

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        e = event
        x = xVal
        y = yVal
    if event == cv2.EVENT_RBUTTONUP:
        print(event)
        e = event
        x = xVal
        y = yVal

cv2.namedWindow('Demo14')
cv2.setMouseCallback('Demo14',onMouseClick)

cv2.namedWindow('ColorBoxWin')
cv2.resizeWindow('ColorBoxWin',width=200,height=150)

while True:
    ignore,  frame = camera.read()

    # LBUTTONDOWN
    if e == 1:
        colorFrame = np.zeros([256,256,3],dtype=np.uint8) 
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        currentHSVColor = frameHSV[y][x]

        colorFrame[:,:]= currentHSVColor
        cv2.putText(colorFrame,str(currentHSVColor),(0,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('ColorBoxWin',colorFrame)
        cv2.moveWindow('ColorBoxWin',width,0)
        e = 0

    # RBUTTONUP
    if e == 5:
        cv2.destroyWindow('ColorBoxWin')
        e = 0

    cv2.imshow('Demo14', frame)

    # Using global x and y from Trackbar
    cv2.moveWindow('Demo14',0,0)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()