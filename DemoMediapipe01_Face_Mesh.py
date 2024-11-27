import mediapipe as mp
import cv2
print(cv2.__version__)

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
    results = face.process(frameRGB)

    if results.multi_face_landmarks != None:
        for faceLandMarks in results.multi_face_landmarks:
            # mp_draw.draw_landmarks(frame, faceLandMarks, mp_face_mesh.FACE_CONNECTIONS)
            # AttributeError: module 'mediapipe.python.solutions.face_mesh' has no attribute 'FACE_CONNECTIONS'
            # FACE_CONNECTIONS is renamed to FACEMESH_CONTOURS.
            # from mediapipe.python.solutions.face_mesh_connections import FACEMESH_CONTOURS
            mp_draw.draw_landmarks(frame, faceLandMarks,
                                   mp_face_mesh.FACEMESH_CONTOURS,)

    # Showing frame
    cv2.imshow('FaceWin', frame)
    cv2.moveWindow('FaceWin', Xpos, Ypos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
