import cv2

width = 640
height = 480
# camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore , frame = camera.read()

    #Learning Computer Vision 1 at position 0,0
    cv2.imshow('Vision1', frame) 
    cv2.moveWindow('Vision1', 0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# release camera
camera.release()
