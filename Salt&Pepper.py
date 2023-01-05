import random
import cv2
import numpy as np
def add_noise(img):
	row,col = img.shape[:2]
	number_of_pixels = random.randint(300, 400)
	for i in range(number_of_pixels):
		y_coord=random.randint(0, row - 1)
		x_coord=random.randint(0, col - 1)
		img[y_coord][x_coord] = 255
	number_of_pixels = random.randint(300 , 10000)
	for i in range(number_of_pixels):
		y_coord=random.randint(0, row - 1)
		x_coord=random.randint(0, col - 1)
		img[y_coord][x_coord] = 0
	return img
image = cv2.imread('RGB.jpg',0)
im1=add_noise(image)
cv2.imshow('Noisy one',im1)
cv2.waitKey(0)

