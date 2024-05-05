import cv2
import numpy
img = cv2.imread('karmakar.jpg')
width = 500  # New width
height = 300  # New height

# Resize the image
img = cv2.resize(img, (width, height))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
lab = cv2.cvtColor(img,cv4'2.COLOR_BGR2LAB)
cv2.imshow('LAB',lab)
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
