import cv2

# Read the image
image = cv2.imread('your_image.jpg')

# Define the new dimensions
width = 500  # New width
height = 300  # New height

# Resize the image
resized_image = cv2.resize(image, (width, height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()