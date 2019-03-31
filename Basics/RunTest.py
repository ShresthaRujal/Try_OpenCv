import cv2

# Load image
image = cv2.imread('../images/dog.jpg')
# Takes in Title and image to display on the screen
cv2.imshow('Hello World',image)

# waitKey waits for anykey to be pressed before Continuing.
# also takes number parameter to delay for specific milliseconds
cv2.waitKey()

#close all windows.
cv2.destroyAllWindows()