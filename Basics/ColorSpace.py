import cv2

image = cv2.imread('../images/dog.jpg')

B,G,R = image[10,50]
print(B,G,R)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray_image[10,50])