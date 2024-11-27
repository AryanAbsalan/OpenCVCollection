import cv2

def cameraSettings(w,h):
    # Size of the screen
    width = w
    height = h

    # camera settings
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv2.CAP_PROP_FPS, 30)
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    return width,camera

width,camera = cameraSettings(640,360)

def onMouseclick(event,x,y,flags,params):
    global e 
    global firstPoint
    global secondPoint 

    # left button down event 1
    if event == cv2.EVENT_LBUTTONDOWN:
        e = event
        firstPoint = (x,y)
    # left button up event 4
    if event == cv2.EVENT_LBUTTONUP:
        e = event
        secondPoint = (x,y)
    # right button up event 5
    if event == cv2.EVENT_RBUTTONUP:
        e = event

cv2.namedWindow('Demo11')
cv2.setMouseCallback('Demo11',onMouseclick)
e = 0

while True:
    ignore,  frame = camera.read()

    # clickdown or clickup event
    # if e == 1:
        # cv2.circle(frame,firstPoint,25,(0,0,255),2)
    if e == 4:
       cv2.rectangle(frame, firstPoint, secondPoint, (0,0,255), 2)
       # creating region of interest frame
       frameROI = frame[firstPoint[1]:secondPoint[1], firstPoint[0]:secondPoint[0]]
       cv2.imshow('frameROI', frameROI)
       cv2.moveWindow('frameROI', int(width*1.1), 0)
    
    # rightclick event
    if e == 5:
        cv2.destroyWindow('frameROI')
        e = 0
    
    cv2.imshow('Demo10', frame)
    cv2.moveWindow('Demo10',0,0)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()