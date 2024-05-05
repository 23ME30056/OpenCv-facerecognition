import cv2 as cv
img = cv.imread('C:/Users/skm06/OneDrive/Desktop/bubu1.jpg')
new_width = 400
new_height = 300

# Resize the image
resized_img = cv.resize(img, (new_width, new_height))

# Display the original and resized images (optional)
cv.imshow('Original Image', img)
cv.imshow('Resized Image', resized_img)
cv.imshow('bubu1',img)
# cv.destroyAllWindows()

# cap = cv.VideoCapture('video_file.mp4')
# while True:
# isTrue,frame = capture.read()
# cv.imshow('Video', frame)
# # Wait for 25 milliseconds; press 'q' to exit
# if cv.waitKey(25) & 0xFF == ord('q'):
#  break
cv.waitKey(0)

# Open the video file
cap = cv.VideoCapture('input_video.mp4')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Unable to open the video file.")
    exit()

# Define the new dimensions for resizing
new_width = 640
new_height = 480

# Get the frames per second (fps) of the input video
fps = cap.get(cv.CAP_PROP_FPS)

# Get the total number of frames in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

# Create a VideoWriter object to write the scaled video
out = cv.VideoWriter('output_video.mp4', cv.VideoWriter_fourcc(*'mp4v'), fps, (new_width, new_height))

# Loop to read frames from the video and scale each frame
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Unable to read the frame.")
        break

    # Resize the frame
    resized_frame = cv.resize(frame, (new_width, new_height))

    # Write the resized frame to the output video
    out.write(resized_frame)

    # Display the resized frame (optional)
    cv.imshow('Resized Video', resized_frame)

    # Wait for 25 milliseconds; press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects, and close all OpenCV windows
cap.release()
out.release()
# uint8 refers to unsigned 8-bit integers
img = np.zeros((400, 400, 3), dtype=np.uint8)  

# Draw a line from (50, 50) to (350, 350) with blue color and thickness 5
cv.line(img, (50, 50), (350, 350), (255, 0, 0), 5)

# Draw a circle centered at (200, 200) with radius 100, green color, and filled
cv.circle(img, (200, 200), 100, (0, 255, 0), -1)

# Display the image with the drawn shapes
cv.imshow('Image with Line and Circle', img)
cv.destroyAllWindows()