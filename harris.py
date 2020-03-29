"""
Harris Corner Detection algorithm
:param img: image, numpy array
:param kernel: square guassian matrix, w
:param n: size of kernel
:k: ...
:th: threshold
:returns: void
"""
import numpy as np

def cornerHarris(img,kernel,n,k,th):
    x = conv(img,xsobel)
    y = conv(img,ysobel)

    g = gauss(n)
    xx = x*x
    yy = y*y
    xy = y*x

    r,c = img.shape
    for i in range(r-n):
        for j in range(c-n):
            sxx = (g * xx[i:i+n, j:j+n]).sum()
            syy = (g * yy[i:i+n, j:j+n]).sum()
            sxy = (g * xy[i:i+n, j:j+n]).sum()

            d = (sxx*syy)-(sxy*sxy) 
            t = sxx+syy
            r = det-k*(t*t)

            if r > th: 

                # do something
				# set pixel to RED






