# region Project requirements
from random import randint
import cv2
import mediapipehelper as mph
import numpy as np

# ****************************
import mediapipe as mp
# endregion 

# region Const Variables
HANDENESS_LEFT = 0
HANDENESS_RIGHT = 1

HAND_REGION_ALL = 0
HAND_REGION_WRIST = 1
HAND_REGION_THUMB = 2
HAND_REGION_INDEX_FINGER = 3
HAND_REGION_MIDDLE_FINGER = 4
HAND_REGION_RING_FINGER = 5
HAND_REGION_PINKY = 6

# https://github.com/tensorflow/tfjs-models/commit/838611c02f51159afdd77469ce67f0e26b7bbb23
FACEMESH_REGION_ALL = 0
FACEMESH_REGION_SILHOUETTE = 1
FACEMESH_REGION_LIPS_UPPER_OUTER = 2
FACEMESH_REGION_LIPS_LOWER_OUTER = 3
FACEMESH_REGION_LIPS_UPPER_INNER = 4
FACEMESH_REGION_LIPS_LOWER_INNER = 5
FACEMESH_REGION_RIGHT_EYE_UPPER_0 = 6
FACEMESH_REGION_RIGHT_EYE_LOWER_0 = 7
FACEMESH_REGION_RIGHT_EYE_UPPER_1 = 8
FACEMESH_REGION_RIGHT_EYE_LOWER_1 = 9
FACEMESH_REGION_RIGHT_EYE_UPPER_2 = 10
FACEMESH_REGION_RIGHT_EYE_LOWER_2 = 11
FACEMESH_REGION_RIGHT_EYE_LOWER_3 = 12
FACEMESH_REGION_RIGHT_EYEBROW_UPPER = 13
FACEMESH_REGION_RIGHT_EYEBROW_LOWER = 14
FACEMESH_REGION_LEFT_EYE_UPPER_0 = 15
FACEMESH_REGION_LEFT_EYE_LOWER_0 = 16
FACEMESH_REGION_LEFT_EYE_UPPER_1 = 17
FACEMESH_REGION_LEFT_EYE_LOWER_1 = 18
FACEMESH_REGION_LEFT_EYE_UPPER_2 = 19
FACEMESH_REGION_LEFT_EYE_LOWER_2 = 20
FACEMESH_REGION_LEFT_EYE_LOWER_3 = 21
FACEMESH_REGION_LEFT_EYEBROW_UPPER = 22
FACEMESH_REGION_LEFT_EYEBROW_LOWER = 23
FACEMESH_REGION_MIDWAY_BETWEEN_EYES = 24
FACEMESH_REGION_NOSE_TIP = 25
FACEMESH_REGION_NOSE_BOTTOM = 26
FACEMESH_REGION_NOSE_RIGHT_CORNER = 27
FACEMESH_REGION_NOSE_LEFT_CORNER = 28
FACEMESH_REGION_RIGHT_CHEEK = 29
FACEMESH_REGION_LEFT_CHEEK = 30

POSE_REGION_ALL = 0
POSE_REGION_NOSE = 1
POSE_REGION_LEFT_EYE_INNER = 2
POSE_REGION_LEFT_EYE = 3
POSE_REGION_LEFT_EYE_OUTER = 4
POSE_REGION_RIGHT_EYE_INNER = 5
POSE_REGION_RIGHT_EYE = 6
POSE_REGION_RIGHT_EYE_OUTER = 7
POSE_REGION_LEFT_EAR = 8
POSE_REGION_RIGHT_EAR = 9
POSE_REGION_MOUTH_LEFT = 10
POSE_REGION_MOUTH_RIGHT = 11
POSE_REGION_LEFT_SHOULDER = 12
POSE_REGION_RIGHT_SHOULDER = 13
POSE_REGION_LEFT_ELBOW = 14
POSE_REGION_RIGHT_ELBOW = 15
POSE_REGION_LEFT_WRIST = 16
POSE_REGION_RIGHT_WRIST = 17
POSE_REGION_LEFT_PINKY = 18
POSE_REGION_RIGHT_PINKY = 19
POSE_REGION_LEFT_INDEX = 20
POSE_REGION_RIGHT_INDEX = 21
POSE_REGION_LEFT_THUMB = 22
POSE_REGION_RIGHT_THUMB = 23
POSE_REGION_LEFT_HIP = 24
POSE_REGION_RIGHT_HIP = 25
POSE_REGION_LEFT_KNEE = 26
POSE_REGION_RIGHT_KNEE = 27
POSE_REGION_LEFT_ANKLE = 28
POSE_REGION_RIGHT_ANKLE = 29
POSE_REGION_LEFT_HEEL = 30
POSE_REGION_RIGHT_HEEL = 31
POSE_REGION_LEFT_FOOT = 32
POSE_REGION_RIGHT_FOOT = 33
# endregion 

# class Face
class Face:
    def __init__(self, boxUpperLeft, boxLowerRight):
        self.__boxUpperLeft__ = boxUpperLeft
        self.__boxLowerRight__ = boxLowerRight

    def getBoxUpperLeft(self):
        return self.__boxUpperLeft__

    def getBoxLowerRight(self):
        return self.__boxLowerRight__

