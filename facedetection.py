import cv2
import numpy as np
img = cv2.imread('karmakar.jpg')
img = cv2.resize(img,(800,600))
cv2.imshow('image',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
haar_cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'number of faces found  = {len(faces_rect)}')
# Draw rectangles around the detected faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
