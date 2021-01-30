import numpy as np
import cv2 

img=np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,0),(512,512),(0,150,0),5)

cv2.circle(img,(300,300), 150, (0, 0,150), 5)
cv2.circle(img,(150,150), 50, (60, 0,100), 5)
cv2.circle(img,(450,150), 50, (60, 0,150), 5)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
points=np.array([[50, 50],[50, 100],[100, 200],[200, 400], [400,50]], np.int32)
points=points.reshape((-1,1,2))
print(points)

cv2.polylines(img[points],1,(0,0,100),5)
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX


cv2.imshow("Window Name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
