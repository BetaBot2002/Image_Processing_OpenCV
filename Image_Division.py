import cv2
import numpy as np

img1=cv2.imread('Demo.jpg')
h,w,c=img1.shape

img2=cv2.imread('RGB.jpg')
img2=cv2.resize(img2,(w,h))

new_img=img1/img2

# imgs=np.hstack((img1,img2,new_img))

cv2.imshow('div',new_img)

cv2.waitKey(0)