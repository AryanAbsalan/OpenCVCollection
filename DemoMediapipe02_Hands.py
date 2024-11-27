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

mp_draw = mp.solutions.drawing_utils

Radius = 10
Red = (0, 0, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
Thickness = -1

# Loading camera
while True:
    myHands = []

    # Camera frame
    ignore, frame = camera.read()
    frame = cv2.resize(frame, (width, height))

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)

    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            # myHand = []
            # for handLandMark in handLandMarks.landmark:
            #     #print(handLandMark.x, handLandMark.y)
            #     myHand.append((int(handLandMark.x*width),int(handLandMark.y*height)))
            #     # print(myHand)
            # myHands.append(myHand)

            # # Drawing circle on tip of fingers
            # cv2.circle(frame, myHand[4], radius = Radius, color = Black, thickness = Thickness)
            # cv2.circle(frame, myHand[8], radius = Radius, color = Black, thickness = Thickness)

            # cv2.circle(frame, myHand[12], radius = Radius, color = Black, thickness = Thickness)
            # cv2.circle(frame, myHand[16], radius = Radius, color = Black, thickness = Thickness)
            # cv2.circle(frame, myHand[20], radius = Radius, color = Black, thickness = Thickness)

            # # Drawing circle on hand land marks
            # for i in range(0, len(myHand)):
            #     cv2.circle(frame, myHand[i], radius=(Radius-2), color=Red, thickness=Thickness)

            #     # Drawing line between hand land marks
            #     if i != 20:
            #         cv2.line(frame, (myHand[i]), (myHand[i+1]), color=Green, thickness=2)
            #     else:    
            #         cv2.line(frame, (myHand[0]), (myHand[20]), color=Green, thickness=2)

    # Showing frame
    cv2.imshow('HandWin', frame)
    cv2.moveWindow('HandWin', Xpos, Ypos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
