import cv2
import numpy as np

image = cv2.imread('../images/dog.jpg')
cv2.imshow('Original',image)
cv2.waitKey()

# normalizing 3x3 matrix kernel so that the sum of all values in matrix is 1
# or else intensity will increase.
kernel =np.ones((3,3),np.float32) / 9

blurred = cv2.filter2D(image, -1 ,kernel)
cv2.imshow('kernel bluring', blurred)
cv2.waitKey()

kernel = np.ones((7,7),np.float32) / 49

blurred2 = cv2.filter2D(image,-1,kernel)
cv2.imshow('kernel bluring 2', blurred2)
cv2.waitKey()
cv2.destroyAllWindows()