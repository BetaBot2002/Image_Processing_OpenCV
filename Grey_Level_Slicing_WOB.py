import cv2
import matplotlib.pyplot as plt
i=cv2.imread('RGB2.jpg',0)
i=cv2.resize(i,(300,300))
j=i.copy()
k=i.copy()
row,col=i.shape
T1=int(input('Enter the Lowest threshold value:'))
T2=int(input('Enter the Highest threshold value:'))
for x in range(1,row):            
    for y in range(1,col):        
        if((j[x][y]>T1) and (j[x][y]<T2)):
            j[x][y]=i[x][y]
            k[x][y]=255
        else:
            j[x][y]=0
            k[x][y]=0
     
cv2.imshow('Original image',i)
histr=cv2.calcHist([i],[0],None,[256],[0,255])
plt.plot(histr)
plt.show()
cv2.imshow('Graylevel slicing without background',k)
histr=cv2.calcHist([k],[0],None,[256],[0,255])
plt.plot(histr)
plt.show()
