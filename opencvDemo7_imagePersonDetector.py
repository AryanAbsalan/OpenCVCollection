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

while True:
    image = cv2.imread('person.jpg')
    if image is not None:
        image = imutils.resize(image, width=640, height= 640)
        (H, W) = image.shape[:2]
        # creating blob from image 
        blobImage = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)

        detector.setInput(blobImage)
        person_detections = detector.forward()

        for i in np.arange(0, person_detections.shape[2]):
            confidence = person_detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(person_detections[0, 0, i, 1])

                if CLASSES[idx] != "person":
                    continue

                person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = person_box.astype("int")

                # rectangle color
                recColor = (0,0,255)
                recThickness = 2
                cv2.rectangle(image, (startX, startY), (endX, endY), recColor, recThickness)

        cv2.imshow("Results", image)

        key = cv2.waitKey(1) 
        if key == ord('q'):
                break
    else:
        print ("Image is None")
        break

# Closing all windows
cv2.destroyAllWindows()