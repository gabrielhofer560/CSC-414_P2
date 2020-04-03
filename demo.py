
from gk import gk
from harris import harris
from showKeypoints import showKeypoints
import numpy as np
import sys
from skimage import io
from skimage.color import rgb2gray
from showFeatures import showFeatures
from sift import printH, makeH, sift
from matching import matchSIFT
import cv2
from drawMatches import drawMatches


def demo(imgfile0,imgfile1,rth0,rth1,mth):
    # read image, convert to gray
    #img = io.imread(sys.argv[1]);
    img=io.imread("data/plane.bmp")
    img0 = io.imread(imgfile0)
    img1 = io.imread(imgfile1)

    print("orig0 shape: "+str(img0.shape))
    print("orig1 shape: "+str(img1.shape))

    gry0 = rgb2gray(img0)
    gry1 = rgb2gray(img1)

    print("gray0 shape: "+str(gry0.shape))
    print("gray1 shape: "+str(gry1.shape))
    
    # get list of locations of interest points
    feat0 = harris(gry0,gk(3,3,1),rth0)
    feat1 = harris(gry1,gk(3,3,1),rth1)

    print("number of features0: "+str(len(feat0)))
    print("number of features1: "+str(len(feat1)))
    
    # make sift descriptors
    des0 = sift(gry0,feat0)
    des1 = sift(gry1,feat1)
    
    showFeatures(img0,feat0,des0)
    showFeatures(img1,feat1,des1)
    
    M = matchSIFT(des0,des1,40,mth)
    
    img2 = drawMatches(img0,feat0,img1,feat1,M)
    
    io.imshow( img2,vmin=0,vmax=255,cmap="gray")
    io.show()
    


