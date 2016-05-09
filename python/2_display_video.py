#!/usr/bin/python3
# This sample captures video from camera or file.
# Usage: python3 2_display_video.py VIDEO_PATH
#    or: python3 2_display_video.py CAMERA_INDEX
#
# Licensed under the MIT License (MIT)
# Copyright (c) 2016 Eder Perez
import cv2
import numpy as np
import sys

arglist = list(sys.argv)

if len(arglist) != 2:
    print('')
    print('Usage: python3 2_display_video.py VIDEO_PATH')
    print('   or: python3 2_display_video.py CAMERA_INDEX')
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

windowName = 'Video Display'

# Creates a resizeble window
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# Starts capture frame by frame
frameCount = 0
while (cap.isOpened):
    # Get frame and status
    ret, frame = cap.read()
    frameCount += 1
    
    if ret == False:
        print('Frame {0} read error.'.format(frameCount))

    # Populates the created window with the loaded image
    cv2.imshow(windowName, frame)

    # Waits for ESC to stop
    if cv2.waitKey(fps) & 0xFF == 27: # 0xFF in case of a 64-bit machine
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

