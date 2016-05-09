#!/usr/bin/python3
# This sample shows how trackbars works.
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2016 Eder Perez
import cv2
import numpy as np

# Callback for nothing
def nothing(x):
    pass

windowName = 'Trackbar'

# Create a black image window
img = np.zeros((480, 640, 3), np.uint8)
cv2.namedWindow(windowName)

# Create trackbars for color change
cv2.createTrackbar('R', windowName, 0, 255, nothing)
cv2.createTrackbar('G', windowName, 0, 255, nothing)
cv2.createTrackbar('B', windowName, 0, 255, nothing)

while (True):
    cv2.imshow(windowName, img)

    if ((cv2.waitKey(1) & 0xFF) == 27):
        break

    # Get current positions of four trackbars
    r = cv2.getTrackbarPos('R', windowName)
    g = cv2.getTrackbarPos('G', windowName)
    b = cv2.getTrackbarPos('B', windowName)
    img[:] = [b, g, r]

cv2.destroyAllWindows()

