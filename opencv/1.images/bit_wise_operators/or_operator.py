import cv2 as cv
import numpy as np

image = np.zeros((500, 500), dtype='uint8')

blank_image_1 = image.copy()
blank_image_2 = image.copy()

cv.rectangle(blank_image_1, (40, 40), (450, 450), color=255, thickness=-1)
cv.circle(blank_image_2, (250, 250), 240, color=255, thickness=-1)

image_with_or_operator = cv.bitwise_or(blank_image_1, blank_image_2)

cv.imshow('Rectangle', blank_image_1)
cv.imshow('Circle', blank_image_2)

cv.imshow('image_with_or_operator', image_with_or_operator)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()