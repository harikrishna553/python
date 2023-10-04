import cv2 as cv

# Read the image as matrix of pixels
image = cv.imread('photos/tiger.png')

print('\nResizing image to (500, 500)')
image = cv.resize(image, (500, 500), interpolation=cv.INTER_AREA)

# Display the image in new window
cv.imshow('Tiger', image)

cropped_image = image[20:300, 100: 350]
# Display the image in new window
cv.imshow('cropped_image', cropped_image)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()