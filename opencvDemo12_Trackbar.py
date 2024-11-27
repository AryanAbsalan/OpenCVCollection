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

def onChangeR(value):
    global r
    r = value

def onChangeT(value):
    global t
    t = value
    
def onChangeBlue(value):
    global blue
    blue = value

def onChangeGreen(value):
    global green
    green = value

def onChangeRed(value):
    global red
    red = value

cv2.namedWindow('TrackbarWindow')
cv2.moveWindow('TrackbarWindow',width,0)
cv2.resizeWindow('TrackbarWindow',width,height)

cv2.createTrackbar('X','TrackbarWindow',0,width,onChangeX)
cv2.createTrackbar('Y','TrackbarWindow',0,height,onChangeY)
cv2.createTrackbar('Radius','TrackbarWindow',0,height,onChangeR)
cv2.createTrackbar('Thickness','TrackbarWindow',0,10,onChangeT)
cv2.createTrackbar('Blue','TrackbarWindow',0,255,onChangeBlue)
cv2.createTrackbar('Green','TrackbarWindow',0,255,onChangeGreen)
cv2.createTrackbar('Red','TrackbarWindow',0,255,onChangeRed)

x = int(width/2)     # Default value for x
y = int(height/2)    # Default value for y
r = 25               # Default value for radius
t = 2                # Default value for thickness
blue = 0             # Default value for blue color
green = 0            # Default value for green color
red = 0              # Default value for red color

while True:
    ignore,  frame = camera.read()

    # cv2.circle(frame,(x,y),r,(blue,green,red),t)
    # cv2.rectangle(frame, (x, y), (int(x *0.12), int(y *0.07)), (blue, green, red), t)
    cv2.rectangle(frame, (x, y), (x + 150, y + 100), (blue, green, red), t)

    cv2.imshow('Demo12', frame)
    cv2.moveWindow('Demo12',0,0)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()