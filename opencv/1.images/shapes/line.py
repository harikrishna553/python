import cv2 as cv
import numpy as np

# Create a black image
image = np.zeros((300, 300, 3), dtype=np.uint8)
image[:] = [255, 255, 255]

# Define the starting and ending points of the line
pt1 = (50, 100)
pt2 = (250, 100)


pt3 = (50, 150)
pt4 = (250, 150)

# Define the color (blue in BGR format)
color1 = (255, 0, 0)
color2 = (0, 255, 0)

# Draw the line
cv.line(image, pt1, pt2, color1, thickness=2)
cv.line(image, pt3, pt4, color2, thickness=10)

# Display the image
cv.imshow("Line Example", image)
cv.waitKey(0)
cv.destroyAllWindows()
