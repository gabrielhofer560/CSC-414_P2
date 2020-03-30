"""
Harris Corner Detection algorithm
:param img: image, numpy array
:param g: square guassian matrix, w
:th: threshold value for R
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

def harris(img,g,th):
    n=g.shape[0]
    x = ss.convolve2d(img,xsobel)
    y = ss.convolve2d(img,ysobel)    
    xx = x*x
    yy = y*y
    xy = x*y
    r,c = img.shape[0],img.shape[1]
    avgR=0
    R=125
    feat=[]
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
            if R > th: 
                feat.append([i,j])
    avgR /= r*c
    print("average r: "+str(avgR))
    return feat

