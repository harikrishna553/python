import cv2 as cv

video_capture = cv.VideoCapture('videos/bird.mp4')

while True:
    # Read the video frame by frame
    # is_true says whether the frame is successfully read or not
    is_true, frame = video_capture.read()

    if is_true == False:
        break

    # Show the frame
    cv.imshow('video', frame)

    # If the letter x is pressed then come out of video
    if (cv.waitKey(20) & 0xFF) == ord('x'):
        break

video_capture.release()

# Close the OpenCV windows
cv.destroyAllWindows()