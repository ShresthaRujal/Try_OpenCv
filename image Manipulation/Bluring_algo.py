import cv2
import numpy as np

image = cv2.imread('../images/dog.jpg')

# use normalized box filter | takes the average of all the pixel under kernel area 
# and replace the central element.
# https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
Averaging_blur = cv2.blur(image,(3,3))
cv2.imshow("Averaging",Averaging_blur)
cv2.waitKey()

Gaussian_blur = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Gaussian", Gaussian_blur)
cv2.waitKey()

# effective against salt and pepper noise in the images
median = cv2.medianBlur(image,5)
cv2.imshow('Median Blurring', median)
cv2.waitKey()

# removes all noise while kepping edges sharp
# 
bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('bilateral Blurring', bilateral)
cv2.waitKey()

cv2.destroyAllWindows()