import cv2
import numpy as np

# Create a black image
image = np.zeros((400, 500, 3), dtype=np.uint8)
image[:] = [255, 255, 255]

# Define the text to be added
text = "Hello, World!!!!"

# Draw the text
cv2.putText(image, text, org=(50, 150), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.5, color=(255, 0, 0), thickness=2)
cv2.putText(image, text, org=(50, 200), fontFace=cv2.FONT_HERSHEY_DUPLEX,  fontScale=1, color=(0, 0, 255), thickness=2)

# Display the image
cv2.imshow("Text Example", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
