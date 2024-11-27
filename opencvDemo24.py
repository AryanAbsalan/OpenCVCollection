import cv2
print(cv2.__version__)
import face_recognition as FR
import os
import pickle

imgDir='C:\\Demo\DemoImages\known'
knownEncodings=list()
names=list()

for root, dirs, files in os.walk(imgDir):
    #print('Root folder: ', root)
    #print('Folders: ', dirs)
    #print('Files: ', files)

    for file in files:
        imgPath=os.path.join(root,file)
        #print(imgPath)

        imgFile=FR.load_image_file(imgPath)
        knownEncodings.append(FR.face_encodings(imgFile)[0])
        names.append(os.path.splitext(file)[0])
with open('train.pkl','wb') as f:
    pickle.dump(names,f)
    pickle.dump(knownEncodings,f)
    print('train.pkl created!')

    

