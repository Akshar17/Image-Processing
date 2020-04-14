import cv2
import numpy as np

cap = cv2.VideoCapture(0)

panel = np.zeros([100, 800, 3], np.uint8)   # Black Screen 100 height and 700 width
cv2.namedWindow("Panel")


def nothing(x):
    pass


cv2.createTrackbar("L - h", "Panel", 0, 179, nothing)   # pass
cv2.createTrackbar("U - h", "Panel", 179, 179, nothing)

cv2.createTrackbar("L - s", "Panel", 0, 255, nothing)   # pass
cv2.createTrackbar("U - s", "Panel", 255, 255, nothing)

cv2.createTrackbar("L - v", "Panel", 0, 255, nothing)   # pass
cv2.createTrackbar("U - v", "Panel", 255, 255, nothing)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - h", "Panel")
    u_h = cv2.getTrackbarPos("U - h", "Panel")

    l_s = cv2.getTrackbarPos("L - s", "Panel")
    u_s = cv2.getTrackbarPos("U - s", "Panel")

    l_v = cv2.getTrackbarPos("L - v", "Panel")
    u_v = cv2.getTrackbarPos("U - v", "Panel")

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])     # u-s 126 only skin

    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(frame, frame, mask=mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)

    cv2.imshow("BG", bg)
    cv2.imshow("FG", fg)
    cv2.imshow("Panel", panel)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
