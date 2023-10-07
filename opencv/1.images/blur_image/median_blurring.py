import cv2 as cv

image = cv.imread('gateway_of_india.png')
cv.imshow('Original image', image)

blurred_image = cv.medianBlur(image, 5)
cv.imshow('Blurred image 5*5 kernel size', blurred_image)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()