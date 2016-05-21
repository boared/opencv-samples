#!/usr/bin/python3
# This sample tracks an object based on its HSV color.
# Usage: python3 8_object_tracking_hsv.py VIDEO_PATH
#    or: python3 8_object_tracking_hsv.py CAMERA_INDEX
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2016 Eder Perez
import cv2
import numpy as np
import sys

arglist = list(sys.argv)

if len(arglist) != 2:
    print('')
    print('Usage: python3 8_object_tracking_hsv.py VIDEO_PATH')
    print('   or: python3 8_object_tracking_hsv.py CAMERA_INDEX')
    print('')
    exit()

path = arglist[1]
print('Starting capture from {0}'.format(path))

# Refresh rate
fps = 1

# Check if path is a camera index or video file
try:
   path = int(path)
except ValueError:
    fps = 25 # 25ms of refresh rate for video files

# Creates a video capture object
cap = cv2.VideoCapture(path)

if (not cap.isOpened()):
    print('Failed to open video.')
    exit()

print('Frame size: {0}x{1}'.format( int(cap.get(3)), int(cap.get(4))))

windowFrame = 'Frame'
windowMask = 'Mask'
windowHSV = 'HSV'
windowTracking = 'Tracking'

# Creates a resizable window
cv2.namedWindow(windowFrame, cv2.WINDOW_NORMAL)
cv2.namedWindow(windowMask, cv2.WINDOW_NORMAL)
cv2.namedWindow(windowTracking, cv2.WINDOW_NORMAL)

# Starts capture frame by frame
frameCount = 0
while (cap.isOpened):
    # Get frame and status
    ret, frame = cap.read()
    frameCount += 1

    if ret == False:
        print('Frame {0} read error.'.format(frameCount))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_clr = hsv
    h_clr[:,:,1] = 255
    h_clr[:,:,2] = 255
    h_clr = cv2.cvtColor(h_clr, cv2.COLOR_HSV2BGR)

    # Define range of blue color in HSV
    lower_red = np.array([50, 50, 50])
    upper_red = np.array([70, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    tracking = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow(windowFrame, frame)
    cv2.imshow(windowMask, mask)
    cv2.imshow(windowHSV, h_clr)
    cv2.imshow(windowTracking, tracking)

    # Waits for ESC to stop
    if cv2.waitKey(fps) & 0xFF == 27: # 0xFF in case of a 64-bit machine
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
