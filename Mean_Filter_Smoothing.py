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
        kernel[0][0]=paddedImg[i-1][j-1]
        kernel[0][1]=paddedImg[i-1][j]
        kernel[0][2]=paddedImg[i-1][j+1]
        kernel[1][0]=paddedImg[i][j-1]
        kernel[1][1]=paddedImg[i][j]
        kernel[1][2]=paddedImg[i][j+1]
        kernel[2][0]=paddedImg[i+1][j-1]
        kernel[2][1]=paddedImg[i+1][j]
        kernel[2][2]=paddedImg[i+1][j+1]

        img2[i-1][j-1]=np.mean(kernel)

imgs=np.hstack((img,img2))

cv2.imshow('Filter',imgs)
cv2.waitKey(0)