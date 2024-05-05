
import cv2
import numpy as np

# Read the image
image = cv2.imread('karmakar.jpg')
width = 500  # New width
height = 300  # New height

# Resize the image
image = cv2.resize(image, (width, height))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresh',thresh)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank canvas
contour_image = np.zeros_like(image)
cv2.drawContours(contour_image, contours, -1, (10, 240, 255), 2)

# Alternatively, draw contours on the original image
# cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.RETR_LIST: Retrieves all contours without any hierarchical relationships. This is the simplest mode, where each contour is retrieved and stored as a separate contour.
# cv2.RETR_EXTERNAL: Retrieves only the external contours, ignoring any internal contours. It is useful when you only need the outer boundaries of objects.
# cv2.RETR_CCOMP: Retrieves all contours and organizes them into a two-level hierarchy. The first level contains external contours, while the second level contains internal contours.
# cv2.RETR_TREE: Retrieves all contours and reconstructs a full hierarchy of nested contours. This mode retrieves all contours and reconstructs the full hierarchy of nested contours, which can be useful for analyzing the relationships between different contours.
# Method: This parameter specifies the contour approximation method. It determines how the contours are approximated from the detected edges. There are several approximation methods available:
# cv2.CHAIN_APPROX_NONE: Stores all the contour points. It provides the highest level of accuracy but can result in a large number of points.
# cv2.CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangular contour is encoded with only four points. It is useful when the exact shape of the contour is not necessary.
# cv2.CHAIN_APPROX_TC89_L1, cv2.CHAIN_APPROX_TC89_KCOS: Applies one of the flavors of the Teh-Chin chain approximation algorithm.

