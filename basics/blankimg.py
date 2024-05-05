import cv2
import numpy as np
width = 640
height = 480
channels = 3 # For color image, 1 for grayscale

# Create a blank image
blank_image = np.zeros((height, width, channels), dtype=np.uint8)

# Display the blank image
cv2.imshow('Blank Image', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()