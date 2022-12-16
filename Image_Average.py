import cv2
import numpy as np

img1=cv2.imread('Demo.jpg')
img2=cv2.imread('RGB.jpg')
imgAvg=img1.copy()

h,w,c=img1.shape

img2=cv2.resize(img2,(w,h))

for i in range(h):
    for j in range(w):
            imgAvg[i][j]=(img1[i][j]+img2[i][j])/2

cv2.imshow('',imgAvg)

cv2.waitKey(0)