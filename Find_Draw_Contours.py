import cv2
import numpy as np

cap = cv2.VideoCapture(0)
panel = np.zeros([100, 800, 3], np.uint8)   # Black Screen 100 height and 700 width
cv2.namedWindow("panel")


def nothing(x):
    pass


cv2.createTrackbar("L - h", "panel", 0, 179, nothing)   # pass
cv2.createTrackbar("U - h", "panel", 179, 179, nothing)

cv2.createTrackbar("L - s", "panel", 0, 255, nothing)   # pass
cv2.createTrackbar("U - s", "panel", 255, 255, nothing)

cv2.createTrackbar("L - v", "panel", 0, 255, nothing)   # pass
cv2.createTrackbar("U - v", "panel", 255, 255, nothing)


while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - h", "panel")
    u_h = cv2.getTrackbarPos("U - h", "panel")

    l_s = cv2.getTrackbarPos("L - s", "panel")
    u_s = cv2.getTrackbarPos("U - s", "panel")

    l_v = cv2.getTrackbarPos("L - v", "panel")
    u_v = cv2.getTrackbarPos("U - v", "panel")

    '''lower_brown = np.array([5, 135, 116])   # Skin Color
    upper_brown = np.array([25, 155, 196])  # Skin Color
    lower_brown = np.array([58, 169, 80])      # green Color
    upper_brown = np.array([78, 192, 158])      #green Color '''

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])     

    mask = cv2.inRange(hsv, lower_color, upper_color)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("panel", panel)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
