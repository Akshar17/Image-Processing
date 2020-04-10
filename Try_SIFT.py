import cv2
import numpy as np

img = cv2.imread("Demo_2.png", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()

#kp = sift.detect(img, None)

keypoints, descriptors = sift.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, keypoints, None)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
