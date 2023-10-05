import cv2 as cv

# if angle is positive, then it rotate the image in anti clock wise direction
# If angle is negative, then it rotate the image in clock wise direction
def rotate(img, angle, rotation_point=None):
    width = img.shape[1]
    height = img.shape[0]

    if rotation_point == None:
        rotation_point = (width // 2, height // 2)

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotation_matrix, dimensions)


# Read the image as matrix of pixels
image = cv.imread('nature.png')
image = cv.resize(image, (1000, 800))

# Display the image in new window
cv.imshow('Nature', image)
cv.imshow('Rotate image by 45 degrees', rotate(image, 45))
cv.imshow('Rotate image by -45 degrees', rotate(image, -45))

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()
