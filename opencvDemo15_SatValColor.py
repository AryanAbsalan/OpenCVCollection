import cv2
import numpy as np

# Size of the screen
# width = 640
# height = 360

# # camera settings
# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# camera.set(cv2.CAP_PROP_FPS, 30)
# camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))



cv2.namedWindow('SaturationColorBoxWin')
cv2.resizeWindow('SaturationColorBoxWin',width=720,height=256)

cv2.namedWindow('ValueColorBoxWin')
cv2.resizeWindow('ValueColorBoxWin',width=720,height=256)

while True:
   
    colorFrame = np.zeros([256,720,3],dtype=np.uint8)
    
    # Color windows for saturation
    for row in range(0,256):
        for column in range(0,720):
            # HSV 
            HSVColor = (int(column/4),row,255)
            colorFrame[row,column]= HSVColor

    colorFrame = cv2.cvtColor(colorFrame,cv2.COLOR_HSV2BGR)

    cv2.imshow('SaturationColorBoxWin',colorFrame)
    cv2.moveWindow('SaturationColorBoxWin',0,0)

    # Color windows for value
    for row in range(0,256):
        for column in range(0,720):
            # HSV 
            HSVColor = (int(column/4),255,row)
            colorFrame[row,column]= HSVColor

    colorFrame = cv2.cvtColor(colorFrame,cv2.COLOR_HSV2BGR)

    cv2.imshow('ValueColorBoxWin',colorFrame)
    cv2.moveWindow('ValueColorBoxWin',0,row+4)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()