import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('Demo.jpg',0)
img2=img.copy()
height,width=img.shape[:2]

paddedImg=np.zeros([height+2,width+2],int)

for i in range(1,height-1):
    for j in range(1,width-1):
        paddedImg[i][j]=img[i-1][j-1]

kernel=np.ones([3,3],int)

for i in range(1,height-1):
    for j in range(1,width-1):
        for k in range(3):
            for l in range(3):
                kernel[k][l]=paddedImg[i+k-1][j+l-1]


        img2[i-1][j-1]=np.mean(kernel)

imgs=np.hstack((img,img2))

cv2.imshow('Filter',imgs)
cv2.waitKey(0)