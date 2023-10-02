import cv2 as cv

def resize_frame(frame, scale_width=0.5, scale_height=0.5):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    new_dimensions = (width, height)
    return cv.resize(frame, new_dimensions, interpolation=cv.INTER_AREA)

video_capture = cv.VideoCapture('videos/bird.mp4')

while True:
    # Read the video frame by frame
    # is_true says whether the frame is successfully read or not
    is_true, frame = video_capture.read()

    # You can skip this if you want
    if is_true == False:
        break

    new_frame = resize_frame(frame, 0.3, 0.2)
    # Show the frame
    cv.imshow('bird video', new_frame)

    # If the letter x is pressed then come out of video
    if (cv.waitKey(20) & 0xFF) == ord('x'):
        break

video_capture.release()

# Close the OpenCV windows
cv.destroyAllWindows()