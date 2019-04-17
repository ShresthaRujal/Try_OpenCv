import cv2
import numpy as np

image = cv2.imread('../images/dog.jpg')

# creates a matrix of ones then multiply by a scaler of 100
# this gives a matrix with same dimensions of image with all values being 100
matrix = np.ones(image.shape,dtype= "uint8") * 75
print(matrix)

# will add brightness in image
added = cv2.add(image,matrix)
cv2.imshow("Added",added)

#will subtract brighness in image
subtracted= cv2.subtract(image,matrix)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destoryAllWindows()
