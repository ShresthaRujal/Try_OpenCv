import cv2
import numpy as np

image = cv2.imread('../images/gradient.jpg')

# image = cv2.cvtColor(square,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# everything above the threshold turns black and below threshold turns white
ret,threshold1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold 1',threshold1)

# its an inverse of THRESH_BINARY
ret,threshold2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Inverse',threshold2)

# everything above the threshold stays same as image and
# everything below the threshold stays as threshold i.e 127
ret,threshold3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('Threshold Trunc',threshold3)

# everything above the threshold is masked to blackcolor and
# everything below the threshold stays same as image
ret,threshold4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('Threshold TOZERO',threshold4)

# its an inverse of THRESH_TOZERO_INV
ret,threshold5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Threshold Tozero inv',threshold5)
cv2.waitKey()
cv2.destroyAllWindows()