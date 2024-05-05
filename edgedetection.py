import cv2
import numpy as np
# Read the image in grayscale
image = cv2.imread('karmakar.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(800,600))

# Apply Laplacian operator for edge detection
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Apply Sobel operator for edge detection in x and y directions
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Display the original image and the edges detected using Laplacian and Sobel operators
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.imshow('Sobel Edge Detection X', sobel_x)
cv2.imshow('Sobel Edge Detection Y', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()