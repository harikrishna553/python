import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('rgb.png')

cv.imshow('image in opencv', image)

plt.imshow(image)
plt.title('Image in matplotlib')
plt.show()

# Close the OpenCV windows
cv.destroyAllWindows()