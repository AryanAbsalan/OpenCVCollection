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

# Face drawing
mp_face_mesh = mp.solutions.face_mesh
#face = face_mesh.FaceMesh(max_num_faces=2)
face = mp_face_mesh.FaceMesh(static_image_mode=False,
                          max_num_faces=1,
                          refine_landmarks=False,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)
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

myHands = []
# Loading camera
while True:
    # Camera frame
    ignore, frame = camera.read()

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_results = face.process(frameRGB)
    hands_results = hands.process(frameRGB)

    # Drawing face land marks
    if face_results.multi_face_landmarks != None:
        for faceLandMarks in face_results.multi_face_landmarks:
            # mp_draw.draw_landmarks(frame, faceLandMarks, mp_face_mesh.FACE_CONNECTIONS)
            # AttributeError: module 'mediapipe.python.solutions.face_mesh' has no attribute 'FACE_CONNECTIONS'
            # FACE_CONNECTIONS is renamed to FACEMESH_CONTOURS.
            # from mediapipe.python.solutions.face_mesh_connections import FACEMESH_CONTOURS
            mp_draw.draw_landmarks(frame, faceLandMarks, mp_face_mesh.FACEMESH_CONTOURS,)
    
    # Drawing hand land marks
    if hands_results.multi_hand_landmarks != None:
        for handLandMarks in hands_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            myHand = []
            for handLandMark in handLandMarks.landmark:
                #print(handLandMark.x, handLandMark.y)
                myHand.append((int(handLandMark.x*width),int(handLandMark.y*height)))
                # print(myHand)
            myHands.append(myHand)

            # Drawing circle on tip of fingers
            # cv2.circle(frame, myHand[4], radius = Radius, color = Black, thickness = Thickness)
            # cv2.circle(frame, myHand[8], radius = Radius, color = Black, thickness = Thickness)

            # cv2.circle(frame, myHand[12], radius = Radius, color = Black, thickness = Thickness)
            # cv2.circle(frame, myHand[16], radius = Radius, color = Black, thickness = Thickness)
            # cv2.circle(frame, myHand[20], radius = Radius, color = Black, thickness = Thickness)

            # Short form
            for i in [4,8,12,16,20]:
                cv2.circle(frame, myHand[i], radius = Radius, color = Black, thickness = Thickness)

            
    # Showing frame
    cv2.imshow('FaceWin', frame)
    cv2.moveWindow('FaceWin', Xpos, Ypos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
