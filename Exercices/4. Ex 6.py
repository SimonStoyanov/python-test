import cv2
import numpy as np

def erodeNtimes(n, img):
    return cv2.erode(img, kernel, iterations = n)

def dilateNtimes(n, img):
    return cv2.dilate(img, kernel, iterations = n)

filename = 'Ex_Images/Edges_Fry.jpg'

img = cv2.imread(filename, 0)
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(img, kernel, iterations = 5)

cv2.imshow(filename, img)
cv2.imshow('Dilate '+str(filename), dilation)
cv2.imshow('Dilate n', dilateNtimes(1, img))
cv2.imshow('Erode n', erodeNtimes(5, dilation))

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
