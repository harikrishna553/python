import cv2 as cv

def resize_frame(frame, scale_width=0.5, scale_height=0.5):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    new_dimensions = (width, height)
    return cv.resize(frame, new_dimensions, interpolation=cv.INTER_AREA)

# Read the image as matrix of pixels
frame = cv.imread('photos/tiger.png')

print(f'height : {frame.shape[0]}')
print(f'width : {frame.shape[1]}')

print('\nResizing image to half')
frame = resize_frame(frame)

print(f'height : {frame.shape[0]}')
print(f'width : {frame.shape[1]}')

# Display the image in new window
cv.imshow('Tiger', frame)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()