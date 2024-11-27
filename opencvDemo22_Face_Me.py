import cv2
print(cv2.__version__)
import face_recognition as FR

# Size of the screen
width = 640
height = 340

# Camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
Xpos = 0                  # Default value for x position of frame window
Ypos = 0                  # Default value for y position of frame window

# Settings
font=cv2.FONT_HERSHEY_SIMPLEX

# Loading known faces
myFace=FR.load_image_file('C:/Demo/DemoImages/known/Aryan.jpg')
aryanFaceEncode=FR.face_encodings(myFace)[0]

knownEncodings=[aryanFaceEncode]
names=['Aryan']

# Loading unknown faces from camera
while True:
    # Camera frame
    ignore, faceFrame=camera.read()

    faceLocations=FR.face_locations(faceFrame)
    unknownEncodings=FR.face_encodings(faceFrame,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        cv2.rectangle(faceFrame,(left,top),(right,bottom),(255,0,0),3)
        name='Unknown Person'
        # Comparing unknown face with known faces
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        #print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            name=names[matchIndex]
        cv2.putText(faceFrame,name,(left,top),font,.75,(0,0,255),2)

    cv2.imshow('FacesWin',faceFrame)
    cv2.moveWindow('FacesWin',Xpos,Ypos)

    if cv2.waitKey(1) & 0xff== ord('q'):
        break

camera.release()