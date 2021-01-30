import numpy as np
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread('test1.jpg',1)
# b = img[:,:,]
# b[100:200,100:200,0]=0
# b[146:191,460:607,1]=0
# b[300:200,200:100,2]=0
# print(b)
# roi=img[549:603,145:168]
# img[77:131,680:703]=roi
# print(img)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) 
# plt.show()

cv2.namedWindow('b', cv2.WINDOW_NORMAL)
cv2.imshow('b',img)

cv2.imwrite('test.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()