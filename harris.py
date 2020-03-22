"""
Harris Corner Detection algorithm
------------------------------------------
param img: image, numpy array
param kernel: square guassian matrix, w
param n: size of kernel
"""
import numpy as np

def cornerHarris(img,kernel,n):
    # get img's shape and dimensions

    # create sobel derivatives Ixy, Iyx, Ix2, Iy2
    Ix = imfilter(img,xsobel)
    Iy = imfilter(img,ysobel)

    Iy2 = imfilter(Iy,ysobel)
    Ix2 = imfilter(Ix,xsobel)

    Ixy = imfilter(Ix,ysobel)
    Iyx = imfilter(Iy,xsobel)
    
    # create w (gaussian mask) by calling gauss from gauss.py 
    w = gauss(n,n,1)
    
    # calculate H 
    for x in range(r-n):
        for y in range(c-n):
            H = np.zeros((n,n)) 
            for i in range(n):
                for j in range(n):
                    H += w[i][j] * img[x+i:x+i+n][y+j:x+j+n]

            R = np.linalg.det(H) / np.trace(H)

            # use R to determine significance of point...?



    # create thresholding function for corner c(H)
  










