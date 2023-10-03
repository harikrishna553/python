import cv2
import numpy as np

# Read an image using OpenCV
image = cv2.imread('gateway_of_india.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Image', image)

# Define a custom kernel (as a NumPy array)
kernel = np.array([
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
])

# Perform 2D convolution on the image
convolution_result = cv2.filter2D(image, -1, kernel)
cv2.imshow('convolution_result', convolution_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
