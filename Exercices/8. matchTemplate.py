import numpy as np
import cv2

img = cv2.imread('Ex_Images/ricalin.png', 0)
img2 = cv2.imread('Ex_Images/ricalin-eye2.png', 0)
match =  cv2.matchTemplate(img, img2, 5)

while True:
    cv2.imshow('Match', match)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
