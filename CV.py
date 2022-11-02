"""
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    rgb = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
    # Display the resulting frame
    cv.imshow('frame', rgb)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensitivity = 15
    """
    lower_blue = np.array([75, 15, 51])
    upper_blue = np.array([125, 255, 255])
    lower_red = np.array([175, 150, 0])
    upper_red = np.array([240, 200, 255])
    lower_green = np.array([60-sensitivity, 30, 100])
    upper_green = np.array([60+sensitivity, 255, 255])
    """
    lower_blue = np.array([75, 15, 51])
    upper_blue = np.array([125, 255, 255])
    lower_red = np.array([175, 150, 0])
    upper_red = np.array([240, 200, 255])
    lower_green = np.array([60 - sensitivity, 30, 100])
    upper_green = np.array([60 + sensitivity, 255, 255])

    maskB = cv2.inRange(hsv, lower_blue, upper_blue)
    maskG = cv2.inRange(hsv, lower_green, upper_green)
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    resB = cv2.bitwise_and(frame, frame, mask=maskB)
    resG = cv2.bitwise_and(frame, frame, mask=maskG)
    resR = cv2.bitwise_and(frame, frame, mask=maskR)

    cv2.imshow('frame', frame)
    cv2.imshow('maskB', maskB)
    cv2.imshow('maskG', maskG)
    cv2.imshow('maskR', maskR)
    cv2.imshow('resB', resB)
    cv2.imshow('resG', resG)
    cv2.imshow('resR', resR)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

