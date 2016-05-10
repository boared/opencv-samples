#!/usr/bin/python3
# This sample shows how to access image pixels.
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2016 Eder Perez
import cv2
import sys

arglist = list(sys.argv)

if len(arglist) != 2:
    print('')
    print('Usage: python3 4_image_access.py IMAGE_PATH')
    print('')
    exit()

path = arglist[1]
print(path)

# Load image
img = cv2.imread( path )

# Access image BGR pixel (slow way)
px = img[0,0]
print(px)

# Access image red pixel (slow way)
px = img[0, 0, 2]
print(px)

# Modify pixel value (slow way)
img[0, 0] = [127, 127, 127]
print(img[0, 0])

# Access image BGR pixel (better way)
b = img.item(10, 10, 0)
g = img.item(10, 10, 1)
r = img.item(10, 10, 2)
print([b, g, r])

# Image properties (height, width and channels)
print(img.shape)

# Image number of pixels
channels = 1
if len(img.shape) == 3: channels = img.shape[2]
print( int(img.size / channels) )

# Image type
print(img.dtype)

# ROI (Region Of Interest)
roi = img[10:15, 5:10] # ROI from lines 10 to 15 and columns from 5 to 10

# Split image channels
b, g, r = cv2.split(img)  # Slower way
b = img[:, :, 0]  # Faster way

# Set all blue and green values to zero
img[:, :, 0] = 0
img[:, :, 1] = 0

# Merge image channels
img = cv2.merge((r, g, b))
