import cv2 as cv
import numpy as np

# Define the dimensions of the 2D array
rows = 500
cols = 500

# Create a 2D NumPy array filled with 4s
frame = np.full((rows, cols), 0, dtype='uint8')
cv.imshow('White blank image', frame)

cv.waitKey(0)