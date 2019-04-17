import cv2
import numpy as np

def sketch(image):
    #convert into grayScale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #clean up image noise using Gaussian Blure
    grayImage_blur = cv2.GaussianBlur(grayImage,(5,5),0)
    #extract edges (note canny is black background with white edges)
    canny_edges = cv2.Canny(grayImage_blur,10,70)
    # to invert binary image
    ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask

# cap is object provided by VideoCapture. COntains a boolean indicatting if it was 
# sucessful (ret). it also contain the images collected from webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("Live",sketch(frame))
    if cv2.waitKey(1) == 13: #(ENTER)
        break 

cap.release()
cv2.destroyAllWindows()