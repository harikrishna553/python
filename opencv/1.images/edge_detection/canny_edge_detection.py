import cv2 as cv

image = cv.imread('gateway_of_india.png')
cv.imshow('Original image', image)

canny = cv.Canny(image, 120, 150)
cv.imshow('Original image with threshold 120 and 150', canny)

canny = cv.Canny(image, 120, 400)
cv.imshow('Original image with threshold 120 and 400', canny)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()