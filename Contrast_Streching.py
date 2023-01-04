import cv2,numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('Demo.jpg',0)
# cv2.imshow('old',img)
# cv2.waitKey(0)

#before stretch
histogram=cv2.calcHist([img],[0],None,[256],[0,255])

plt.plot(histogram)
plt.show()

height,width=img.shape

Lmax=255
Lmin=0
Mmax=np.max(img)
Mmin=np.min(img)

def evaluatePixel(pixel):
    global Lmax,Lmin,Mmax,Mmin
    out_pix=(((Lmax-Lmin)*(pixel-Mmin))/(Mmax-Mmin))+Lmin #formula
    return out_pix

for i in range(height):
    for j in range(width):
        img[i][j]=evaluatePixel(img[i][j])

cv2.imshow('Strechted',img)

#after strech
histogram=cv2.calcHist([img],[0],None,[256],[0,255])

plt.plot(histogram)
plt.show()

