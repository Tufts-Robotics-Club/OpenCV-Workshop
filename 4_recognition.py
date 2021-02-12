import cv2

# Create camera capture device
cam = cv2.VideoCapture(2)

# THIS IS NEW ##################################################################

model_path = 'deps/haarcascade_frontalface_default.xml'
detector = cv2.CascadeClassifier(model_path)

scale_factor = 1.1
minimum_neighbors = 3
minimum_size = (20, 20)

################################################################################

# "infinite" run loop
while True:

    # read from the camera: returns status and frame
    status, frame = cam.read()

    # if unable to read, restart the loop
    if status == False:
        print("Error reading from camera!")
        continue

    # THIS IS NEW ##############################################################

    detector_results = detector.detectMultiScale(frame, scaleFactor=scale_factor, minNeighbors=minimum_neighbors, minSize=minimum_size)

    for (x, y, w, h) in detector_results:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    ############################################################################

    # show the image in a window called 'Window Title'
    cv2.imshow('Window Title', frame)

    # declares to keep the window open for 10 milliseconds and listen
    # for key presses
    key = cv2.waitKey(10) & 0xFF 

    # if the key is q, quit
    if key == ord('q'):
        break

# good practice to always release the camera when done
cam.release()
