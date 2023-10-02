import cv2

# Initialize a video capture object (e.g., from a webcam)
video_capture = cv2.VideoCapture(0)

# Set the desired frame width and height
width = 640  # Set the desired width in pixels
height = 480  # Set the desired height in pixels

video_capture.set(3, width)  # Set frame width
video_capture.set(4, height)  # Set frame height

# Check if the video capture is opened successfully
if not video_capture.isOpened():
    print("Error: Video capture could not be opened.")
    exit()

while True:
    ret, frame = video_capture.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Error: Failed to capture a frame.")
        break

    # Check if the frame dimensions are valid
    if frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Video Frame', frame)
    else:
        print("Error: Invalid frame dimensions.")

    # Exit the loop if a key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any open windows
video_capture.release()
cv2.destroyAllWindows()
