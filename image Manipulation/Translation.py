import cv2
import numpy as np

image = cv2.imread("../images/dog.jpg")

height,width = image.shape[:2]
quarter_height, quater_width = height/4, width/4

# as we know Translation can be optained as "P+T"
# into Matrix form :- |1 0 tx|
                      |0 1 ty|
# tx = quater_width = to which extent image is to be translate and respectively. 
T = np.float32([[1,0,quater_width],[0,1,quarter_height]])

# warpAffine applied for transformation to an image 

# parameter cv2.warpAffine(src,mapMatrix,dsize)
# for more information check "https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#warpaffine"
img_translation = cv2.warpAffine(image,T,(width,height))

cv2.imshow('Translation',img_translation)
cv2.waitKey()
cv2.destroyAllWindows()