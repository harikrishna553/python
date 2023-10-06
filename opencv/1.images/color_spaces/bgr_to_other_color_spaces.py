import cv2 as cv

# Read the image as matrix of pixels
image = cv.imread('flowers.png')
image = cv.resize(image, (1000, 800))

# Display the image in new window
cv.imshow('Original image', image)

# Convert BGR image to RGB
bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
bgr_to_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
bgr_to_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

#bgr_to_bgr555 = cv.cvtColor(image, cv.COLOR_BGR2BGR555)
#bgr_to_bgr565 = cv.cvtColor(image, cv.COLOR_BGR2BGR565)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2HLS)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2BGRA)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2HLS_FULL)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2HSV)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2LAB)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2LUV)
#bgr_to_gray = cv.cvtColor(image, cv.COLOR_BGR2XYZ)

cv.imshow('bgr_to_gray', bgr_to_gray)
cv.imshow('bgr_to_rgb', bgr_to_rgb)
cv.imshow('bgr_to_hsv', bgr_to_hsv)

# Wait for Infinite amount of time for a keyboard key to be pressed
cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()