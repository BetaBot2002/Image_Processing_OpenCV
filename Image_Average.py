import cv2
import numpy as np
img1=cv2.imread('Taj.jpg')
img2=cv2.imread('Lowcont.png')
img1=cv2.resize(img1,(500,300))
imgAvg=img1.copy()
h,w,c=img1.shape
img2=cv2.resize(img2,(w,h))
for i in range(h):
    for j in range(w):
            imgAvg[i][j]=(img1[i][j]+img2[i][j])/2
imgs=np.hstack((img1,img2,imgAvg))
cv2.imshow('',imgs)
cv2.waitKey(0)
