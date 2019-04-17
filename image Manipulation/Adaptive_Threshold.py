import cv2
import numpy as np

image_original = cv2.imread('../images/dog.jpg')
image =cv2.cvtColor(image_original,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original',image)
cv2.waitKey(0)

ret,threshold1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', threshold1)
cv2.waitKey()


image = cv2.GaussianBlur(image,(3,3),0)
# ADAPTIVE_THRESH_MEAN_C -> Based on mean of nighborhood of pixels
# ADAPTIVE_THRESH_GAUSSIAN_C ->weighted sum of nighborhood pixels under the Gaussian window
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow("ADAPTIVE",thresh)
cv2.waitKey()

#OTSU use threshold function, cleaver algorithm that assumes two peaks from image histogram
# with two different height and takes a value of thoes two peaks
_, th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('OTSU', th2)
cv2.waitKey()

blur = cv2.GaussianBlur(image,(5,5),0)
_,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Gaussian OTSU', th3)
cv2.waitKey()
cv2.destroyAllWindows()
