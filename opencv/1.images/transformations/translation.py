import cv2 as cv
import numpy as np

# x : Right
# -x : Left
# y : Down
# -y : Up
def translate(img, x, y):
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    width = img.shape[1]
    height = img.shape[0]

    dimensions = (width, height)
    return cv.warpAffine(img, translation_matrix, dimensions)

# Read the image as matrix of pixels
image = cv.imread('nature.png')
image = cv.resize(image, (1000, 800))

# Display the image in new window
cv.imshow('Nature', image)
cv.imshow('Image shifted 150 pixels right and 100 pixels down', translate(image, 150, 100))
cv.imshow('Image shifted 150 pixels left and 200 pixels up', translate(image, -150, -200))

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()