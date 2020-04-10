import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lower_brown = np.array([5, 135, 116])   # Skin Color
    upper_brown = np.array([25, 155, 196])  # Skin Color
    '''lower_brown = np.array([58, 169, 80])      # green Color
    upper_brown = np.array([78, 192, 158])      #green Color '''
    mask = cv2.inRange(hsv, lower_brown, upper_brown)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
