import cv2 as cv
import numpy as np

image = cv.imread('gateway_of_india.png')
gray_scale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

sobel_x = cv.Sobel(image, -1, 1, 0)
sobel_y = cv.Sobel(image, -1, 0, 1)
sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow('Original image', image)
cv.imshow('gray_scale_image', gray_scale_image)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)
cv.imshow('sobel', sobel)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()