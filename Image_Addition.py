import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('Demo.jpg')
h,w,c=img1.shape

img2=cv2.imread('RGB.jpg')
img2=cv2.resize(img2,(w,h))

new_img=img1+img2

imgs=np.hstack((img1,img2,new_img))
histr=cv2.calcHist([new_img],[0],None,[256],[0,255])
plt.plot(histr)
plt.show()
cv2.imshow('add',imgs)
cv2.waitKey(0)