class HandsDrawing:
    import cv2
    import mediapipe as mp

    myHands=[]
    handsType=[]

    def __init__(self,max_hands=2,de_confidence=.5,tr_confidence=.5):
        self.hands = self.mp.solutions.hands.Hands(static_image_mode=False,
                                        max_num_hands=max_hands,
                                        model_complexity=1,
                                        min_detection_confidence=de_confidence,
                                        min_tracking_confidence=tr_confidence)
    
    def find_land_marks(self,frame,width,height):
        frameBGR = self.cv2.cvtColor(frame, self.cv2.COLOR_RGB2BGR)
        hands_results = self.hands.process(frameBGR)
        myHand = []
        
        # finding left and right hand label
        if hands_results.multi_hand_landmarks != None:
            for hand in hands_results.multi_handedness:
                handType = hand.classification[0].label
                self.handsType.append(handType)

            # finding hand land marks, left and right hand
            for handLandMarks in hands_results.multi_hand_landmarks:
                for handLandMark in handLandMarks.landmark:
                    myHand.append((int(handLandMark.x*width),int(handLandMark.y*height)))
                self.myHands.append(myHand)
        
        return self.myHands, self.handsType
        