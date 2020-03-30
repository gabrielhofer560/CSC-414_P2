"""
Harris Corner Detection algorithm
:param img: image, numpy array
:param g: square guassian matrix, w
:param n: size of kernel
:k: ...
:th: threshold
:returns: void
"""
import numpy as np
from imfilter import imfilter
import scipy.signal as ss


xsobel = np.array([
    [1,0,-1],
    [2,0,-2],
    [1,0,-1]])

ysobel = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]])

def harris(img,g,n,th):
    x = ss.convolve2d(img,xsobel)
    y = ss.convolve2d(img,ysobel)    

    xx = x*x
    yy = y*y
    xy = x*y
    
    r,c = img.shape[0],img.shape[1]
    avgR=0
    R=125
    for i in range(r-n):
        for j in range(c-n):
            sxx = (g * xx[i:i+n, j:j+n]).sum()
            syy = (g * yy[i:i+n, j:j+n]).sum()
            sxy = (g * xy[i:i+n, j:j+n]).sum()
            
            d = (sxx*syy)-(sxy*sxy) 
            t = sxx+syy

            if t!=0:
                R = d/t
            avgR+=R
            
            if R > 0.005: 
                img[i,j]=0
                # set pixel to RED
                # img[i,j,:]=[0,0,255]

    avgR /= r*c
    print("average r: "+str(avgR))
    return img



