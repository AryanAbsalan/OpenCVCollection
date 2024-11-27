import cv2
print(cv2.__version__)
import face_recognition as FR
import os

imgDir='C:\\Demo\DemoImages\known'
knownEncodings=list()
names=list()

for root, dirs, files in os.walk(imgDir):
    print('Root folder: ', root)
    #print('Folders: ', dirs)
    #print('Files: ', files)

    for file in files:
        imgPath=os.path.join(root,file)
        print(imgPath)

        imgFile=FR.load_image_file(imgPath)
        imgFileBGR=cv2.cvtColor(imgFile,cv2.COLOR_RGB2BGR)
        knownEncodings.append(FR.face_encodings(imgFile)[0])

        name=os.path.splitext(file)[0] # Aryan.jpg -> name=Aryan
        names.append(name)

        cv2.imshow(name,imgFileBGR)
        cv2.moveWindow(name,0,0)

        cv2.waitKey(100)
        cv2.destroyAllWindows()

