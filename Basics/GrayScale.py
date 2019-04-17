import cv2

image = cv2.imread('../images/dog.jpg')
cv2.imshow('Hello World',image)
cv2.waitKey()

#convert the full RGB color image to GRAY scale image
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# OR Direct 
# gray_image = cv2.imread('./images/dog.jpg',0)
cv2.imshow('Grayscale',gray_image)
cv2.waitKey()

cv2.destroyAllWindows()