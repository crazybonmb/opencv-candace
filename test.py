import numpy as np
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread('test1.jpg',1)
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

roi=img[549:603,145:168]
img[77:131,680:703]=roi

print(img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) 
plt.show()

# cv2.namedWindow('test5', cv2.WINDOW_NORMAL)
# cv2.imshow('test5',img)
# cv2.imwrite('test.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()