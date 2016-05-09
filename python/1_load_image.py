#!/usr/bin/python3
# This sample loads an image given as argument and displays it.
# Usage:
# python3 1_load_image.py <image_path>
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2014 Eder de Almeida Perez
import cv2
import numpy as np
import sys

arglist = list(sys.argv)

if len(arglist) != 2:
    print('Usage:')
    print('python3 1_load_image.py <image_path>')
    exit()

path = arglist[1]
print('Loading image {0}'.format(path))
img = cv2.imread( path, cv2.IMREAD_UNCHANGED )
cv2.namedWindow('imgDisplay', cv2.WINDOW_NORMAL)
cv2.imshow('imgDisplay', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

