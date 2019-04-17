import cv2
# multidimensional array
import numpy as np

image =cv2.imread('../images/dog.jpg')
B,G,R = cv2.split(image)

# creating array of the zeros of the same shape as original image
# dtype = 'uint8' refers to which opencv use to store image data
# refrence(https://docs.opencv.org/3.0-beta/modules/imgproc/doc/drawing_functions.html)
zeros = np.zeros(image.shape[:2],dtype = 'uint8')

cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()