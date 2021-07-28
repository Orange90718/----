import numpy as np
import cv2 as cv

#開圖
img1=cv.imread('5t5.jfif')

# 创建一个黑色的图像
print(len(img1),len(img1[0]))
print(img1.shape)

cv.line(img1,(200,100),(200,200),(0,0,255),5)
cv.rectangle(img1,(100,50),(250,300),(255,0,0),3)

#秀圖
cv.namedWindow('5t5',cv.WINDOW_NORMAL)
cv.imshow('5t5',img1)
cv.waitKey(0)
cv.destroyAllWindows()