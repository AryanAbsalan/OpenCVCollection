from handsdetection import HandsDrawing
import cv2
print(cv2.__version__)

width = 1280
height = 720


class mpHands:
    import mediapipe as mp

    def __init__(self, maxHands=2, tol1=.5, tol2=.5):
        self.hands = self.mp.solutions.hands.Hands(False, maxHands, tol1, tol2)

    def Marks(self, frame):
        myHands = []

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)

        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append(
                        (int(landMark.x*width), int(landMark.y*height)))
                myHands.append(myHand)
        return myHands


camera = cv2.VideoCapture(4, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# findHands=HandsDrawing()
findHands = mpHands(2)

while True:
    ignore,  frame = camera.read()
    frame = cv2.resize(frame, (width, height))
    # handData=findHands.find_land_marks(frame=frame,width=width,height=height)
    handData = findHands.Marks(frame)
    for hand in handData:
        for ind in [0, 5, 6, 7, 8]:
            cv2.circle(frame, hand[ind], 25, (255, 0, 255), 3)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
