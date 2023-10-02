import cv2 as cv
import numpy as np
import random

# Define the dimensions of the blank image
width, height = 1000, 500

random_image = np.zeros((height, width, 3), dtype=np.uint8)
random_image[:] = [255, 0, 0]

# Display the random color image
cv.imshow('Blue Color Image', random_image)
cv.waitKey(0)
cv.destroyAllWindows()
