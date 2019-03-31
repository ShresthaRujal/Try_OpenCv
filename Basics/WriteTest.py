import cv2

image = cv2.imread('../images/dog.jpg')
print(image.shape)
print('Height of Image',int(image.shape[0]),'pixels')
print('width of Image',int(image.shape[1]),'pixels')

# writes the specific image into given filename
cv2.imwrite('output.jpg',image)
cv2.imwrite('output.png',image)