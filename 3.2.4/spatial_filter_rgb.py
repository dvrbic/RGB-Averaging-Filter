import numpy as np
import cv2
import math

img = cv2.imread('mandrill.png', 1)

def spatial_filter(img, h, r):
    new_img = img
    valuer = 0
    valueg = 0
    valueb = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[0]):
            if x < r or y < r or (x >= (img.shape[0]-r)) or (y >= (img.shape[1]-r)):
                new_img[x][y][2] = 0
                new_img[x][y][1] = 0
                new_img[x][y][0] = 0
                pass
            else:
                for i in range(-1*r, r+1):
                    for j in range(-1*r, r+1):
                        valuer = valuer + ((img[x+i, y+j][2])*h[r+i, r+j])
                        valueg = valueg + ((img[x+i, y+j][1])*h[r+i, r+j])
                        valueb = valueb + ((img[x+i, y+j][0])*h[r+i, r+j])
                new_img[x][y][2] = valuer
                new_img[x][y][1] = valueg
                new_img[x][y][0] = valueb
                valuer = 0
                valueg = 0
                valueb = 0
    return new_img




r = int(input("Please enter a kernel radius: "))
rad_range = (r * 2) + 1
h = np.zeros((rad_range, rad_range))
for i in range(rad_range):
        for j in range(rad_range):
            h[i,j] = 1/((rad_range)*(rad_range))

out = spatial_filter(img, h, r)
cv2.imwrite('RGB_spatial_filt.png', out)