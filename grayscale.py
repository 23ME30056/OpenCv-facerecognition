import cv2

# Load the image
image = cv2.imread('cat.jpg')

new_width = 1920
new_height = 1080

# Resize the image
image = cv2.resize(image, (new_width, new_height),interpolation=cv2.INTER_CUBIC)

# Display and save the resized image
cv2.imshow('Resized Image', image)
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display and save the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('gray_image.jpg', gray_image)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Display and save the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('blurred_image.jpg', blurred_image)


# Apply Canny edge detection
edges = cv2.Canny(blurred_image, 100, 200)

import numpy as np

# Define kernel for dilation
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(edges, kernel, iterations=1)

# Display and save the dilated image
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('dilated_image.jpg', dilated_image)

# Display and save the edge-detected image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('edges_image.jpg', edges)

# Apply erosion
eroded_image = cv2.erode(dilated_image, kernel, iterations=1)

# Display and save the eroded image
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('eroded_image.jpg', eroded_image)

# Define coordinates for cropping
x, y, w, h = 500, 500, 700, 800  # Example coordinates (x, y, width, height)

# Crop the image
cropped_image = image[y:y+h, x:x+w]

# Display and save the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cropped_image.jpg', cropped_image)