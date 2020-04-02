"""
draw lines showing feature matches

"""
import cv2
import math
import numpy as np

def drawLine(img,one,two,c,th):
    x0,y0=one
    x1,y1=two
    if x0==x1: return
    dx=x1-x0
    dy=y1-y0
    print(str(one)+" "+str(two))
    for x in range(x0,x1+1):
        y = y0+((dy*(x-x0))/dx)
        img[int(x),int(y)]=c


from showDots import showDots 
from skimage import io

def drawMatches(img0,kp0,img1,kp1,matches):

    img2 = np.zeros((
        max(img0.shape[0],img1.shape[0]),
        img0.shape[1]+img1.shape[1],
        3),np.uint(8))

    img2[0:img0.shape[0],0:img0.shape[1]] = img0
    img2[0:img1.shape[0],img0.shape[1]:img0.shape[1]+img1.shape[1]] = img1


#    showDots(img2,kp0)
#    io.imshow(img2)
#    io.show()

    cpy=list(kp1)
    nkp1=[]
    # translate coordinate of right image
    for i in range(len(kp1)):
        nkp1.append([kp1[i][0],img0.shape[1]+kp1[i][1]])
        #kp1[i][1]=img0.shape[1]+kp1[i][1]

#    showDots(img2,kp1)
#    io.imshow(img2)
#    io.show()

    for i in range(len(kp1)):
        one,two = kp1[i], nkp1[i]
        print(one)
        print(two)
        drawLine(img2,one,two,[0,0,255],2)

    return img2


    for [i,j] in matches:
        one,two = kp1[i], nkp1[j]
        drawLine(img2,one,two,[0,0,255],2)

    return img2



