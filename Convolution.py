def Convolve(img, mask):
    convolved=img.copy()
    h,w=img.shape[:2]
    for i in range(1,h-1):
            for j in range(1,w-1):
                        convolved[i][j] =abs((img[i-1][j-1]*mask[0][0])+(img[i-1][j]*mask[0][1])+(img[i-1][j+1]*mask[0][2])+(img[i][j-1]*mask[1][0])+(img[i][j]*mask[1][1])+(img[i][j+1]*mask[1][2])+(img[i+1][j-1]*mask[2][0])+(img[i+1][j]*mask[2][1])+(img[i+1][j+1]*mask[2][2]))
    return convolved
