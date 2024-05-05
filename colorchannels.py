import cv2
import numpy as np
width = 640
height = 480
channels = 3 # For color image, 1 for grayscale

# Create a blank image

img = cv2.imread('karmakar.jpg')
blank = np.zeros(img.shape[:2], dtype=np.uint8)
b,g,r = cv2.split(img)
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('red',red)
cv2.imshow('green',green)
cv2.imshow('blue',blue)
cv2.waitKey(0)
cv2.dwstroyAllWindows()