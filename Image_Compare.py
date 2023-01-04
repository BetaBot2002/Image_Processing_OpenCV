import cv2
import numpy as np

img1=cv2.imread('Demo.jpg')
h,w,c=img1.shape

img2=cv2.imread('Taj.jpg')
img2=cv2.resize(img2,(w,h))

new_img=img1-img2

status=True

for i in range(h):
    for j in range(w):
        for k in range(c):
            if(new_img[i][j][k]!=0):
                status=False
                break 

if status:
    print("Identical Image")
    cv2.imshow('Identity',np.hstack((img1,img2)))
else:
    print("Not Equal")
    cv2.imshow('Not Equal',new_img)



# imgs=np.hstack((img1,img2,new_img))

# cv2.imshow('add',new_img)

cv2.waitKey(0)