import pytesseract
import cv2

img = cv2.imread('test.png')
img = cv2.resize(img, (720, 480))
cv2.imshow('Result', img)
cv2.waitKey(0)