# class FaceMesh
class FaceMesh:
    # https://github.com/tensorflow/tfjs-models/commit/838611c02f51159afdd77469ce67f0e26b7bbb23
    __regionIndexes__ = {
        FACEMESH_REGION_ALL: range(0, 468),
        FACEMESH_REGION_SILHOUETTE: [
            10,  338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
            397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
            172, 58,  132, 93,  234, 127, 162, 21,  54,  103, 67,  109
        ],
        FACEMESH_REGION_LIPS_UPPER_OUTER: [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291],
        FACEMESH_REGION_LIPS_LOWER_OUTER: [146, 91, 181, 84, 17, 314, 405, 321, 375, 291],
        FACEMESH_REGION_LIPS_UPPER_INNER: [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308],
        FACEMESH_REGION_LIPS_LOWER_INNER: [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308],
        FACEMESH_REGION_RIGHT_EYE_UPPER_0: [246, 161, 160, 159, 158, 157, 173],
        FACEMESH_REGION_RIGHT_EYE_LOWER_0: [33, 7, 163, 144, 145, 153, 154, 155, 133],
        FACEMESH_REGION_RIGHT_EYE_UPPER_1: [247, 30, 29, 27, 28, 56, 190],
        FACEMESH_REGION_RIGHT_EYE_LOWER_1: [130, 25, 110, 24, 23, 22, 26, 112, 243],
        FACEMESH_REGION_RIGHT_EYE_UPPER_2: [113, 225, 224, 223, 222, 221, 189],
        FACEMESH_REGION_RIGHT_EYE_LOWER_2: [226, 31, 228, 229, 230, 231, 232, 233, 244],
        FACEMESH_REGION_RIGHT_EYE_LOWER_3: [143, 111, 117, 118, 119, 120, 121, 128, 245],
        FACEMESH_REGION_RIGHT_EYEBROW_UPPER: [156, 70, 63, 105, 66, 107, 55, 193],
        FACEMESH_REGION_RIGHT_EYEBROW_LOWER: [35, 124, 46, 53, 52, 65],
        FACEMESH_REGION_LEFT_EYE_UPPER_0: [466, 388, 387, 386, 385, 384, 398],
        FACEMESH_REGION_LEFT_EYE_LOWER_0: [263, 249, 390, 373, 374, 380, 381, 382, 362],
        FACEMESH_REGION_LEFT_EYE_UPPER_1: [467, 260, 259, 257, 258, 286, 414],
        FACEMESH_REGION_LEFT_EYE_LOWER_1: [359, 255, 339, 254, 253, 252, 256, 341, 463],
        FACEMESH_REGION_LEFT_EYE_UPPER_2: [342, 445, 444, 443, 442, 441, 413],
        FACEMESH_REGION_LEFT_EYE_LOWER_2: [446, 261, 448, 449, 450, 451, 452, 453, 464],
        FACEMESH_REGION_LEFT_EYE_LOWER_3: [372, 340, 346, 347, 348, 349, 350, 357, 465],
        FACEMESH_REGION_LEFT_EYEBROW_UPPER: [383, 300, 293, 334, 296, 336, 285, 417],
        FACEMESH_REGION_LEFT_EYEBROW_LOWER: [265, 353, 276, 283, 282, 295],
        FACEMESH_REGION_MIDWAY_BETWEEN_EYES: [168],
        FACEMESH_REGION_NOSE_TIP: [1],
        FACEMESH_REGION_NOSE_BOTTOM: [2],
        FACEMESH_REGION_NOSE_RIGHT_CORNER: [98],
        FACEMESH_REGION_NOSE_LEFT_CORNER: [327],
        FACEMESH_REGION_RIGHT_CHEEK: [205],
        FACEMESH_REGION_LEFT_CHEEK: [425]
    }

    def __init__(self, landmarks):
        self.__landmarks__ = landmarks

    def getLandmarks(self, *regions):
        landmarkIndices = set()

        if (len(regions) == 0):
            for i in FaceMesh.__regionIndexes__[FACEMESH_REGION_ALL]:
                landmarkIndices.add(i)
        else:
            for r in regions:
                for i in FaceMesh.__regionIndexes__[r]:
                    landmarkIndices.add(i)

        arr = []
        for i in set(landmarkIndices):
            arr.append(self.__landmarks__[i])
        return arr

# class Hand
class Hand:
    __regionIndexes__ = {
        HAND_REGION_ALL: range(0, 21),
        HAND_REGION_WRIST: [0],
        HAND_REGION_THUMB: [1, 2, 3, 4],
        HAND_REGION_INDEX_FINGER: [5, 6, 7, 8],
        HAND_REGION_MIDDLE_FINGER: [9, 10, 11, 12],
        HAND_REGION_RING_FINGER: [13, 14, 15, 16],
        HAND_REGION_PINKY: [17, 18, 19, 20]
    }

    def __init__(self, landmarks, handedness):
        self.__landmarks__ = landmarks
        self.__handedness__ = handedness

    def getLandmarks(self, *regions):
        landmarkIndices = set()

        if (len(regions) == 0):
            for i in Hand.__regionIndexes__[HAND_REGION_ALL]:
                landmarkIndices.add(i)
        else:
            for r in regions:
                for i in Hand.__regionIndexes__[r]:
                    landmarkIndices.add(i)

        arr = []
        for i in set(landmarkIndices):
            arr.append(self.__landmarks__[i])
        return arr

    def getHandedness(self):
        return self.__handedness__

