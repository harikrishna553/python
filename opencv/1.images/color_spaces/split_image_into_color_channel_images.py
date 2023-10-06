import cv2 as cv
import numpy as np

# Read the image as matrix of pixels
image = cv.imread('flowers.png')
image = cv.resize(image, (800, 800))

# Default color space is BGR in OpenCV
splits = cv.split(image)

blue_channel_image = splits[0]
green_channel_image = splits[1]
red_channel_image = splits[1]

# Let's create a blank image use it in the merging process
blank_image = np.zeros(image.shape[:2], dtype='uint8')

blue = cv.merge([blue_channel_image, blank_image, blank_image])
green = cv.merge([blank_image, green_channel_image, blank_image])
red = cv.merge([blank_image, blank_image, red_channel_image])

cv.imshow('image', image)
cv.imshow('blue', blue)
cv.imshow('red', red)
cv.imshow('green', green)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()