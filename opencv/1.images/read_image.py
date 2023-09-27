import cv2 as cv

# Read the image as matrix of pixels
image_data = cv.imread('photos/tiger.png')
print(f'type of image_data  is {type(image_data)}')

# Display the image in new window
cv.imshow('Tiger', image_data)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()