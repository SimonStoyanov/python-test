import cv2
import numpy as np

def trackbarCallback(x):
    # Do nothing
    pass

# Create a black image and a window
img =  np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Color Palette')

# Create trackbar for color change
cv2.createTrackbar('R', 'Color Palette', 0, 255, trackbarCallback)
cv2.createTrackbar('G', 'Color Palette', 0, 255, trackbarCallback)
cv2.createTrackbar('B', 'Color Palette', 0, 255, trackbarCallback)

while True:
    # Get values of the trackbars
    r = cv2.getTrackbarPos('R', 'Color Palette')
    g = cv2.getTrackbarPos('G', 'Color Palette')
    b = cv2.getTrackbarPos('B', 'Color Palette')

    img[:] = [b, g, r]
    cv2.imshow('Color Palette', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
