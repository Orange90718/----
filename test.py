import cv2
#開圖
img1=cv2.imread('5t5.jfif')
#秀圖
cv2.namedWindow('5t5',cv2.WINDOW_NORMAL)
cv2.imshow('5t5',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()