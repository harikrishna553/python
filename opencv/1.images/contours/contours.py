import cv2 as cv
import numpy as np

image = cv.imread('bear.jpeg')
cv.imshow('Puppies', image)

# Convert this image to grayscale
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale_image', grayscale_image)

blurred_image = cv.GaussianBlur(grayscale_image, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blurred_image', blurred_image)

# Define the structuring element (square in this case)
kernel = np.ones((3, 3), np.uint8)

# Perform dilation
dilated_image = cv.dilate(blurred_image, kernel, iterations=1)
cv.imshow('dilated_image', dilated_image)

# Get the edges
canny = cv.Canny(dilated_image, 125, 175)
cv.imshow('canny edges', canny)

# Get the contours, contours are returned as a list
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Total contours are  : {len(contours)}')

max_length = -1
contour_index = -1
max_contour_index = contour_index

for contour in range(len(contours)):
    contour_index = contour_index + 1



blank_image = np.zeros(image.shape, dtype='uint8')

# Draw the contours on blank image
cv.drawContours(blank_image, contours, -1, (0, 255, 0), thickness=1)
cv.imshow('contours on blank_image', blank_image)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()