import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('flowers.jpeg')

colors = ('b', 'g', 'r')
for index, color in enumerate(colors):
    hist = cv.calcHist([image], [index], None, [256], [0,256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

cv.imshow('Image', image)
plt.title('Histogram for image')
plt.xlabel('bins')
plt.ylabel('Number of Pixels')
plt.xlim([0, 256])

plt.show()
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()