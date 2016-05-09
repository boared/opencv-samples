#!/usr/bin/python3
# This sample loads an image given as argument and displays it.
# Usage:
# python3 1_load_image.py <image_path>
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2014 Eder Perez
import cv2
import numpy as np
import sys

arglist = list(sys.argv)

if len(arglist) != 2:
    print('')
    print('Usage: python3 1_load_image.py IMAGE_PATH')
    print('')
    exit()

path = arglist[1]
print('Loading image {0}'.format(path))

# Reads an image the way it is
img = cv2.imread( path, cv2.IMREAD_UNCHANGED )

# Creates a resizeble window
cv2.namedWindow('Image Display', cv2.WINDOW_NORMAL)

# Populates the created window with the loaded image
cv2.imshow('Image Display', img)

# Waits for ESC to exit
k = cv2.waitKey(0) & 0xFF # 0xFF in case of a 64-bit machine
if k == 27:
    cv2.destroyAllWindows()

