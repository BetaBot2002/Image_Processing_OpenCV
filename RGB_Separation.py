import cv2
import numpy as np

img=cv2.imread('Lowcont.png')
imgR=img.copy()
imgG=img.copy()
imgB=img.copy()
height,width,ch=img.shape

for i in range(height):
    for j in range(width):
        imgR[i][j][0]=imgR[i][j][1]=0
        imgG[i][j][0]=imgG[i][j][2]=0
        imgB[i][j][1]=imgB[i][j][2]=0

imgs1=np.hstack((img,imgR))
imgs2=np.hstack((imgG,imgB))
imgs=np.vstack((imgs1,imgs2))
cv2.imshow('Separated',imgs)

cv2.waitKey(0)