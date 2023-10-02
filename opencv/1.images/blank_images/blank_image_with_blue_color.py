import cv2 as cv
import numpy as np
import random

# Define the dimensions of the blank image
width, height = 1000, 500

# Create a blank image filled with random colors
random_image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with random colors
for y in range(height):
    for x in range(width):
        # Set the pixel color at (x, y)
        random_image[y, x] = [255, 0, 0]

# Display the random color image
cv.imshow('Random Color Image', random_image)
cv.waitKey(0)
cv.destroyAllWindows()
