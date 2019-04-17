#Dialation, Erosion, Opening and Closing
# Theses are operations in field of mathematical morphology

import cv2
import numpy as np

image = cv2.imread('../images/Paint.png')
cv2.imshow('Original', image)
cv2.waitKey()

kernel = np.ones((5,5),np.uint8)

# Removes pixel at the boundaries of objects in an image
# that means it can help in removing noise in image
# generally minimize white parts by scale 1 
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow('Erosion',erosion)
cv2.waitKey(0)

#Add pixel to the boundaries of objects in an image
# generaly maximize white parts by scale 1
dilation = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Dilation',dilation)
cv2.waitKey()

# Erosion followed by Dilation
opening = cv2.morphologyEx(image,cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening',opening)
cv2.waitKey()
# Dilation followed by Erossion
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)
cv2.waitKey()

cv2.destroyAllWindows()