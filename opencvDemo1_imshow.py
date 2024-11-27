import cv2

# creating camera object
camera = cv2.VideoCapture(0)

while True:
    ignore , frame = camera.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Learning Computer Vision 1 at position 0,0
    cv2.imshow('Vision1', frame) 
    cv2.moveWindow('Vision1', 0,0)
    cv2.resizeWindow('Vision1', 620,300)
    
    #Learning Computer Vision 2 at position 650,0
    cv2.imshow('Vision2', grayFrame)
    cv2.moveWindow('Vision2',650,0)
    cv2.resizeWindow('Vision2', 620,300)
    
    #Learning Computer Vision 3 at position 0,350
    cv2.imshow('Vision3', grayFrame)
    cv2.moveWindow('Vision3',0,350)
    cv2.resizeWindow('Vision3', 620,300)

    #Learning Computer Vision 4 at position 650, 350
    cv2.imshow('Vision4', frame)
    cv2.moveWindow('Vision4', 650,350)
    cv2.resizeWindow('Vision4', 620,300)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# release camera
camera.release()