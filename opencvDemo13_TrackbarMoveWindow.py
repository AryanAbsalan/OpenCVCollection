import cv2

# Size of the screen
width = 640
height = 360

# camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

def onChangeX(value):
    global x
    x = value

def onChangeY(value):
    global y
    y = value

def onChangeW(value):
    width = value
    height = int(width*9/16)
    # Using global w and h from Trackbar
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


cv2.namedWindow('TrackbarWindow')
cv2.moveWindow('TrackbarWindow',width,0)
cv2.resizeWindow('TrackbarWindow',width,height)

cv2.createTrackbar('X','TrackbarWindow',0,width,onChangeX)
cv2.createTrackbar('Y','TrackbarWindow',0,height,onChangeY)
cv2.createTrackbar('Width','TrackbarWindow',width,(width*2),onChangeW)

x = 0            # Default value for x
y = 0            # Default value for y
w = width        # Default value for width
h = height       # Default value for height


while True:
    ignore,  frame = camera.read()
    cv2.imshow('Demo13', frame)

    # Using global x and y from Trackbar
    cv2.moveWindow('Demo13',x,y)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()