import cv2 as cv
import numpy as np

image = np.zeros((500, 500), dtype='uint8')
cv.rectangle(image, (50, 50), (400, 400), color=255, thickness=-1)

image_with_not_operator = cv.bitwise_not(image)

cv.imshow('image', image)
cv.imshow('image_with_not_operator', image_with_not_operator)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()