# class Pose
class Pose:
    __regionIndexes__ = {
        POSE_REGION_ALL: range(0, 33),
        POSE_REGION_NOSE: [0],
        POSE_REGION_LEFT_EYE_INNER: [1],
        POSE_REGION_LEFT_EYE: [2],
        POSE_REGION_LEFT_EYE_OUTER: [3],
        POSE_REGION_RIGHT_EYE_INNER: [4],
        POSE_REGION_RIGHT_EYE: [5],
        POSE_REGION_RIGHT_EYE_OUTER: [6],
        POSE_REGION_LEFT_EAR: [7],
        POSE_REGION_RIGHT_EAR: [8],
        POSE_REGION_MOUTH_LEFT: [9],
        POSE_REGION_MOUTH_RIGHT: [10],
        POSE_REGION_LEFT_SHOULDER: [11],
        POSE_REGION_RIGHT_SHOULDER: [12],
        POSE_REGION_LEFT_ELBOW: [13],
        POSE_REGION_RIGHT_ELBOW: [14],
        POSE_REGION_LEFT_WRIST: [15],
        POSE_REGION_RIGHT_WRIST: [16],
        POSE_REGION_LEFT_PINKY: [17],
        POSE_REGION_RIGHT_PINKY: [18],
        POSE_REGION_LEFT_INDEX: [19],
        POSE_REGION_RIGHT_INDEX: [20],
        POSE_REGION_LEFT_THUMB: [21],
        POSE_REGION_RIGHT_THUMB: [22],
        POSE_REGION_LEFT_HIP: [23],
        POSE_REGION_RIGHT_HIP: [24],
        POSE_REGION_LEFT_KNEE: [25],
        POSE_REGION_RIGHT_KNEE: [26],
        POSE_REGION_LEFT_ANKLE: [27],
        POSE_REGION_RIGHT_ANKLE: [28],
        POSE_REGION_LEFT_HEEL: [29],
        POSE_REGION_RIGHT_HEEL: [30],
        POSE_REGION_LEFT_FOOT: [31],
        POSE_REGION_RIGHT_FOOT: [32]
    }

    def __init__(self, landmarks):
        self.__landmarks__ = landmarks

    def getLandmarks(self, *regions):
        landmarkIndices = set()

        if (len(regions) == 0):
            for i in Pose.__regionIndexes__[HAND_REGION_ALL]:
                landmarkIndices.add(i)
        else:
            for r in regions:
                for i in Pose.__regionIndexes__[r]:
                    landmarkIndices.add(i)

        arr = []
        for i in set(landmarkIndices):
            arr.append(self.__landmarks__[i])
        return arr

# class FaceDetection
class FaceDetection:
    def __init__(self, min_detection_confidence=0.5):
        # https://google.github.io/mediapipe/solutions/face_detection.html
        self.__mpFaceDetection__ = mp.solutions.face_detection.FaceDetection(
            min_detection_confidence=min_detection_confidence
        )

    def detectFaces(self, frameRGB):
        dimY = len(frameRGB)
        dimX = 0 if dimY == 0 else len(frameRGB[0])
        mpFaceDetectionOuput = self.__mpFaceDetection__.process(frameRGB)
        faces = []
        if mpFaceDetectionOuput.detections != None:
            for f in mpFaceDetectionOuput.detections:
                bbox = f.location_data.relative_bounding_box
                topLeft = (
                    int(bbox.xmin * dimX),
                    int(bbox.ymin * dimY)
                )
                bottomRight = (
                    int((bbox.xmin + bbox.width) * dimX),
                    int((bbox.ymin + bbox.height) * dimY)
                )
                faces.append(Face(topLeft, bottomRight))
        return faces

