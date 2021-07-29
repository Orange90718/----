  
import cv2

#開圖
img1 = cv2.imread('./image/11.jfif')

print(img1.shape)
print(img1[100,200])
print(img1.item(100,200,1))
# img1[200:400,300:700]=[255,0,0]
roi = img1[200:400,200:300]  
roi[:,:,1]=255
# roi[:,:,2]=0
h,w,a =roi.shape
img1[0:100,600:700] = roi
print(len(roi),len(roi[0]))
img1[10:10+h,10:10+w] = roi
print(img1.size)
#秀圖
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)