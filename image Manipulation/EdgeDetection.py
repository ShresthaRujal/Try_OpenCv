import cv2
import numpy as np

image = cv2.imread('../images/dog.jpg')

# sobel algorithm are used to emphasize vertical or horizontal edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0,1,ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1,0,ksize=5)

cv2.imshow('Original',image)
cv2.waitKey()

cv2.imshow('Sobel X', sobel_x)
cv2.waitKey()

cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey()

sobel_OR = cv2.bitwise_or(sobel_x,sobel_y)
cv2.waitKey()

# laplacian algorithm gets all orientations
laplacian = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow('Laplatian', laplacian)
cv2.waitKey()

#canny algorithm is optimal algorithm due to low error rate, well defined edges and accurate detection
# takes in three parameters (image,threshold1,threshold2)
# any gradient value larger than threshold2 is considered to be an edge. Any value below threshold1
#is considered not to be an edge. Values between threshold1 and threshold2 are either classified as edges for non-edges based on how their 
# intensities are "connected".
canny = cv2.Canny(image,20,170)
cv2.imshow("canny",canny)
cv2.waitKey()

cv2.destroyAllWindows()
