import cv2 as cv

image = cv.imread('gateway_of_india.png')
cv.imshow('Original image', image)

blurred_image = cv.bilateralFilter(image, 15, 25, 35)
cv.imshow('Bilateral filter', blurred_image)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()