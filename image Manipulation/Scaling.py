import cv2
import numpy as np

image = cv2.imread("../images/dog.jpg")
image_height,image_width = image.shape[:2]
# fx/fy is factors of image by
# By default interpolation is set to Linear Algorithm
image_scaled = cv2.resize(image,None,fx=0.7,fy=0.75)
cv2.imshow('Scaling-Linear', image_scaled)
cv2.waitKey()

image_scaled_cubeic = cv2.resize(image,None,fx=2,fy=2,interpolation =cv2.INTER_CUBIC)
cv2.imshow('Scaling-Cubic', image_scaled_cubeic)
cv2.waitKey()

image_scaled_area = cv2.resize(image,(900,900),interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - Area',image_scaled_area)
cv2.waitKey()

cv2.destroyAllWindows()