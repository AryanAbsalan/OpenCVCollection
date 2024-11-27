class FaceDrawing():
    import cv2
    import mediapipe as mp 
    def __init__(self):
        self.myFace=self.mp.solutions.face_detection.FaceDetection()
    def find_land_marks(self,frame,width,height):
        frameRGB=self.cv2.cvtColor(frame,self.cv2.COLOR_BGR2RGB)
        results=self.myFace.process(frameRGB)
        faceBoundBoxs=[]
        if results.detections != None:
            for face in results.detections:
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs