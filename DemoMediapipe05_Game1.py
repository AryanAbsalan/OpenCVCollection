import cv2
print(cv2.__version__)

from handsdetection import HandsDrawing


# Size of the screen
width = 1120
height = 660

# Camera settings
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

Xpos = 0                  # Default value for x position of frame window
Ypos = 0                  # Default value for y position of frame window

hands_finder = HandsDrawing()

# Circle params
Radius = 10
Red = (0, 0, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
Thickness = -1

# Paddle params
paddle_width=25
paddle_height=150
paddle_color=(255,0,0)

# Game params
ball_radius=25
ball_color=(255,0,0)
ball_x=int(width/2)
ball_y=int(height/2)
deltaX=5
deltaY=5

font= cv2.FONT_HERSHEY_COMPLEX_SMALL

y_left_tip=0
y_right_tip=0

score_left=0
score_right=0


# Loading camera
while True:
    # Camera frame
    ignore, frame = camera.read()
    frame=cv2.resize(frame,(width,height))

    cv2.circle(frame,(ball_x,ball_y),ball_radius,ball_color,-1)
    cv2.putText(frame,str(score_left),(50,125),font,4,Black,3)
    cv2.putText(frame,str(score_right),(width-150,125),font,4,Black,3)

    # Finding hand land marks and hand type: left or right
    hands_data, handsType = hands_finder.find_land_marks(frame,width,height)

    # Creating paddle
    for hand , handType in zip(hands_data,handsType):
        y_left_tip=hand[8][1]
        print(y_left_tip)
        if handType=='Left':
            y_left_tip=hand[8][1]
            #cv2.circle(frame, y_left_tip, radius = Radius, color = Red, thickness = Thickness)
        if handType=='Right':
            y_right_tip=hand[8][1]
            #cv2.circle(frame,center=(hand[8],[0]), radius = Radius, color = Red, thickness = Thickness)

    cv2.rectangle(frame,(0,int(y_left_tip-paddle_height/2)),(paddle_width,int(y_left_tip+paddle_height/2)),paddle_color,Thickness)
    cv2.rectangle(frame,(width-paddle_width,int(y_right_tip-paddle_height/2)),(width,int(y_right_tip+paddle_height/2)),paddle_color,Thickness)
    
    # Game conditions
    left_ball=ball_x-ball_radius
    right_ball=ball_x+ball_radius
    top_ball=ball_y-ball_radius
    buttom_ball=ball_y+ball_radius

    # Ball out from top 
    if top_ball<=0 :
        deltaY=deltaY*(-1)

    # Ball out from buttom 
    if buttom_ball>=height:
        deltaY=deltaY*(-1)

    # Ball out from left
    if left_ball<=paddle_width:
        # When ball hit the left paddle
        if Ypos>=int(y_left_tip-paddle_height/2) and Ypos<=int(y_left_tip+paddle_height/2):
            deltaX=deltaX*(-1)
        else:
            ball_x=int(width/2)
            ball_y=int(height/2)
            score_right = score_right+1

    # Ball out from right
    if right_ball>=width-paddle_width:
        # When ball hit the right paddle
        if Ypos>=int(y_right_tip-paddle_height/2) and Ypos<=int(y_right_tip+paddle_height/2):
            deltaX=deltaX*(-1)
        else:
            ball_x=int(width/2)
            ball_y=int(height/2)
            score_left = score_left+1

    # Moving ball
    ball_x=ball_x+deltaX
    ball_y=ball_y+deltaY
        
    # Showing frame
    cv2.imshow('GameWin', frame)
    cv2.moveWindow('GameWin', Xpos, Ypos)

    # End of the Game
    if score_left+score_right>=30:
        cv2.putText(frame,'Game Over!',(ball_x,ball_y),font,4,Black,3)
        cv2.waitKey(3000)
        break
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
