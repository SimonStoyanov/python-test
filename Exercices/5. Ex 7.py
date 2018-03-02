import cv2
import numpy as np

#10 elements array
array = np.array([1,2,3,4,5,6,7,8,9,10])


print array[4]
matrix = np.array([1,2,3,4,5,
                                6,7,8,9,10,
                                11,12,13,14,15,
                                16,17,18,19,20,
                                21,22,23,24,25])
matrix.shape = (5,5)
print matrix[2,3];
print
print matrix.shape[0]/2
print

def GetMaxElementArray(array):
    val = 0
    for element in array:
        if val<element:
            val=element
    return val

def GetMinElementMatrix(matrix):
    val = matrix[0,0]
    for array in matrix:
        for element in array:
            if val>element:
                val=element
    return val

def GetMaxElementMatrix(matrix):
    val = matrix[0,0]
    for array in matrix:
        for element in array:
            if val<element:
                val=element
    return val

def PrintMatrix(matrix):
    cols, rows = matrix.shape
    for y in range(0,cols):
        for x in range(0, rows):
            print matrix[y,x]
        print

img = cv2.imread('Ex_Images/ricalin.png',0)

kernel = np.array(3*[3*[1.0/9.0]])

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

def ApplyKernel(img_to_apply, kernel):    
    max_val = GetMaxElementMatrix(img_to_apply)
    cols, rows = img_to_apply.shape
    new_img = img_to_apply.copy()
    for i in range(0,cols):
        for j in range(0,rows):
            new_img[i][j] = getFilteredValue(new_img,kernel,i,j)
    max_val = GetMaxElementMatrix(new_img)
    for i in range(0,cols):
        for j in range(0,rows):
            new_img[i][j] = strechValue(new_img[i][j], max_val)

    return new_img

kernel1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel2 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
print kernel1

cv2.imshow('Normal', img)
cv2.imshow('Kernel 1', ApplyKernel(img, kernel1))
cv2.imshow('Kernel 2', ApplyKernel(img, kernel2))

k = cv2.waitKey(0)
