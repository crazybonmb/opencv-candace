import cv2
import numpy as np
img = cv2.imread('test1.jpg',1)
b = cv2.imread('test1.jpg',1)
img1 = b[400:500,150:300]
img2 = b[100:200,400:550]
print(img1)
print(img2)
dst=cv2.addWeighted(img1,0.3,img2,0.3,0)

cv2.namedWindow('b', cv2.WINDOW_NORMAL)
cv2.imshow('b',img)

cv2.imwrite('test.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()