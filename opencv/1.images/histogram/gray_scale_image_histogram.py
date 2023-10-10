import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('sea_animals.jpeg')
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow('Image', image)
cv.imshow('grayscale_image', grayscale_image)

# Compute grayscale histogram
gray_histogram = cv.calcHist([grayscale_image], [0], None, [256], [0, 256])

plt.title('Histogram for Grayscaled imaged')
plt.xlabel('bins')
plt.ylabel('Number of Pixels')
plt.xlim([0, 256])
plt.plot(gray_histogram)

plt.show()
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()