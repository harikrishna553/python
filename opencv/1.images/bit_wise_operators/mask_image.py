import cv2 as cv
import numpy as np

# Read the image as matrix of pixels
panda_image = cv.imread('panda.png')

blank_image = np.zeros(panda_image.shape[:2], dtype='uint8')
masked_image = cv.circle(blank_image, (400, 500), 400, color=255, thickness=-1)

result_after_masking = cv.bitwise_and(panda_image, panda_image, mask=masked_image)

# Display the image in new window
cv.imshow('panda_image', panda_image)
cv.imshow('masked_image', masked_image)
cv.imshow('result_after_masking', result_after_masking)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()