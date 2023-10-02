import cv2 as cv
import numpy as np

# Create a 2D NumPy array filled with 4s
frame = np.full((500, 500, 3), 255, dtype='uint8')

frame[100:200, 100:200] = [0, 0, 255]
frame[200:300, 200:300] = [0, 255, 0]
frame[300:400, 300:400] = [255, 0, 0]

cv.imshow('White blank image', frame)
cv.waitKey(0)