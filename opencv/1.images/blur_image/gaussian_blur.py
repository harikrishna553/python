import cv2 as cv

image = cv.imread('gateway_of_india.png')
cv.imshow('Original image', image)

blurred_image = cv.GaussianBlur(image, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blurred_image)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()