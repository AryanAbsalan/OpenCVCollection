import cv2
print(cv2.__version__)
import mediapipe as mp

# Size of the screen
width = 1280
height = 720

# Camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

Xpos = 0                  # Default value for x position of frame window
Ypos = 0                  # Default value for y position of frame window

# Hands drawing
hands = mp.solutions.hands.Hands(static_image_mode=False,
                                 max_num_hands=2,
                                 model_complexity=1,
                                 min_detection_confidence=0.5,
                                 min_tracking_confidence=0.5)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)

mp_draw = mp.solutions.drawing_utils

Radius = 10
Red = (0, 0, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
Thickness = -1

# Loading camera
while True:
    # Camera frame
    ignore, frame = camera.read()
    frame = cv2.resize(frame, (width, height))

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    #print(results)

    land_marks=[]

    if results.pose_landmarks != None:
        mp_draw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        #print(results.pose_landmarks)
        #print(results.pose_landmarks.landmark)
        for lm in results.pose_landmarks.landmark:
            #print(lm.x,lm.y)
            land_marks.append((int(lm.x*width),int(lm.y*height)))
        
        #print(land_marks)

        cv2.circle(frame,land_marks[0],radius=Radius,color=Red,thickness=Thickness)
        cv2.circle(frame,land_marks[2],radius=Radius,color=Green,thickness=Thickness)
        cv2.circle(frame,land_marks[5],radius=Radius,color=Green,thickness=Thickness)

    # Showing frame
    cv2.imshow('HandWin', frame)
    cv2.moveWindow('HandWin', Xpos, Ypos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
