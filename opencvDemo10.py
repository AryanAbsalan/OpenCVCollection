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

# size of the moving box
snipW = 120
snipH= 60

# center of the box
boxCR= int(height/2)
boxCC= int(width/2)

# moving the box: 10 pixel each time
boxMoveRow = 10
boxMoveCol = 10

while True:
    ignore,  frame = camera.read()

    # creating region of interest frame
    frameROI = frame[int(boxCR - snipH/2):int(boxCR + snipH/2), int(boxCC - snipW/2):int(boxCC + snipW/2)]

    # changing color and demention of the frame 
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCR - snipH/2):int(boxCR + snipH/2), int(boxCC - snipW/2):int(boxCC + snipW/2)] = frameROI

    # moving the center box
    if boxCR - snipH/2 <= 0 or boxCR + snipH/2 >= height:
        boxMoveRow = boxMoveRow * (-1)
    if boxCC - snipW/2 <= 0 or boxCC + snipW/2 >= width:
        boxMoveCol = boxMoveCol * (-1)

    boxCR = boxCR + boxMoveRow
    boxCC = boxCC + boxMoveCol

    cv2.imshow('Demo10', frame)
    cv2.moveWindow('Demo10',0,0)

    cv2.imshow('frameROI', frameROI)
    cv2.moveWindow('frameROI', width + 50,0)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()