# class FaceMeshDetection
class FaceMeshDetection:
    def __init__(self, static_image_mode=False, max_num_faces=1,
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        # https://google.github.io/mediapipe/solutions/face_mesh.html
        self.__mpFaceMesh__ = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=static_image_mode,
            max_num_faces=max_num_faces,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def detectFaces(self, frameRGB):
        dimY = len(frameRGB)
        dimX = 0 if dimY == 0 else len(frameRGB[0])
        mpFaceMeshOuput = self.__mpFaceMesh__.process(frameRGB)
        faces = []
        if mpFaceMeshOuput.multi_face_landmarks != None:
            for f in mpFaceMeshOuput.multi_face_landmarks:
                landmarks = []
                for landmark in f.landmark:
                    lx = int(landmark.x * dimX)
                    ly = int(landmark.y * dimY)
                    landmarks.append((lx, ly))
                faces.append(FaceMesh(landmarks))
        return faces

# class HandDetection
class HandDetection:
    def __init__(self, static_image_mode=False, max_num_hands=-1,
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        # Setup media pipe
        # https://google.github.io/mediapipe/solutions/hands.html
        self.__mpHandDetection__ = mp.solutions.hands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def detectHands(self, frameRGB):
        dimY = len(frameRGB)
        dimX = 0 if dimY == 0 else len(frameRGB[0])
        frameDimensions = (dimX, dimY)

        hands = []

        mediaPipeHandDetectionOutput = self.__mpHandDetection__.process(frameRGB)
        multiHandLandmarks = mediaPipeHandDetectionOutput.multi_hand_landmarks
        multiHandedness = mediaPipeHandDetectionOutput.multi_handedness

        if multiHandLandmarks != None:
            for i in range(0, len(multiHandLandmarks)):
                rawLandmarks = multiHandLandmarks[i]
                rawHandedness = multiHandedness[i].classification[0].index
                landmarks = []
                for landmark in rawLandmarks.landmark:
                    lx = int(landmark.x * frameDimensions[0])
                    ly = int(landmark.y * frameDimensions[1])
                    landmarks.append((lx, ly))
                hands.append(Hand(landmarks, rawHandedness))

        return hands

# class PoseDetection 
class PoseDetection:
    def __init__(self, static_image_mode=False, smooth_landmarks=True,
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        # Setup media pipe
        # https://google.github.io/mediapipe/solutions/pose.html#cross-platform-configuration-options
        self.__mpPoseDetection__ = mp.solutions.pose.Pose(
            static_image_mode=static_image_mode,
            smooth_landmarks=smooth_landmarks,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def detectPose(self, frameRGB):
        dimY = len(frameRGB)
        dimX = 0 if dimY == 0 else len(frameRGB[0])
        frameDimensions = (dimX, dimY)

        poseDetectionOutput = self.__mpPoseDetection__.process(frameRGB)
        poseLandmarks = poseDetectionOutput.pose_landmarks

        landmarks = []
        if poseLandmarks != None:
            for landmark in poseLandmarks.landmark:
                lx = int(landmark.x * frameDimensions[0])
                ly = int(landmark.y * frameDimensions[1])
                landmarks.append((lx, ly))

        return None if len(landmarks) == 0 else Pose(landmarks)
# ****************************

print(f'OpenCV version is {cv2.__version__}')

# region Parameters
CAM_ID = 0
CAM_FPS = 30
CAM_RES = (640, 480)

WINDOW_CAMERA_POS = (0, 0)
WINDOW_CAMERA_NAME = 'Camera'

HAND_MIN_DETECTION_CONFIDENCE = 0.7
HAND_MIN_TRACKING_CONFIDENCE = 0.5

# 640x480 => 10
# 1280x1024 => 26
GAME_SPEED = 10
# endregion

# class Arena
class Arena:
    def __init__(self, dim):
        self.__dim__ = (dim[0], dim[1])

    def getCenter(self):
        return (
            int((self.__dim__[0] - 1) / 2),
            int((self.__dim__[1] - 1) / 2),
        )

    def getUpperLeftCorner(self):
        return (0, 0)

    def getLowerRightCorner(self):
        return (self.__dim__[0] - 1, self.__dim__[1] - 1)

    def getWidth(self):
        return self.__dim__[0]

    def getHeight(self):
        return self.__dim__[1]

# class Ball
class Ball:
    def __init__(self, radius, color):
        self.__radius__ = radius
        self.__color__ = color
        self.__center__ = (0, 0)
        self.__velocity__ = (0, 0)
        self.__thickness__ = -1

    def getRadius(self):
        return self.__radius__

    def getColor(self):
        return self.__color__

    def getCenter(self):
        return self.__center__

    def setCenter(self, center):
        self.__center__ = (center[0], center[1])

    def getVelocity(self):
        return self.__velocity__

    def setVelocity(self, velocity):
        self.__velocity__ = (velocity[0], velocity[1])

    def move(self):
        self.__center__ = (
            round(self.__center__[0] + self.__velocity__[0]),
            round(self.__center__[1] + self.__velocity__[1])
        )

    def getThickness(self):
        return self.__thickness__

    def setThickness(self, thickness):
        self.__thickness__ = thickness

# class Paddle
class Paddle:
    def __init__(self, width, height, color):
        self.__width__ = width
        self.__height__ = height
        self.__color__ = color
        self.__upperLeftCorner__ = (0, 0)

    def getWidth(self):
        return self.__width__

    def getHeight(self):
        return self.__height__

    def getCenter(self):
        cx = self.getUpperLeftCorner()[0] + int(self.getWidth() / 2)
        cy = self.getUpperLeftCorner()[1] + int(self.getHeight() / 2)
        return (cx, cy)

    def getColor(self):
        return self.__color__

    def setUpperLeftCorner(self, upperLeftCorner):
        self.__upperLeftCorner__ = (upperLeftCorner[0], upperLeftCorner[1])

    def getUpperLeftCorner(self):
        return self.__upperLeftCorner__

    def getLowerRightCorner(self):
        return (
            self.__upperLeftCorner__[0] + self.__width__,
            self.__upperLeftCorner__[1] + self.__height__
        )

# class Player
class Player:
    def __init__(self, paddle):
        self.__score__ = 0
        self.__paddle__ = paddle

    def getPaddle(self):
        return self.__paddle__

    def getScore(self):
        return self.__score__

    def increaseScore(self):
        self.__score__ = self.__score__ + 1

# class GameEngine
class GameEngine:
    __LEFT_WALL__ = 0
    __CEILING__ = 1
    __RIGHT_WALL__ = 2
    __FLOOR__ = 3
    __MAX_SCORE__ = 10

    def __init__(self, arena, ball, leftPlayer, rightPlayer, gameSpeed):
        self.__arena__ = arena
        self.__ball__ = ball
        self.__leftPlayer__ = leftPlayer
        self.__rightPlayer__ = rightPlayer
        self.__gameSpeed__ = gameSpeed
        self.__isBallExploding__ = False
        self.__isGameOver__ = False
        self.__server__ = 1
        self.__scorer__ = None
        self.__resetPaddles__()
        self.__serveBall__()

    def isGameOver(self):
        return self.__isGameOver__

    def setPaddleYPosition(self, paddle, yPosition):
        if self.__isBallExploding__ or self.__isGameOver__:
            return

        arenaCeiling = self.__arena__.getUpperLeftCorner()[1]
        arenaFloor = self.__arena__.getLowerRightCorner()[1]
        newPaddleCeiling = yPosition - int(paddle.getHeight() / 2)
        newPaddleFloor = newPaddleCeiling + paddle.getHeight()

        if newPaddleCeiling < arenaCeiling:
            newPaddleCeiling = arenaCeiling
        elif newPaddleFloor > arenaFloor:
            newPaddleCeiling = arenaFloor - paddle.getHeight()

        paddle.setUpperLeftCorner((paddle.getUpperLeftCorner()[0], newPaddleCeiling))

    def tick(self):
        if self.__isBallExploding__:
            # If ball thickness is -1, we are just starting the animation.
            ballThickness = self.__ball__.getRadius() if self.__ball__.getThickness() < 0 else self.__ball__.getThickness() - 1

            if ballThickness < 1:
                self.__isBallExploding__ = False
                self.__scorer__.increaseScore()

                if self.__scorer__.getScore() >= GameEngine.__MAX_SCORE__:
                    self.__isGameOver__ = True
                else:
                    self.__ball__.setThickness(-1)
                    self.__resetPaddles__()
                    self.__serveBall__()

                self.__scorer__ = None
            else:
                self.__ball__.setThickness(ballThickness)

            return

        if self.__isGameOver__:
            return

        self.__ball__.move()

        collision = self.__detectCollision__()

        if collision[GameEngine.__LEFT_WALL__]:
            self.__handleLeftWallCollision__()

        if collision[GameEngine.__CEILING__]:
            self.__handleCeilingCollision__()

        if collision[GameEngine.__RIGHT_WALL__]:
            self.__handleRightWallCollision__()

        if collision[GameEngine.__FLOOR__]:
            self.__handleFloorCollision__()

    def __deflectBall__(self, paddle):
        vX = self.__ball__.getVelocity()[0] * -1

        # Ball Y-axis velocity is based on where the ball hits the paddle relative
        # to the paddle center. The hit position is a value between [-1.0, 1.0],
        # where -1 is the paddle upper-right corner, 0 is the paddle center and
        # 1 represents the paddle lower-right corner. The new velocity is
        # REL_DIST_FROM_PADDLE_CENTER * GAME_SPEED. A hit straight at the center of
        # the paddle would result in a velocity of 0 while a hit at the top or
        # at the bottom corner would result in a velocity of -GAME_SPEED and
        # GAME_SPEED respectively.
        paddleFloor = paddle.getLowerRightCorner()[1]
        paddleCenter = paddle.getCenter()[1]
        paddleHalfHeight = float(paddleFloor - paddleCenter)
        ballCenter = self.__ball__.getCenter()[1]
        relDistFromPaddleCenter = (ballCenter - paddleCenter) / paddleHalfHeight
        vY = self.__gameSpeed__ * relDistFromPaddleCenter
        self.__ball__.setVelocity((vX, vY))

    def __detectCollision__(self):
        arenaLeftWall = self.__arena__.getUpperLeftCorner()[0] + self.__leftPlayer__.getPaddle().getWidth()
        arenaRightWall = self.__arena__.getLowerRightCorner()[0] - self.__rightPlayer__.getPaddle().getWidth()
        arenaCeiling = self.__arena__.getUpperLeftCorner()[1]
        arenaFloor = self.__arena__.getLowerRightCorner()[1]

        ballCenter = self.__ball__.getCenter()
        ballRadius = self.__ball__.getRadius()
        ballLeft = ballCenter[0] - ballRadius
        ballRight = ballCenter[0] + ballRadius
        ballTop = ballCenter[1] - ballRadius
        ballBottom = ballCenter[1] + ballRadius

        isLeftCollision = True if ballLeft < arenaLeftWall else False
        isRightCollision = True if ballRight > arenaRightWall else False
        isTopCollision = True if ballTop < arenaCeiling else False
        isFloorCollision = True if ballBottom > arenaFloor else False

        return (isLeftCollision, isTopCollision, isRightCollision, isFloorCollision)

    def __score__(self, player):
        self.__isBallExploding__ = True
        self.__scorer__ = player

    def __handleLeftWallCollision__(self):
        arenaLeftWall = self.__arena__.getUpperLeftCorner()[0] + self.__leftPlayer__.getPaddle().getWidth()
        ballX = arenaLeftWall + self.__ball__.getRadius()  # Don't display ball passed the left wall
        ballY = self.__ball__.getCenter()[1]
        self.__ball__.setCenter((ballX, ballY))

        ballCenter = self.__ball__.getCenter()[1]
        paddleCeiling = self.__leftPlayer__.getPaddle().getUpperLeftCorner()[1]
        paddleFloor = self.__leftPlayer__.getPaddle().getLowerRightCorner()[1]
        hasMissed = ballCenter < paddleCeiling or ballCenter > paddleFloor

        if hasMissed:
            self.__score__(self.__rightPlayer__)
        else:
            self.__deflectBall__(self.__leftPlayer__.getPaddle())

    def __handleRightWallCollision__(self):
        arenaRightWall = self.__arena__.getLowerRightCorner()[0] - self.__rightPlayer__.getPaddle().getWidth()
        ballX = arenaRightWall - self.__ball__.getRadius()  # Don't display ball passed the right wall
        ballY = self.__ball__.getCenter()[1]
        self.__ball__.setCenter((ballX, ballY))

        ballCenter = self.__ball__.getCenter()[1]
        paddleCeiling = self.__rightPlayer__.getPaddle().getUpperLeftCorner()[1]
        paddleFloor = self.__rightPlayer__.getPaddle().getLowerRightCorner()[1]
        hasMissed = ballCenter < paddleCeiling or ballCenter > paddleFloor

        if hasMissed:
            self.__score__(self.__leftPlayer__)
        else:
            self.__deflectBall__(rightPlayerPaddle)

    def __handleCeilingCollision__(self):
        arenaCeiling = self.__arena__.getUpperLeftCorner()[1]
        ballX = self.__ball__.getCenter()[0]
        ballY = arenaCeiling + self.__ball__.getRadius()  # Don't display ball passed the ceiling
        self.__ball__.setCenter((ballX, ballY))
        ballVx = self.__ball__.getVelocity()[0]
        ballVy = self.__ball__.getVelocity()[1] * -1
        self.__ball__.setVelocity((ballVx, ballVy))

    def __handleFloorCollision__(self):
        arenaFloor = self.__arena__.getLowerRightCorner()[1]
        ballX = self.__ball__.getCenter()[0]
        ballY = arenaFloor - self.__ball__.getRadius()  # Don't display ball passed the floor
        self.__ball__.setCenter((ballX, ballY))
        ballVx = self.__ball__.getVelocity()[0]
        ballVy = self.__ball__.getVelocity()[1] * -1
        self.__ball__.setVelocity((ballVx, ballVy))

    def __resetPaddles__(self):
        self.__leftPlayer__.getPaddle().setUpperLeftCorner((
            0,
            self.__arena__.getCenter()[1] - int(self.__leftPlayer__.getPaddle().getHeight() / 2)
        ))

        self.__rightPlayer__.getPaddle().setUpperLeftCorner((
            self.__arena__.getWidth() - self.__rightPlayer__.getPaddle().getWidth(),
            self.__arena__.getCenter()[1] - int(self.__rightPlayer__.getPaddle().getHeight() / 2)
        ))

    def __serveBall__(self):
        self.__ball__.setCenter(self.__arena__.getCenter())
        ballVx = self.__gameSpeed__ * self.__server__
        ballVy = randint(self.__gameSpeed__ * -1, self.__gameSpeed__)  # *-1 so ball can go either up or down
        self.__ball__.setVelocity((ballVx, ballVy))

        # When the left player serves (player 1), the ball is going to the
        # right so the X-Axis velocity direction is 1.
        # When the right player serves (player 2), the ball is going to the
        # left so the X-Axis velocity direction is -1.
        # We alternate between players
        self.__server__ = self.__server__ * -1

# region functions
def displayGameOver(frame, winner):
    TEXT_FONT = cv2.FONT_HERSHEY_COMPLEX
    TEXT_COLOR = (255, 255, 255)
    TEXT_THICKNESS = 1
    TEXT_SCALE = 1.0
    TEXT1 = "PLAYER 1 WINS"
    TEXT2 = "PLAYER 2 WINS"

    text = TEXT1 if winner == 1 else TEXT2

    frameCenterX = int((len(frame[0]) - 1) / 2)
    frameCenterY = int((len(frame) - 1) / 2)

    (textWidth, textHeight), _ = cv2.getTextSize(text, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)
    textX = frameCenterX - int(textWidth / 2)
    textY = frameCenterY - int(textHeight / 2)
    cv2.putText(frame, text, (textX, textY), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)
    return displayStartButton(frame, int(textHeight * 1.25))


def displayScoreboard(frame, leftPlayer, rightPlayer):
    TEXT_FONT = cv2.FONT_HERSHEY_COMPLEX
    TEXT_COLOR = (255, 255, 255)
    TEXT_THICKNESS = 1
    TEXT_SCALE = 1
    BOX_PADDING_FACTOR = 0.5
    HEADER_LPLAYER = "PLAYER1"
    HEADER_RPLAYER = "PLAYER2"

    frameCenterX = int((len(frame[0]) - 1) / 2)

    (lPlayerHeaderWidth, lPlayerHeaderHeight), _ = cv2.getTextSize(HEADER_LPLAYER, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)
    (lPlayerValueWidth, lPlayerValueHeight), _ = cv2.getTextSize(str(leftPlayer.getScore()), TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)
    (rPlayerHeaderWidth, scoreHeaderHeight), _ = cv2.getTextSize(HEADER_RPLAYER, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)
    (rPlayerValueWidth, scoreValueHeight), _ = cv2.getTextSize(str(rightPlayer.getScore()), TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)

    boxWidth = int(max([lPlayerHeaderWidth, lPlayerValueWidth, rPlayerHeaderWidth, rPlayerValueWidth]))
    boxHeight = int(max([lPlayerHeaderHeight + lPlayerValueHeight, scoreHeaderHeight + scoreValueHeight]))
    widthPadding = int(boxWidth * BOX_PADDING_FACTOR)
    heightPadding = int(boxHeight * BOX_PADDING_FACTOR)
    boxWidth = boxWidth + widthPadding
    boxHeight = boxHeight + heightPadding

    # Left player score
    cv2.rectangle(frame, (frameCenterX - boxWidth, 0), (frameCenterX, boxHeight), (255, 255, 255), 1)
    lPlayerHeaderX = frameCenterX - int(boxWidth / 2) - int(lPlayerHeaderWidth / 2)
    lPlayerHeaderY = lPlayerHeaderHeight + int(heightPadding/3)
    cv2.putText(frame, HEADER_LPLAYER, (lPlayerHeaderX, lPlayerHeaderY), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)
    lPlayerValueX = frameCenterX - int(boxWidth / 2) - int(lPlayerValueWidth / 2)
    lPlayerValueY = boxHeight - int(heightPadding/3)
    cv2.putText(frame, str(leftPlayer.getScore()), (lPlayerValueX, lPlayerValueY), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)

    # Right player score
    cv2.rectangle(frame, (frameCenterX, 0), (frameCenterX + boxWidth, boxHeight), (255, 255, 255), 1)
    scoreHeaderX = frameCenterX + int(boxWidth / 2) - int(rPlayerHeaderWidth / 2)
    scoreHeaderY = scoreHeaderHeight + int(heightPadding/3)
    cv2.putText(frame, HEADER_RPLAYER, (scoreHeaderX, scoreHeaderY), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)
    scoreValueX = frameCenterX + int(boxWidth / 2) - int(rPlayerValueWidth / 2)
    scoreValueY = boxHeight - int(heightPadding/3)
    cv2.putText(frame, str(rightPlayer.getScore()), (scoreValueX, scoreValueY), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)


def displayStartButton(frame, yOffset):
    TEXT_FONT = cv2.FONT_HERSHEY_COMPLEX
    TEXT_COLOR = (255, 255, 255)
    TEXT_THICKNESS = 1
    TEXT_SCALE = 1
    TEXT = "START"
    BOX_PADDING_FACTOR = 0.5

    frameCenterX = int((len(frame[0]) - 1) / 2)
    frameCenterY = int((len(frame) - 1) / 2) + yOffset

    (textWidth, textHeight), _ = cv2.getTextSize(TEXT, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)

    boxWidth = textWidth
    boxHeight = textHeight
    widthPadding = int(boxWidth * BOX_PADDING_FACTOR)
    heightPadding = int(boxHeight * BOX_PADDING_FACTOR)
    boxWidth = boxWidth + widthPadding
    boxHeight = boxHeight + heightPadding

    boxUpperLeftCorner = (frameCenterX - int(boxWidth / 2), frameCenterY - int(boxHeight / 2))
    boxLowerRightCorner = (frameCenterX - int(boxWidth / 2) + boxWidth, frameCenterY - int(boxHeight / 2) + boxHeight)

    cv2.rectangle(frame, boxUpperLeftCorner, boxLowerRightCorner, (255, 255, 255), 1)
    textX = frameCenterX - int(textWidth / 2)
    textY = frameCenterY + int(textHeight / 2)
    cv2.putText(frame, TEXT, (textX, textY), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)

    return (boxUpperLeftCorner, boxLowerRightCorner)


def isWithinRectangle(point, areaUpperLeftCorner, areaLowerRightCorner):
    if point[0] < areaUpperLeftCorner[0] or point[0] > areaLowerRightCorner[0]:
        return False
    if point[1] < areaUpperLeftCorner[1] or point[1] > areaLowerRightCorner[1]:
        return False
    return True


def getLeftPlayerIndex(screenCenterX, hands):
    for h in hands:
        index = h.getLandmarks(mph.HAND_REGION_INDEX_FINGER)[3]
        if index[0] < screenCenterX:
            return index
    return None


def getRightPlayerIndex(screenCenterX, hands):
    for h in hands:
        index = h.getLandmarks(mph.HAND_REGION_INDEX_FINGER)[3]
        if index[0] > screenCenterX:
            return index
    return None

# endregion

# Setup camera
cam = cv2.VideoCapture(CAM_ID, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_RES[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_RES[1])
cam.set(cv2.CAP_PROP_FPS, CAM_FPS)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(cv2.CAP_PROP_ZOOM, 100)

# Display camera settings dialog
#cam.set(cv2.CAP_PROP_SETTINGS, 1)

# Calculate actual frame dimensions. These dimensions may be different than
# our settings as the camera supports only a subset of possible resolutions.
frameDim = (int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(f'Actual camera resolution is "{frameDim[0]}x{frameDim[1]}."')

# Setup the window
cv2.namedWindow(WINDOW_CAMERA_NAME)
cv2.moveWindow(WINDOW_CAMERA_NAME, WINDOW_CAMERA_POS[0], WINDOW_CAMERA_POS[1])
cv2.resizeWindow(WINDOW_CAMERA_NAME, frameDim[0], frameDim[1])

# Setup media pipe
# https://google.github.io/mediapipe/solutions/hands.html
handDetection = mph.HandDetection(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=HAND_MIN_DETECTION_CONFIDENCE,
    min_tracking_confidence=HAND_MIN_TRACKING_CONFIDENCE
)

# Game components
arena = None
ball = None
leftPlayerPaddle = None
rightPlayerPaddle = None
leftPlayer = None
rightPlayer = None
engine = None
hotspot = None

# Read and display camera capture
print('Press "q" to quit...')

while True:
    _, frame = cam.read()

    # Flip frame horizontally so left is left when you look at the screen
    frame = cv2.flip(frame, 1)

    # Try to locate the index finger position
    hands = handDetection.detectHands(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    leftPlayerFingerCoordinates = getLeftPlayerIndex((frameDim[0] - 1) / 2, hands)
    rightPlayerFingerCoordinates = getRightPlayerIndex((frameDim[0] - 1) / 2, hands)

    # Add dark overlay
    darkOverlay = np.zeros((len(frame), len(frame[0]), 3), dtype=np.uint8)
    alpha = 0.6
    frame = cv2.addWeighted(frame, alpha, darkOverlay, 1 - alpha, 0.0)

    # Display start game / game over components based on the current game state
    if engine == None:
        hotspot = displayStartButton(frame, 0)
    elif engine.isGameOver():
        hotspot = displayGameOver(frame, 1 if leftPlayer.getScore() > rightPlayer.getScore() else 2)

    # If both an hotspot (button) is active and a finger was detected,
    # check if the finger coordinates match the hotspot location. If so,
    # handle the current state as a button click.
    if hotspot != None:
        hotspotUpperLeftCorner = hotspot[0]
        hotspotLowerRightCorner = hotspot[1]

        isHotspotActive = False
        if leftPlayerFingerCoordinates != None and isWithinRectangle(leftPlayerFingerCoordinates, hotspotUpperLeftCorner, hotspotLowerRightCorner):
            isHotspotActive = True
        elif rightPlayerFingerCoordinates != None and isWithinRectangle(rightPlayerFingerCoordinates, hotspotUpperLeftCorner, hotspotLowerRightCorner):
            isHotspotActive = True

        if isHotspotActive:
            arena = Arena(frameDim)
            ball = Ball(radius=int(frameDim[1] * 0.04), color=(0, 0, 255))
            leftPlayerPaddle = Paddle(width=int(frameDim[1] * 0.05), height=int(frameDim[1] * 0.2), color=(0, 255, 0))
            leftPlayer = Player(leftPlayerPaddle)
            rightPlayerPaddle = Paddle(width=int(frameDim[1] * 0.05), height=int(frameDim[1] * 0.2), color=(0, 255, 0))
            rightPlayer = Player(rightPlayerPaddle)
            engine = GameEngine(arena, ball, leftPlayer, rightPlayer, GAME_SPEED)
            hotspot = None

    # If game has been started
    if engine != None:
        if leftPlayerFingerCoordinates != None:
            engine.setPaddleYPosition(leftPlayer.getPaddle(), leftPlayerFingerCoordinates[1])
        if rightPlayerFingerCoordinates != None:
            engine.setPaddleYPosition(rightPlayer.getPaddle(), rightPlayerFingerCoordinates[1])

        engine.tick()
        displayScoreboard(frame, leftPlayer, rightPlayer)

        # Ball and paddle are not visible when the game is over
        if not engine.isGameOver():
            # Draw center dotted line
            for y in range(0, arena.getHeight(), 5):
                cv2.line(frame, (arena.getCenter()[0], y+1), (arena.getCenter()[0], y + 3), (255, 255, 255), 1, cv2.LINE_AA)
            # Draw ball
            cv2.circle(frame, ball.getCenter(), ball.getRadius(), ball.getColor(), ball.getThickness())
            # Draw left dotted line
            for y in range(0, arena.getHeight(), 5):
                cv2.line(frame, (leftPlayerPaddle.getWidth() - 1, y+1), (leftPlayerPaddle.getWidth(), y + 3), (255, 255, 255), 1, cv2.LINE_AA)
            # Draw left paddle
            cv2.rectangle(frame, leftPlayerPaddle.getUpperLeftCorner(), leftPlayerPaddle.getLowerRightCorner(), leftPlayerPaddle.getColor(), cv2.FILLED)
            # Draw right dotted line
            for y in range(0, arena.getHeight(), 5):
                cv2.line(frame, (arena.getWidth() - leftPlayerPaddle.getWidth() - 1, y+1), (arena.getWidth() - leftPlayerPaddle.getWidth(), y + 3), (255, 255, 255), 1, cv2.LINE_AA)
            # Draw right paddle
            cv2.rectangle(frame, rightPlayerPaddle.getUpperLeftCorner(), rightPlayerPaddle.getLowerRightCorner(), rightPlayerPaddle.getColor(), cv2.FILLED)

    cv2.imshow(WINDOW_CAMERA_NAME, frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Cleanup
print('Shutting down...')
cam.release()
cv2.destroyAllWindows()
print('Application ended')