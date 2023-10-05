import cv2 as cv

# Read the image as matrix of pixels
image = cv.imread('buildings.png')
horizontal_flip = cv.flip(image, 0)
vertical_flip = cv.flip(image, 1)
horizontal_and_vertical_flip = cv.flip(image, -1)

# Display the image in new window
cv.imshow('Buildings', image)
cv.imshow('horizontal_flip', horizontal_flip)
cv.imshow('vertical_flip', vertical_flip)
cv.imshow('horizontal_and_vertical_flip', horizontal_and_vertical_flip)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()
