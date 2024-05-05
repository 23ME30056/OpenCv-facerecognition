import cv2
# Read the image in grayscale
image = cv2.imread('karmakar.jpg', cv2.IMREAD_GRAYSCALE)
image =  cv2.resize(image,(800,600))

# Apply simple thresholding with a threshold value of 127
# The second argument is the threshold value
# The third argument is the maximum value to be assigned if pixel value is greater than the threshold
# The fourth argument is the thresholding type
# cv2.THRESH_BINARY is for binary thresholding
# cv2.THRESH_BINARY_INV is for inverse binary thresholding
_, binary_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
_, binary_threshold_inv = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.imshow('Inverse Binary Threshold', binary_threshold_inv)
result = cv2.bitwise_and(binary_threshold, binary_threshold_inv)
cv2.imshow('bitwise',result)
adaptive_mean_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply adaptive thresholding with Gaussian method
adaptive_gaussian_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the original and thresholded images

cv2.imshow('Adaptive Mean Threshold', adaptive_mean_threshold)
cv2.imshow('Adaptive Gaussian Threshold', adaptive_gaussian_threshold)


cv2.waitKey(0)
cv2.destroyAllWindows()