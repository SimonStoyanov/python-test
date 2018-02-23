import cv2
import numpy as np

# EX 4. Color channels
#   Load a color image (use a relatively small one)
img = cv2.imread('Ex_Images/color-palette.jpg', 1)
cv2.imshow('Color Palette', img)

#   Store into three RGB images each color channel of the original one (the red channel of
#   the first image will be the red channel of the original one, while the green and blue
#   channels will be set to zero. Do the same with the second image (green) and the third
#   one (blue)).
red = img.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0

green = img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = img.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0
        
#   Show the three images and the original one on the screen.
cv2.imshow('Red', red)
cv2.imshow('Green', green)
cv2.imshow('Blue', blue)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
