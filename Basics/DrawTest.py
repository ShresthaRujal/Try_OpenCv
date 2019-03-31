import cv2
import numpy as np

# create a blank image
image = np.zeros((512,512,3), np.uint8)

image_bw = np.zeros((512,512),np.uint8)

# parameter(image,start_point,end_point,color,thickness)
cv2.line(image,(0,0),(511,511),(255,127,0),5)
cv2.circle(image,(100,100),100,(255,127,0),-1)
cv2.rectangle(image_bw,(100,100),(300,250),(127,50,127),-1)

points = np.array([[10,10],[511,400],[127,127],[300,50]],np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(image_bw,[points],True,(255,127,0),3)

# cv2.putText(image,"text",starting_point,font,font Size,color,thickness)
cv2.putText(image_bw,"HELLO WORLD!",(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
cv2.imshow("Black",image)
cv2.imshow("Black and White", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()