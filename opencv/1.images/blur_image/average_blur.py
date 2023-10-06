import cv2 as cv

image = cv.imread('gateway_of_india.png')
cv.imshow('Original image', image)

blurred_image = cv.blur(image, (3, 3))
cv.imshow('Blurred image 3*3 kernel size', blurred_image)

blurred_image = cv.blur(image, (5, 5))
cv.imshow('Blurred image 5*5 kernel size', blurred_image)

blurred_image = cv.blur(image, (7, 7))
cv.imshow('Blurred image 7*7 kernel size', blurred_image)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()