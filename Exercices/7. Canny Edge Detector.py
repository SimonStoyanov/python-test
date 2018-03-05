import numpy as np
import cv2

def GetMaxElementMatrix(matrix):
    val = matrix[0,0]
    for array in matrix:
        for element in array:
            if val<element:
                val=element
    return val

def trackbarCallback(x):
    pass

# Load a color image in grayscale
filename = 'Ex_Images/ricalin.png'
cv2.namedWindow('OpenCV: Canny')
img = cv2.imread(filename, 0)

# Trackbars to select min and max
cv2.createTrackbar('Min', 'OpenCV: Canny', 0, GetMaxElementMatrix(img), trackbarCallback)
cv2.createTrackbar('Max', 'OpenCV: Canny', 0, GetMaxElementMatrix(img), trackbarCallback)

while True:
    min_ = cv2.getTrackbarPos('Min', 'OpenCV: Canny')
    max_ = cv2.getTrackbarPos('Max', 'OpenCV: Canny')

    # Apply the Canny edge detector
    edges = cv2.Canny(img, min_, max_)
    cv2.imshow('OpenCV: Canny', edges)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
