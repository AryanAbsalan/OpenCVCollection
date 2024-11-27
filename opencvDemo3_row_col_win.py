
import cv2

width = 1280
height = 720

# camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# number of rows and columns 
rows = int(input('How many rows? '))
columns = int(input('How many columns? '))

while True:
    ignore , frame = camera.read()
    frame = cv2.resize(frame,(int(width/columns),int(height/columns)))

    # resizing gray frame
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFrame = cv2.resize(grayFrame,(int(width/columns),int(height/columns)))

    for i in range(0, rows):
        for j in range(0, columns):
            winName = 'window' + str(i) + 'x' + str(j)

            cv2.imshow(winName, frame)

            # calculating position of window
            x = int(width / columns + 10) * j
            y = int(height / rows + 40) * i
            cv2.moveWindow(winName, x , y )

            # gray frame at odd columns
            if j % 2 != 0 :
                 cv2.imshow(winName, grayFrame)
                 cv2.moveWindow(winName, x , y )
  
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# release camera
camera.release()