import cv2 as cv
import numpy as np

# Create a black image
image = np.zeros((600, 600, 3), dtype=np.uint8)
image[:] = [255, 255, 255]

# Define the center and radius of the circle
center1 = (150, 150)
center2 = (250, 250)
center3 = (350, 350)
radius = 50

# Define the color (red in BGR format)
color1 = (0, 255, 0)
color2 = (255, 0, 0)
color3 = (0, 0, 255)

# Draw the circle
cv.circle(image, center1, radius, color1, thickness=2)
cv.circle(image, center2, radius, color2, thickness=-1)
cv.circle(image, center3, radius, color3, thickness=cv.FILLED)

# Display the image
cv.imshow("Circle Example", image)
cv.waitKey(0)
cv.destroyAllWindows()
