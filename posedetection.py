class PoseDrawing:
    import cv2
    import mediapipe as mp
    
    def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
        self.myPose=self.mp.solutions.pose.Pose(still,upperBody,smoothData,tol1,tol2)
    def find_land_marks(self,frame,width, height):
        frameRGB=self.cv2.cvtColor(frame,self.cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks