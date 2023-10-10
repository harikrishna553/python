import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread('sea_animals.jpeg')
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blank_image = np.zeros(image.shape[:2], dtype='uint8')
mask = cv.rectangle(blank_image, (50, 50), (350, 350), color=255, thickness=-1)

# Compute grayscale histogram
gray_histogram = cv.calcHist([grayscale_image], [0], mask, [256], [0, 256])

cv.imshow('Image', image)
cv.imshow('grayscale_image', grayscale_image)
cv.imshow('mask', mask)

plt.title('Histogram for Grayscaled imaged')
plt.xlabel('bins')
plt.ylabel('Number of Pixels')
plt.xlim([0, 256])
plt.plot(gray_histogram)

plt.show()
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()