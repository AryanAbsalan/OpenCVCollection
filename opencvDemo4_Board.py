
import cv2
import numpy as np

# size of board and numbers of squares
boardSize = int(input('Size of the board in pixel? '))
squares = int(input('Size of the squares in pixel? '))
squareSize = int(boardSize/squares)

while True:
    # board sise : 400 x 400 with 3 color:BGR
    frame = np.zeros([boardSize, boardSize, 3], dtype=np.uint8)
    # first block is black
    darkColorBox = True

    for row in range(0, squareSize):
        for col in range(0, squareSize):
            # block size: squares x squares
            fromRow = row * squares
            toRow = fromRow + squares
            fromCol = col * squares
            toCol = fromCol + squares
            # main colors
            darkcolor = (0, 0, 0)
            brightcolor = (0, 0, 100)

            # black color
            if darkColorBox:
                frame[fromRow: toRow, fromCol:toCol] = darkcolor
                frame[fromRow + 10 : toRow + 10 , fromCol + 10 :toCol + 10] = (0,0,66)
            # red color
            if not darkColorBox:
                frame[fromRow: toRow, fromCol:toCol] = brightcolor
                frame[fromRow + 10 : toRow + 10 , fromCol + 10 :toCol + 10] = (0,0,77)

            # changing color for each column
            darkColorBox = not darkColorBox
        # changing color for each row
        darkColorBox = not darkColorBox

    cv2.imshow('Board', frame)
    cv2.moveWindow('Board', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
