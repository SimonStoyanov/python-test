import cv2
import numpy as np

img = cv2.imread('Ex_Images/ricalin.png', 1)
cv2.imshow('Go To Gulag', img)

# Ex 5. Linear Filters
kernel = np.array(3*[3*[1.0/9.0]])
print kernel
print img
img_shape = img.shape

for x in img_shape[0]:
    for y in img_shape[1]:
        up_left = img[x - 1][y - 1]
        up = img[x][y- 1]
        up_right = img[x + 1][y - 1]
        left = img[x -1][y]
        center = img[x][y]
        right = img[x + 1][y]
        down_left = img[x - 1][y + 1]
        down = img[x][y + 1]
        down_right = img[x + 1][y + 1]

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
