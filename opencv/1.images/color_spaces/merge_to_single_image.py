import cv2 as cv
import numpy as np

# Read the image as matrix of pixels
image = cv.imread('flowers.png')
#image = cv.resize(image, (800, 800))

# Default color space is BGR in OpenCV
splits = cv.split(image)

blue_channel_image = splits[0]
green_channel_image = splits[1]
red_channel_image = splits[2]

merged_image = cv.merge([blue_channel_image, green_channel_image, red_channel_image])

cv.imshow('image', image)
cv.imshow('merged_image', merged_image)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()