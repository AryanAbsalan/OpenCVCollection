import cv2
from cv2 import rectangle

width = 820
height = 640

while True:
    image = cv2.imread("C:\Demo\wind.png")

    if image is not None:
        # Rectangle variable
        recUpperCorner = (400,120)
        recLowerCorner = (800,160)
        recColor = (0,122,0)
        recThickness = 2

        # Circle variable 
        cirCenter = (int(width/2), int(height/2))
        cirRadius = 100 # pix
        cirColor = (122,0,0)
        CirThickness = 2

        # Text variable 
        tText = "Just a text..."
        tPosition = (50,120)
        tFontFace1 = cv2.FONT_HERSHEY_COMPLEX
        tFontFace2 = cv2.FONT_HERSHEY_COMPLEX_SMALL
        tFontFace3 = cv2.FONT_HERSHEY_DUPLEX
        tFontFace4 = cv2.FONT_HERSHEY_PLAIN
        tFontFace5 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        tFontFace6 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        tFontFace7 = cv2.FONT_HERSHEY_SIMPLEX
        tFontFace8 = cv2.FONT_HERSHEY_TRIPLEX
        tFontFace9 = cv2.FONT_ITALIC
        tFontScale=1
        tColor=(0,0,122)
        tThickness = 2

        cv2.rectangle(image,recUpperCorner,recLowerCorner,recColor,recThickness)
        cv2.circle(image,cirCenter,cirRadius,cirColor,CirThickness)
        
        cv2.putText(image,tText,tPosition,tFontFace1,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(60,160),tFontFace2,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(70,200),tFontFace3,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(80,240),tFontFace4,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(90,280),tFontFace5,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(100,320),tFontFace6,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(110,360),tFontFace7,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(120,400),tFontFace8,tFontScale,tColor,tThickness)
        cv2.putText(image,tText,(130,440),tFontFace9,tFontScale,tColor,tThickness)

        # Showing the image at position 0,0
        cv2.imshow('Vision1', image) 
        cv2.moveWindow('Vision1', 0,0)
        
        key = cv2.waitKey(1) 
        if key == ord('q'):
            break
    else:
        print ("Image is None")
        break

# Closing all windows
cv2.destroyAllWindows()
