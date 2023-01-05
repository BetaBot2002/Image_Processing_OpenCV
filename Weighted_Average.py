import cv2
img=cv2.imread('Taj.jpg',0)
cv2.imshow('Original image',img)
h,w=img.shape
newimg1=img.copy()
newimg2=img.copy()
mask=[[1,1,1],[1,2,1],[1,1,1]]
for i in range(1,h-1):
    for j in range(1,w-1):
        temp=abs(img[i-1][j-1]*mask[0][0]+img[i-1][j]*mask[0][1]+img[i-1][j]*mask[0][2]+img[i][j-1]*mask[1][0]+img[i][j]*mask[1][1]+img[i][j+1]*mask[1][2]+img[i+1][j-1]*mask[2][0]+img[i+1][j]*mask[2][1]+img[i+1][j+1]*mask[2][2])
        newimg1[i][j]=(temp//9)
cv2.imshow('Weighted average filter',newimg1)
