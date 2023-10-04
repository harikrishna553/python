import cv2 as cv

# Read the image as matrix of pixels
frame = cv.imread('photos/tiger.png')

# Get the height and width of the image
height = frame.shape[0]
width = frame.shape[1]

print(f'height : {height}')
print(f'width : {width}')

# Display the image in new window
cv.imshow('Tiger', frame)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()