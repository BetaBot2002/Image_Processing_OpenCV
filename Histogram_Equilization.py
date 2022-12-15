import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('Demo.jpg',0)

freq=np.zeros(256,int)

height,width=img.shape[:2]

for i in range(height):
    for j in range(width):
        freq[img[i][j]]+=1

sum=np.sum(freq)
freq=(freq/sum)
freq=np.cumsum(freq)
freq*=255
freq=np.ceil(freq)

img2=img.copy()

for i in range(height):
    for j in range(width):
        img2[i][j]=freq[img[i][j]]

cv2.imshow('Equi',img2)

histogram=cv2.calcHist([img],[0],None,[256],[0,255])
plt.plot(histogram)


histogram=cv2.calcHist([img2],[0],None,[256],[0,255])
plt.plot(histogram)
plt.show()

cv2.waitKey(0)