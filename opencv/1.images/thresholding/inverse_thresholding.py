import cv2 as cv

image = cv.imread('wolfs.jpeg')
cv.imshow('Wolfs', image)

grayed_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('grayed_image', grayed_image)

threshold_value_used, inverse_threshold_image = cv.threshold(grayed_image, 150, 200, cv.THRESH_BINARY_INV)
cv.imshow('binary image', inverse_threshold_image)

print(f'threshold_value_used : {threshold_value_used}')

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()