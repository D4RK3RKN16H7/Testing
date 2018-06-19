import cv2
import numpy as np

cap = cv2.VideoCapture('http://192.168.1.101:8080/videofeed')
#cap = cv2.VideoCapture('video.mp4')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = frame[0:400, 0:400]
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
