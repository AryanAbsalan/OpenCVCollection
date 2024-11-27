import cv2
from handsdetection import  HandsDrawing
from facedetection import   FaceDrawing
from posedetection import   PoseDrawing
print(cv2.__version__)

import mediapipe as mp

# class mpFace:
#     import mediapipe as mp 
#     def __init__(self):
#         self.myFace=self.mp.solutions.face_detection.FaceDetection()
#     def Marks(self,frame):
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.myFace.process(frameRGB)
#         faceBoundBoxs=[]
#         if results.detections != None:
#             for face in results.detections:
#                 bBox=face.location_data.relative_bounding_box
#                 topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
#                 bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
#                 faceBoundBoxs.append((topLeft,bottomRight))
#         return faceBoundBoxs

# class mpPose:
#     import mediapipe as mp
#     def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
#         self.myPose=self.mp.solutions.pose.Pose(still,upperBody,smoothData,tol1,tol2)
#     def Marks(self,frame):
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.myPose.process(frameRGB)
#         poseLandmarks=[]
#         if results.pose_landmarks:
#             for lm in results.pose_landmarks.landmark:            
#                 poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
#         return poseLandmarks

# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         handsType=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             #print(results.multi_handedness)
#             for hand in results.multi_handedness:
#                 #print(hand)
#                 #print(hand.classification)
#                 #print(hand.classification[0])
#                 handType=hand.classification[0].label
#                 handsType.append(handType)
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands,handsType

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=HandsDrawing() # Done
findFace=FaceDrawing() 
mp_pose = mp.solutions.pose
findPose=mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)

mp_draw = mp.solutions.drawing_utils

font=cv2.FONT_HERSHEY_SIMPLEX
fontColor=(0,0,255)
Radius = 10
Red = (0, 0, 255)
Thickness = -1

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))


    # Face
    faceLoc=findFace.find_land_marks(frame,width=width, height=height)

    for face in faceLoc:
        cv2.rectangle(frame,face[0],face[1],(255,0,0),3)

    # Pose
    #poseLM=findPose.find_land_marks(frame,width=width, height=height)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    poseLM = findPose.process(frameRGB)
    land_marks=[]

    if poseLM.pose_landmarks != None:
        mp_draw.draw_landmarks(frame,poseLM.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        #print(results.pose_landmarks)
        #print(results.pose_landmarks.landmark)
        for lm in poseLM.pose_landmarks.landmark:
            #print(lm.x,lm.y)
            land_marks.append((int(lm.x*width),int(lm.y*height)))
    
        #print(land_marks)

    #cv2.circle(frame,land_marks[0],radius=Radius,color=Red,thickness=Thickness)

    # if poseLM != []:
    #     for ind in [13,14,15,16]:
    #         cv2.circle(frame,poseLM[ind],20,(0,255,0),-1)

    # Hand and HandType: Left | Right
    handsLM,handsType=findHands.find_land_marks(frame,width=width, height=height)

    for hand,handType in zip(handsLM,handsType):
        if handType=='Right':
            lbl='Right'
        if handType=='Left':
            lbl='Left'
        cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()