pip install matplotlib
import cv2

import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread('karmakar.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the histogram
histogram, bins = np.histogram(image.flatten(), 256, [0,256])

# Plot the histogram
plt.plot(histogram, color='black')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Histogram of Grayscale Image')
plt.grid(True)
plt.show()
