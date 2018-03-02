import cv2
import numpy as np

img = cv2.imread('Ex_Images/ricalin.png', 1)
cv2.imshow('Go To Gulag', img)

# Ex 5. Linear Filters
kernel = np.array(3*[3*[1.0/9.0]])
print kernel
print img

def GetMaxElementMatrix(matrix):
    val = matrix[0,0]
    for array in matrix:
        for element in array:
            if val<element:
                val=element
    return val

def getFilteredValue(img, kernel, i, j):
    value = 0
    imgx,imgy = img.shape
    kx,ky = kernel.shape
    for ix in range (-(kx/2),kx/2):
        for iy in range (-(ky/2),ky/2):
            if(i+ix>=0 and i+ix < imgx and j+iy >=0 and j+ iy < imgy):
                value = value + img[i+ix][j+iy]*kernel[ix][iy]
    return value

def strechValue(value, maxV, strechValue = 255):
    return value * strechValue / maxV

fimg = img.copy()

max_val = GetMaxElementMatrix(img)
print max_val

cols, rows = img.shape
for i in range(0,cols):
    for j in range(0,rows):
        fimg[i][j] = getFilteredValue(fimg,kernel,i,j)

max_val = GetMaxElementMatrix(fimg)

for i in range(0,cols):
    for j in range(0,rows):
        fimg[i][j] = strechValue(fimg[i][j], max_val)

cv2.imshow('Blur', fimg)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
