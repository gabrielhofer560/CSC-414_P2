"""
Harris Corner Detection algorithm
:param img: image, numpy array
:param kernel: square guassian matrix, w
:param n: size of kernel
:returns: void
"""
import numpy as np

def cornerHarris(img,kernel,n):
    x = conv(img,xsobel)
    y = conv(img,ysobel)

    g = gauss(n)
    xx = x*x
    yy = y*y
    xy = y*x

    r,c = img.shape
    for i in range(r-n):
        for j in range(c-n):
            sxx = xx[i:i+n, j:j+n].sum()
            syy = yy[i:i+n, j:j+n].sum()
            sxy = xy[i:i+n, j:j+n].sum()

            d = (sxx*syy) - (sxy*sxy) 
            t = sxx+syy
            r = det - k * (t*t)

            if r > th: 
                # do something

