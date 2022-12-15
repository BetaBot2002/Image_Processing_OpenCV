import cv2
img=cv2.imread('Demo.jpg')
	
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('kaka',gray)

cv2.waitKey(0)