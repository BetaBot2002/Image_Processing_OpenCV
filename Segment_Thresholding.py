import cv2
import numpy as np
img=cv2.imread("RGB.jpg",0)
max=img.max()
min=img.min()
def thresholdsegmentation(img,thres):
    x,y=img.shape
    out_img=np.zeros_like(img)
    for i in range(0,x):
        for j in range(0,y):
            if img[i][j]<=thres :
                out_img[i][j]=255
            else:
                out_img[i][j]=0
    
    cv2.imshow("Output Image",out_img)
print("Max Pixel:",max)
print("Min Pixel:",min)
thres=int(input("Enter thresold value"))
thresholdsegmentation(img,thres)
cv2.waitKey(0)
cv2.destroyAllWindows()


