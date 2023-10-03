import cv2 as cv

def resize_frame(frame, scale_width=0.5, scale_height=0.5):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    new_dimensions = (width, height)
    return cv.resize(frame, new_dimensions, interpolation=cv.INTER_AREA)

image = cv.imread('taj.jpeg')
cv.imshow('BGR image', resize_frame(image, 0.5, 0.5))

grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale image', resize_frame(grayscale_image, 0.5, 0.5))

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()