import cv2
import numpy as np

cam = cv2.VideoCapture(2)

status, frame = cam.read()

if status == False:
    print('Error reading from camera...')
else:
    cv2.imshow('Capture', frame)

    frame[:,:,2] = np.zeros([frame.shape[0], frame.shape[1]])
    cv2.imshow('Modified', frame)
    
    print(type(frame))
    print(frame)

cam.release()
cv2.waitKey(8000)
