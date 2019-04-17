import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../images/scan.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

# cordinates of the 4 corners of the desired original image
points_A = np.float32([[0,113],[296,19],[151,535],[459,378]])
# cordinates of teh 4 corners of the desired output.
points_B = np.float32([[0,0],[420,0],[0,594],[420,594]])

# transform matrix function
M = cv2.getPerspectiveTransform(points_A,points_B)
warped = cv2.warpPerspective(image,M,(420,594))

cv2.imshow('warpPrespective',warped)
cv2.waitKey()
cv2.destroyAllWindows()