import cv2
import numpy as np

img=cv2.imread('Demo.jpg',0)

imgRotate=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Rotate',imgRotate)

cv2.waitKey(0)