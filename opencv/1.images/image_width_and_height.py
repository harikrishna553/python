import cv2 as cv

# Read the image as matrix of pixels
original_image = cv.imread('photos/tiger.png')
grayed_image = cv.imread('photos/tiger.png', cv.IMREAD_GRAYSCALE)

# Display the image in new window
cv.imshow('original_image', original_image)
cv.imshow('grayed_image', grayed_image)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()