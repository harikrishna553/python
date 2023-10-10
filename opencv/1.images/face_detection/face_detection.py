import cv2 as cv

image = cv.imread('rrr.png')
gray_scaled_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rectangle = haar_cascade.detectMultiScale(gray_scaled_image, scaleFactor=1.3, minNeighbors=5, minSize=(110, 110))
print(f'Total faces found {len(faces_rectangle)}')

for (a, b, c, d) in faces_rectangle:
    cv.rectangle(image, (a,b), (a+c, b+d), color=(0, 255, 0), thickness=3)

cv.imshow('image', image)

cv.waitKey(0)

# Close the OpenCV windows
cv.destroyAllWindows()