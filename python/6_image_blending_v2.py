#!/usr/bin/python3
# This sample realize image blending on 2 images.
# Operation:
#       alpha*img1 + beta*img2 + gamma
# Usage:
# python3 6_image_blending_v2.py <image1_path> <image2_path>
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2016 Eder Perez
import cv2
import numpy as np
import sys

# Callback for nothing (used in Trackbar)
def nothing(x):
    pass

arglist = list(sys.argv)

if len(arglist) != 3:
    print('')
    print('Usage: python3 6_image_blending_v2.py IMAGE_1_PATH IMAGE_2_PATH')
    print('')
    exit()

path1 = arglist[1]
path2 = arglist[2]

# Read images the way they are
img1 = cv2.imread( path1, cv2.IMREAD_UNCHANGED )
print('Loading image {0} {1}'.format(path1, img1.shape))


img2 = cv2.imread( path2, cv2.IMREAD_UNCHANGED )
print('Loading image {0} {1}'.format(path2, img2.shape))


# Create a window
windowName = 'Image Blending'
cv2.namedWindow(windowName)

# Create trackbars for color change
cv2.createTrackbar('alpha', windowName, 0, 100, nothing)
cv2.createTrackbar('beta', windowName, 0, 100, nothing)
cv2.createTrackbar('gamma', windowName, 0, 255, nothing)

while (True):
    # alpha*img1 + beta*img2 + gamma
    alpha = cv2.getTrackbarPos('alpha', windowName)
    beta = cv2.getTrackbarPos('beta', windowName)
    gamma = cv2.getTrackbarPos('gamma', windowName)
    blended = cv2.addWeighted(img1, alpha/100, img2, beta/100, gamma)
    cv2.imshow(windowName, blended)

    if ((cv2.waitKey(1) & 0xFF) == 27):
        break

cv2.destroyAllWindows()
