import numpy as np
def zeroPadding(image):
    h,w=image.shape[:2]
    padded=np.zeros([h+2,w+2],np.uint8)
    for i in range(1,h+1):
        for j in range(1,w+1):
            padded[i][j]=image[i-1][j-1]
    return padded
