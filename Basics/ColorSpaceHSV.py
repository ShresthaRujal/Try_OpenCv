import cv2

image = cv2.imread('../images/dog.jpg')

hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("HSV image", hsv_img)

cv2.imshow("Hue Channel", hsv_img[:,:,0]) #Hue 0-180
cv2.imshow("Saturation Channel", hsv_img[:,:,1]) # Saturation 0-255
cv2.imshow("Value Channel", hsv_img[:,:,2]) # Value 0-255
cv2.waitKey()
cv2.destroyAllWindows()
