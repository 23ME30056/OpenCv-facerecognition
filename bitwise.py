import numpy as np
import cv2

# Define the dimensions of the blank image
width = 400
height = 400
channels = 3  # For color image, 1 for grayscale

# Create a blank image
blank_image = np.zeros((height, width, channels), dtype=np.uint8)

# Draw a rectangle
cv2.rectangle(blank_image, (100, 100), (300, 300), (255, 255, 255), -1)  # white rectangle

# Draw a circle
cv2.circle(blank_image, (150, 150), 100, (255, 255, 255), -1)  # Green circle

cv2.imshow('blank',blank_image)
# Create masks for rectangle and circle
rectangle_mask = np.zeros((height, width), dtype=np.uint8)
cv2.rectangle(rectangle_mask, (50, 50), (200, 200), 255, -1)
circle_mask = np.zeros((height, width), dtype=np.uint8)
cv2.circle(circle_mask, (300, 200), 100, 255, -1)

# # Perform bitwise operations
# bitwise_and = cv2.bitwise_and(blank_image, blank_image, mask=cv2.bitwise_and(rectangle_mask, circle_mask))
# bitwise_or = cv2.bitwise_or(blank_image, blank_image, mask=cv2.bitwise_or(rectangle_mask, circle_mask))
# bitwise_xor = cv2.bitwise_xor(blank_image, blank_image, mask=cv2.bitwise_xor(rectangle_mask, circle_mask))
# bitwise_not = cv2.bitwise_not(blank_image, blank_image, mask=cv2.bitwise_not(rectangle_mask))

# # Display the images
# cv2.imshow('Blank Image', blank_image)
# cv2.imshow('Rectangle Mask', rectangle_mask)
# cv2.imshow('Circle Mask', circle_mask)
# cv2.imshow('Bitwise AND', bitwise_and)
# cv2.imshow('Bitwise OR', bitwise_or)
# cv2.imshow('Bitwise XOR', bitwise_xor)
# cv2.imshow('Bitwise NOT', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()


