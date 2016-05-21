#!/usr/bin/python3
# This sample show handles an image in HSV color space.
# Usage:
# python3 7_hsv_image.py
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2016 Eder Perez
import cv2
import numpy as np

# Callback for nothing (used in Trackbar)
def nothing(x):
    pass

# Create an empty image
hsv = np.zeros((480, 640, 3), np.uint8)

# Create a window
windowHSV = 'HSV'
cv2.namedWindow(windowHSV)

# Create trackbars for color change
cv2.createTrackbar('H', windowHSV, 0, 179, nothing)
cv2.createTrackbar('S', windowHSV, 0, 255, nothing)
cv2.createTrackbar('V', windowHSV, 0, 255, nothing)

cv2.setTrackbarPos('H', windowHSV, 179)
cv2.setTrackbarPos('S', windowHSV, 255)
cv2.setTrackbarPos('V', windowHSV, 255)
while (True):
    H = cv2.getTrackbarPos('H', windowHSV)
    S = cv2.getTrackbarPos('S', windowHSV)
    V = cv2.getTrackbarPos('V', windowHSV)

    hsv[:, :, 0] = H
    hsv[:, :, 1] = S
    hsv[:, :, 2] = V

    cv2.imshow(windowHSV, cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))

    if (cv2.waitKey(1) & 0xFF == 27):
        break

cv2.destroyAllWindows()
