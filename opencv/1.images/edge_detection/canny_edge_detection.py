import cv2 as cv
import numpy as np

image = cv.imread('gateway_of_india.png')
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
lap = cv.Laplacian(gray_image, -1)
lap = np.uint8(np.absolute(lap))

cv.imshow('Original image', image)
cv.imshow('Gray image', gray_image)
cv.imshow('Laplacian image', lap)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()