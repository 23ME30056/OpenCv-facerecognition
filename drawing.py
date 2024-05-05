import cv2 as cv
import numpy as np
# uint8 refers to unsigned 8-bit integers
img = np.zeros((1280, 720, 3), dtype=np.uint8)  
blank = np.zeros((1280,720,3),dtype=np.uint8 )

# Draw a line from (50, 50) to (350, 350) with blue color and thickness 5
cv.line(img, (0, 0), (350, 350), (255, 0, 0), 5)

# Draw a circle centered at (200, 200) with radius 100, green color, and filled
cv.circle(img, (200, 200), 100, (0, 255, 0), 0)
# Define the text to be written
text = "Hello, OpenCV!"
font = cv.FONT_HERSHEY_SIMPLEX
scale = 2
color = (255, 255, 255)  # White color in BGR
thickness = 2

# Get the size of the text bounding box
text_size = cv.getTextSize(text, font, scale, thickness)[0]

# Calculate the position to center the text
text_x = int((blank.shape[1] - text_size[0]) / 2)
text_y = int((blank.shape[0] + text_size[1]) / 2)

# Write the text on the image
cv.putText(blank, text, (text_x, text_y), font, scale, color, thickness)

# Display the image
cv.imshow('Text on Image', blank)
cv.waitKey(0)
cv.destroyAllWindows()

# Save the image with text
cv2.imwrite('output_image.jpg', blank)

cv.destroyAllWindows()
