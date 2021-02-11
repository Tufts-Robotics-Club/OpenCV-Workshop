import cv2

# Create camera capture device
cam = cv2.VideoCapture(2)

# THIS IS NEW ##################################################################

OPENCV_OBJECT_TRACKERS = {
    'csrt': cv2.TrackerCSRT_create,  # More accurate than KCF, but slightly slower
    'kcf': cv2.TrackerKCF_create,  # Fast, doesn't do well with occlusion
    # 'boosting': cv2.TrackerBoosting_create,  # Slow, outdated
    'mil': cv2.TrackerMIL_create,  # Better accuraccy than Boosting
    # 'tld': cv2.TrackerTLD_create,  # Prone to false-positives (do not use)
    # 'medianflow': cv2.TrackerMedianFlow_create,  # Doesn't do well with fast moving targets
    # 'mosse': cv2.TrackerMOSSE_create,  # *Extremely* fast, less accurate than KCF
}

tracker = OPENCV_OBJECT_TRACKERS['csrt']()
reference = None

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

    if reference is not None:
        ret, box = tracker.update(frame)
        if ret == False:
            print("Error updating tracker")
            continue

        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ############################################################################

    # show the image in a window called 'Window Title'
    cv2.imshow('Window Title', frame)

    # declares to keep the window open for 10 milliseconds and listen
    # for key presses
    key = cv2.waitKey(10)

    # if the key is q, quit
    if key == ord('q'):
        break

    # THIS IS NEW ##############################################################

    if key == ord('s'):
        (x, y, w, h) = cv2.selectROI('Window Title', frame, fromCenter=False, showCrosshair=True)
        tracker.init(frame, (x, y, w, h))
        reference = frame[y:y+h, x:x+w]
        cv2.imshow('Reference', reference)

    ############################################################################

# good practice to always release the camera when done
cam.release()
