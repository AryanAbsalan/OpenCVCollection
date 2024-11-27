import cv2

image = cv2.imread("C:\Demo\wind.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

cv2.imshow("Image", image)
cv2.waitKey(0)
