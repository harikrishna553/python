import cv2 as cv
import numpy as np

image = cv.imread('gateway_of_india.png')
gray_scale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

laplacian = cv.Laplacian(gray_scale_image, -1)
#laplacian = np.uint8(np.absolute(laplacian))
# Convert the result to the appropriate data type and scale it
laplacian = cv.convertScaleAbs(laplacian)

cv.imshow('Original image', image)
cv.imshow('gray_scale_image', gray_scale_image)
cv.imshow('Laplacian image', laplacian)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()