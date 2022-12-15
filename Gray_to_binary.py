#will be done later
import cv2
img=cv2.imread('Demo.jpg',0)

binary=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
cv2.imshow('kaka',binary)

cv2.waitKey(0)
