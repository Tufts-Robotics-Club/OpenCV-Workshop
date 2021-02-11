import cv2

cam = cv2.VideoCapture(2)

status, frame = cam.read()

if status == False:
    print('Error reading from camera...')
else:
    print(type(frame))
    print(frame)

cam.release()
