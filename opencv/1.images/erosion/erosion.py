import cv2
import cv2 as cv
import numpy as np

def resize_frame(frame, scale_width=0.5, scale_height=0.5):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    new_dimensions = (width, height)
    return cv.resize(frame, new_dimensions, interpolation=cv.INTER_AREA)

# Load the image
 # Load as grayscale image
image = cv.imread('pyramids.png', cv2.IMREAD_GRAYSCALE)
image = resize_frame(image)

# Define the structuring element (square in this case)
kernel = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
], 'uint8')

# Perform dilation
eroded_image = cv.erode(image, kernel, iterations=2)

# Display the original and dilated images
cv.imshow('Original Image', image)

cv.imshow('Eroded Image', eroded_image)

cv.waitKey(0)
cv.destroyAllWindows()
