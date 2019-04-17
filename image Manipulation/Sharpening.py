import cv2
import numpy as np

image =cv2.imread('../images/dog.jpg')
cv2.imshow('Original', image)

kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

sharpened = cv2.filter2D(image,-1,kernel_sharpening)

cv2.imshow('Sharpening',sharpened)
cv2.waitKey()
cv2.destroyAllWindows()