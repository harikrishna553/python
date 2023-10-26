import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

peoples = ['Dhoni', 'Sehwag']

features = []
labels = []

def populate_face_rect_and_label():
    for person in peoples:
        path = os.path.join('.', person)
        label = peoples.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path, image)

            image_array = cv.imread(img_path)
            gray_scaled_image = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)
            faces_rectangle = haar_cascade.detectMultiScale(gray_scaled_image, scaleFactor=1.1, minNeighbors=7)
            for (a, b, c, d) in faces_rectangle:
                face_array = gray_scaled_image[b:b+d, a:a+c]
                features.append(face_array)
                labels.append(label)

populate_face_rect_and_label()

face_recognizer = cv.face_LBPHFaceRecognizer.create()  # Use create() to create the recognizer

features = np.array(features, dtype='object')
labels = np.array(labels, dtype='int')  # Use 'int' instead of 'uint8'

face_recognizer.train(features, labels)
# face_recognizer.save('trained_face_recognizer.yml')  # Save the trained model

image_to_test = cv.imread('img_to_test.png')
gray_scale_image_to_test = cv.cvtColor(image_to_test, cv.COLOR_BGR2GRAY)
face_rect = haar_cascade.detectMultiScale(gray_scale_image_to_test, scaleFactor=1.3, minNeighbors=5)

for (a, b, c, d) in face_rect:
    face = gray_scale_image_to_test[b:b+d, a:a+c]
    label, confidence = face_recognizer.predict(face)
    print(f'Label {peoples[label]} with confidence {confidence}')
    cv.putText(image_to_test, str(f'Label {peoples[label]} with confidence {confidence}'), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), thickness=4)
    cv.rectangle(image_to_test, (a, b), (a+c, b+d), color=(0, 255, 0), thickness=3)

cv.imshow('Face Recognition', image_to_test)
cv.waitKey(0)
cv.destroyAllWindows()

#print(f'Features length: {len(features)}')
#print(f'Labels length: {len(labels)}')
