import cv2
import numpy as np

def erodeNtimes(n, img):
    return cv2.erode(img, kernel, iterations = n)

def dilateNtimes(n, img):
    return cv2.dilate(img, kernel, iterations = n)

filename = 'Ex_Images/Edges_Fry.jpg'
filename2 = 'Ex_Images/SP_Noise_marker1.jpg'

img = cv2.imread(filename, 0)
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(img, kernel, iterations = 5)

cv2.imshow(filename, img)
cv2.imshow('Dilate '+str(filename), dilation)
cv2.imshow('Erode', erodeNtimes(5, dilation))

img2 = cv2.imread(filename2, 0)
cv2.imshow(filename2, img2)
erosion = erodeNtimes(1, img2)
cv2.imshow('Eroded original', erosion)
cv2.imshow('Dilated eroded', dilateNtimes(3, erosion))


k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
