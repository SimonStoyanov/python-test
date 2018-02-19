import numpy as np
import cv2

# EX1. Use numpy to:
#       Create an array of 10 elements
arr110 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print arr110

#       Create a matrix of 5x5
mat55 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]])
print mat55

#       Implement 2 functions GetMaxElemInArray and GetMinElemInMatrix
def GetMaxElemInArray(array):
    max_val = 0
    for element in array:
        if (element > max_val):
            max_val = element
    return max_val

def GetMinElemInMatrix(matrix):
    min_val = 99
    for array in matrix:
        for element in array:
            if (element < min_val):
               min_val = element
    return min_val
    
print GetMaxElemInArray(arr110)
print GetMinElemInMatrix(mat55)

# EX2. Create a function printMatrix(...) that given a matrix prints it on the screen
def PrintMatrix(matrix):
    cols, rows = matrix.shape
    for i in range(0, rows):
        for j in range(0, cols):
            print matrix[i][j],
        print

PrintMatrix(mat55)

# EX3. Invert an image
#       Load an image in greyscale
#       Create the function invert that given a greyscale image, inverts its values --> black to white and viceversa
#       Show the original greyscale image and the inverted one
def InvertImage(image):
    # return cv2.bitwise_not(image)
    # return (255 - image)
    

img = cv2.imread('Ex_Images/snek.jpg', 0)
cv2.imshow('Snek', img)

img_inv = InvertImage(img)
cv2.imshow('Snek Inv', img_inv)


k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
    
