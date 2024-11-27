import cv2
print(cv2.__version__)
import face_recognition as FR
import pickle

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
text_color=(255,0,0)
rectangle_color=text_color

# Loading known faces from train.pkl model
with open('train.pkl','rb') as f:
    names=pickle.load(f)                # loading names from file
    knownEncodings=pickle.load(f)       # loading knownEncodings from file

# Loading unknown faces from camera
while True:
    # Camera frame
    ignore, faceFrame=camera.read()

    faceLocations=FR.face_locations(faceFrame)
    unknownEncodings=FR.face_encodings(faceFrame,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        cv2.rectangle(faceFrame,(left,top),(right,bottom),rectangle_color,3)
        name='Unknown Person'
        # Comparing unknown face with known faces
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        #print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            name=names[matchIndex]
        cv2.putText(faceFrame,name,(left,top),font,.75,text_color,2)

    cv2.imshow('FacesWin',faceFrame)
    cv2.moveWindow('FacesWin',Xpos,Ypos)

    if cv2.waitKey(1) & 0xff== ord('q'):
        break

camera.release()
