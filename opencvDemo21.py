import cv2
import face_recognition as FR
import imutils

# Installing Cmake: pip install Cmake
# Installing face_recognition: pip install face_recognition==1.2.3
# If installation of fface_recognition fails : ip install dlib from https://pypi.org/simple/dlib
# By copying link of a proper versio of dlib acording to the python version of the venv 
# This venv  has python 3.6: install dlib version 36 from the pypi.org
# If installation of opencv-python fails, do the same process : https://pypi.org/simple/opencv_python

# Settings
font=cv2.FONT_HERSHEY_SIMPLEX

# Loading known faces

donFace=FR.load_image_file('C:/Demo/DemoImages/known/Donald Trump.jpg')
donFaceEncode=FR.face_encodings(donFace)[0]

# Face location 
# donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR)                                
# donFaceLocation=FR.face_locations(donFace)[0]
# top,right,bottom,left=donFaceLocation                                      # trbl for face locations
# cv2.rectangle(donFaceBGR,(left,top),(right,bottom),(255,0,0),3)            # ltrb for rectangle
# cv2.putText(donFaceBGR,'Donald Trump',(left,top),font,.75,(0,0,255),2)     # lt for putText

nancyFace=FR.load_image_file('C:/Demo/DemoImages/known/Nancy Pelosi.jpg')
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

penceFace=FR.load_image_file('C:/Demo/DemoImages/known/Mike Pence.jpg')
penceFaceEncode=FR.face_encodings(penceFace)[0]

kennyFace=FR.load_image_file('C:/Demo/DemoImages/known/kenny-g.jpg')
kennyFaceEncode=FR.face_encodings(kennyFace)[0]

knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode,kennyFaceEncode]
names=['Donald Trump','Nancy Pelosi','Mike Pence','Kenny-G']

# Loading unknown faces
unknownFace=FR.load_image_file('C:/Demo/DemoImages/unknown/u14.jpg')

# Image color should be converted to BGR to be shown by cv2
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations)
#print(len(unknownEncodings)) # number of found faces 

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left=faceLocation
    # print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='Unknown Person'
    # Comparing unknown face with known faces
    matches=FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)

unknownFaceBGR = imutils.resize(unknownFaceBGR, width=1280, height= 840)
cv2.imshow('FacesWin',unknownFaceBGR)

#cv2.imshow('donFacesWin',donFaceBGR)

cv2.waitKey(15000)