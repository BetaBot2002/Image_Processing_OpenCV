import numpy as np
import cv2
def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col))
      gauss = gauss.reshape(row,col)
      noisy = image + gauss
      return noisy
image = cv2.imread('Taj.jpg',0)
noise=noisy('gauss',image)
cv2.imshow('Noise',noise)
cv2.waitKey(0)
