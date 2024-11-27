import cv2
import numpy as np
import imutils

prototxt = "MobileNetSSD_deploy.prototxt"
caffemodel = "MobileNetSSD_deploy.caffemodel"

detector = cv2.dnn.readNetFromCaffe(prototxt=prototxt, caffeModel=caffemodel)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

width = 1280
height = 720

# camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# video = cv2.VideoCapture("video1.mp4")

while True:
    # ignore , frame = video.read()
    ignore , frame = camera.read()
    if frame is not None:
        frame = imutils.resize(frame, width=1280, height= 840)
        (H, W) = frame.shape[:2]
        # creating blob from image 
        blobVideo = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

        detector.setInput(blobVideo)
        person_detections = detector.forward()

        for i in np.arange(0, person_detections.shape[2]):
            confidence = person_detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(person_detections[0, 0, i, 1])

                car = CLASSES[idx] == "car"
                bicycle = CLASSES[idx] == "bicycle"
                bus = CLASSES[idx] == "bus"
                person = CLASSES[idx] == "person" 
                dog = CLASSES[idx] == "dog"
            
                if car or bicycle or bus or person or dog :
                    person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                    (startX, startY, endX, endY) = person_box.astype("int")
                    # rectangle color
                    recColor = (0,0,255)
                    recThickness = 2
                    cv2.rectangle(frame, (startX, startY), (endX, endY), recColor, recThickness)   
                else :
                    continue

        cv2.imshow("Results", frame)
        # cv2.imwrite("Result.jpg", frame)

        key = cv2.waitKey(1) 
        if key == ord('q'):
                break
    else:
        print ("Image is None")
        break

# Closing all windows
cv2.destroyAllWindows()