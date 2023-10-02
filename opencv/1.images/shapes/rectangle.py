import cv2 as cv
import numpy as np

# Create a blank image
image = np.zeros((800, 1200, 3), dtype=np.uint8)
image[:] = [220, 220, 220]

# rectangle with red color
# color is in (b, g, r) formant
cv.rectangle(image, (100, 200), (300, 500), (0, 0, 255), thickness=2)

# fill the rectangle
cv.rectangle(image, (500, 200), (700, 500), (0, 255, 0), thickness=-2)

# fill the rectangle
cv.rectangle(image, (900, 200), (1100, 500), (255, 0, 0), thickness=cv.FILLED, lineType=cv.LINE_4)

# Display the image
cv.imshow('Rectangle Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
