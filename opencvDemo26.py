import cv2
import face_recognition as FR
import pickle
import os

unknownImgDir='C:\\Demo\\DemoImages\\unknown'
#save_path = 'C:\\Demo\\DemoImages\\Detected'
knownEncodings=[]
names=[]

font=cv2.FONT_HERSHEY_SIMPLEX

# Loading known faces from train.pkl model
with open('train.pkl','rb') as f:
    names=pickle.load(f)                # loading names from file
    knownEncodings=pickle.load(f)       # loading knownEncodings from file

# Loading unknown faces from file
for root, dirs, files in os.walk(unknownImgDir):
    for file in files:
        unknownImgPath=os.path.join(root,file)
        unknownFace=FR.load_image_file(unknownImgPath)

        # Image color should be converted to BGR to be shown by cv2
        unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
        faceLocations=FR.face_locations(unknownFace)
        unknownEncodings=FR.face_encodings(unknownFace,faceLocations)

        for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
            top,right,bottom,left=faceLocation
            cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
            name='Unknown Person'
            # Comparing unknown face with known faces
            matches=FR.compare_faces(knownEncodings,unknownEncoding)
            if True in matches:
                matchIndex=matches.index(True)
                name=names[matchIndex]
                cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)

            cv2.imshow(name,unknownFaceBGR)
            cv2.moveWindow(name,0,0)

            cv2.waitKey(3000)
            cv2.destroyAllWindows()
