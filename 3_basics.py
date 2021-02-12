import cv2

# Create camera capture device
cam = cv2.VideoCapture(2)

# "infinite" run loop
while True:

    # read from the camera: returns status and frame
    status, frame = cam.read()

    # if unable to read, restart the loop
    if status == False:
        print("Error reading from camera!")
        continue

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
