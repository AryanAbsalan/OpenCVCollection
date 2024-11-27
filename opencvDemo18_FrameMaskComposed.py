import cv2
import numpy as np

# Size of the screen
width = 400
height = 210

# camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

hue_low1 = 10             # Default value for Hue Low 1
hue_high1 = 20            # Default value for Hue High 1
hue_low2 = 10             # Default value for Hue Low 2
hue_high2 = 170           # Default value for Hue High 2
saturation_low = 10       # Default value for Saturation Low
saturation_high = 250     # Default value for Saturation High
value_low = 10            # Default value for Value Low
value_high = 250          # Default value for Value High
Xpos = 0                  # Default value for x position of frame window
Ypos = 0                  # Default value for y position of frame window

def onChange_hue_low1(value:int) -> None:
    global hue_low1
    hue_low1 = value
    print(hue_low1)

def onChange_hue_high1(value:int) -> None:
    global hue_high1
    hue_high1 = value
    print(hue_high1)

def onChange_hue_low2(value:int) -> None:
    global hue_low2
    hue_low2 = value
    print(hue_low2)

def onChange_hue_high2(value:int) -> None:
    global hue_high2
    hue_high2 = value
    print(hue_high2)

def onChange_saturation_low (value:int) -> None:
    global saturation_low
    saturation_low = value
    print(saturation_low)

def onChange_saturation_high (value:int) -> None:
    global saturation_high
    saturation_high = value
    print(saturation_high)

def onChange_value_low (value:int) -> None:
    global value_low
    value_low = value
    print(value_low)

def onChange_value_high (value:int) -> None:
    global value_high
    value_high= value
    print(value_high)

cv2.namedWindow('TrackbarWindow')
cv2.moveWindow('TrackbarWindow',width,0)
cv2.resizeWindow('TrackbarWindow',width,height+height)
# Hue Trackbars
cv2.createTrackbar('HueLow1','TrackbarWindow',10,179,onChange_hue_low1)
cv2.createTrackbar('HueHigh1','TrackbarWindow',20,179,onChange_hue_high1)
cv2.createTrackbar('HueLow2','TrackbarWindow',10,179,onChange_hue_low2)
cv2.createTrackbar('HueHigh2','TrackbarWindow',170,179,onChange_hue_high2)
# Saturation Trackbars
cv2.createTrackbar('SatLow','TrackbarWindow',10,255,onChange_saturation_low)
cv2.createTrackbar('SatHigh','TrackbarWindow',250,255,onChange_saturation_high)
# Value Trackbars
cv2.createTrackbar('ValueLow','TrackbarWindow',10,255,onChange_value_low)
cv2.createTrackbar('ValueHigh','TrackbarWindow',250,255,onChange_value_high)

while True:
    # Camera frame
    ignore,  frame = camera.read()
    cv2.imshow('CameraWin', frame)

    # First mask
    frame_hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bound1 = np.array([hue_low1, saturation_low, value_low])
    upper_bound1 = np.array([hue_high1, saturation_high, value_high])

    frame_mask1 = cv2.inRange(frame_hsv, lowerb=lower_bound1, upperb=upper_bound1)

    frame_mask1_small = cv2.resize(frame_mask1,(int(width/2),int(height/2)))
    cv2.imshow('MaskWin1', frame_mask1_small)
    cv2.moveWindow('MaskWin1',0,height+30)

    # Second mask
    lower_bound2 = np.array([hue_low2, saturation_low, value_low])
    upper_bound2 = np.array([hue_high2, saturation_high, value_high])

    frame_mask2 = cv2.inRange(frame_hsv, lowerb=lower_bound2, upperb=upper_bound2)

    frame_mask2_small = cv2.resize(frame_mask2,(int(width/2),int(height/2)))
    cv2.imshow('MaskWin2', frame_mask2_small)
    cv2.moveWindow('MaskWin2',int(width/2),height+30)

    # Tracking objects frame with a mask which is a combination of two masks
    frame_mask_composed = frame_mask1 | frame_mask2

    # Drawing contours
    contours, junk = cv2.findContours(frame_mask_composed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame,contours,-1,(255,0,0),3) # -1 draws all contours
    for contour in contours:
        area = cv2.contourArea(contour)
        if area>=800:
            #cv2.drawContours(frame,[contour],0,(255,0,0),3)
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            # x and y position for moving the frame
            Xpos = int(x/width*1920)
            Ypos = int(y/height*1080)
    
    # Addinng composed mask on frame
    object_tracked = cv2.bitwise_and(frame,frame,mask=frame_mask_composed)

    object_tracked_small = cv2.resize(object_tracked,(width,height))
    cv2.imshow('ObjectWin', object_tracked_small)
    cv2.moveWindow('ObjectWin',0,height+height)

    cv2.moveWindow('CameraWin',Xpos,Ypos)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()