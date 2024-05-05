import cv2
import numpy as np

# Read the image
image = cv2.imread('karmakar.jpg')
image = cv2.resize(image, (800, 600))
# Get image dimensions
height, width = image.shape[:2]

# Create a blank mask
mask = np.zeros((height, width), dtype=np.uint8)

# Define circle parameters (center and radius)
center = ((width // 2)-20, (height // 2)-30)  # center of the image
radius = min(width, height) // 4  # radius as 1/4 of the minimum dimension

# Draw a filled circle on the mask
cv2.circle(mask, center, radius, 255, -1)  # 255 for white color, -1 for filled circle

# Apply the mask to the original image
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original and masked images
cv2.imshow('Original Image', image)
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()