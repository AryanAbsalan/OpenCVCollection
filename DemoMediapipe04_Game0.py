from handsdetection import HandsDrawing
import cv2
print(cv2.__version__)


# Size of the screen
width = 1100
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
paddle_height = 25
paddle_width = 125
paddle_color = (255, 0, 0)

# Game params
ball_x = int(width/2)
ball_y = int(height/2)
ball_radius = 25
ball_color = (255, 0, 0)
deltaX = 10
deltaY = 10
score = 0
lives = 5
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Loading camera
while True:
    # Camera frame
    ignore, frame = camera.read()

    cv2.circle(frame, (ball_x, ball_y), ball_radius, ball_color, -1)
    cv2.putText(frame, str(score), (25, int(6*paddle_height)),
                font, 4, paddle_color, 3)
    cv2.putText(frame, str(lives), (width-125, int(6*paddle_height)),
                font, 4, paddle_color, 3)

    # Finding hand land marks
    hands_results, handsType_ = hands_finder.find_land_marks(
        frame, width, height)

    # Creating paddle
    for hand in hands_results:
        paddle_width = paddle_width
        cv2.rectangle(frame,
                      (int(hand[8][0]-paddle_width), 0),
                      (int(hand[8][0]+paddle_width),
                       paddle_height),
                      paddle_color,
                      Thickness)

    # Game conditions
    left_ball = ball_x-ball_radius
    right_ball = ball_x+ball_radius
    top_ball = ball_y-ball_radius
    buttom_ball = ball_y+ball_radius

    if left_ball <= 0 or right_ball >= width:
        deltaX = deltaX*(-1)

    if buttom_ball >= height:
        deltaY = deltaY*(-1)

    # when ball is between corners of  paddle : ball hit paddle
    if top_ball <= paddle_height:
        if ball_x >= (int(hand[8][0]-paddle_width/2)) or ball_x <= (int(hand[8][0]+paddle_width/2)):
            deltaY = deltaY*(-1)
            score += 1
            # Speeding Up!
            # if score==4 or score==8 or score==12:
            #     deltaX=deltaX*3
            #     deltaY=deltaY*3
            if score == 4:
                deltaX = deltaX*3
                deltaY = deltaY*3
            if score > 12:
                Radius = 20
                ball_color = (0, 0, 255)
            if score > 16:
                Radius = 30
                ball_color = (0, 255, 0)
            # if score>25:
            #     cv2.waitKey(3000)
            #     break

        # when ball does NOT hit paddle: ball out!
        else:
            ball_x = int(width/2)
            ball_y = int(height/2)
            lives = lives-1

    # Moving ball
    ball_x = ball_x+deltaX
    ball_y = ball_y+deltaY

    # Showing frame
    cv2.imshow('GameWin', frame)
    cv2.moveWindow('GameWin', Xpos, Ypos)

    if lives == 0:
        cv2.putText(frame, 'Game Over!', (ball_x, ball_y),
                    font, 4, paddle_color, 3)
        cv2.waitKey(3000)
        break

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
