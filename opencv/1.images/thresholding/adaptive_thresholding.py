import cv2 as cv

image = cv.imread('wolfs.jpeg')
grayed_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
adaptive_mean_thresholded_image = cv.adaptiveThreshold(grayed_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 2)
adaptive_gaussian_thresholded_image = cv.adaptiveThreshold(grayed_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 2)
adaptive_mean_thresholded_inverse_image = cv.adaptiveThreshold(grayed_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 7, 2)
adaptive_gaussian_thresholded_inverse_image = cv.adaptiveThreshold(grayed_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 7, 2)

cv.imshow('Wolfs', image)
cv.imshow('grayed_image', grayed_image)
cv.imshow('adaptive_mean_thresholded_image', adaptive_mean_thresholded_image)
cv.imshow('adaptive_gaussian_thresholded_image', adaptive_gaussian_thresholded_image)
cv.imshow('adaptive_mean_thresholded_inverse_image', adaptive_mean_thresholded_inverse_image)
cv.imshow('adaptive_gaussian_thresholded_inverse_image', adaptive_gaussian_thresholded_inverse_image)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()