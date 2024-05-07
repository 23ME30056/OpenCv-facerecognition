import cv2               

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#  use this if you have haar_face.xml downloaded 
# face_cascade = cv2.CascadeClassifier('haar_face.xml')

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        break

    #  you can use if you want. otherwise comment kardo.Resize the frame to fit the full screen
    frame = cv2.resize(frame, (0, 0), fx=2, fy=2)  # Change the scaling factor according to your screen resolution
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # for better face detection, increase scalefactor(you know why), increasw minNeighbors,and increase minSize of face(tuple of height and width)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=10, minSize=(60, 60)) 
    
    # Draw rectangles around the faces vimp
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break


cap.release()
cv2.destroyAllWindows()