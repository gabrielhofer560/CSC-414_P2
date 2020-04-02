"""
Author: Gabriel Hofer
Course: CSC-414
Instructor: Dr. Randy Hoover
"""

import numpy as np
from gk import gk
import math


def printH(H):
    for i in H: print(str(i)+' ',end='')
    print()

def makeH(W):
    H=np.zeros(8)
    for i in range(1,5):
        for j in range(1,5):
            m = math.sqrt((W[i+1,j]-W[i-1,j])**2 + (W[i,j+1]-W[i,j-1])**2)
            if W[i,j+1] != W[i,j-1] and W[i+1,j] != W[i-1,j]: 
                theta = math.atan2((W[i+1,j]-W[i-1,j]), (W[i,j+1]-W[i,j-1]))
            else: continue
            norm=int(math.floor((theta+math.pi)*8/(2*math.pi))%8)
            H[norm]+=m
    m=0
    theta=-1
    for i,j in enumerate(H):
        if j>m:
            m=j
            theta=i
    return [theta,m]

"""
Sift Feature Desciptor
makes HOG: Histogram of Oriented Gradients
:param feat - list of interest points a.k.a. keypoints
:returns 
"""
def sift(img,feat):
    sift=[]
    for i in feat:
        r,c=i[0],i[1]
        A=np.zeros((4,4,2)) 
        if r<9 or r>img.shape[0]-9 or c<8 or c>img.shape[1]-9:
            continue
        for j in range(4):
            for k in range(4):
                A[j,k]=makeH(gk(6,6,1)*img[r-9+(j*4):r-3+(j*4),c-9+(k*4):c-3+(k*4)])
        B=np.zeros(8)
        for j in range(4):
            for k in range(4):
                B[int(A[j,k,0])]+=A[j,k,1]
        m=0
        theta=-1
        for i,j in enumerate(B):
            if j>m:
                m=j
                theta=i
        sift.append([theta,m])
    return sift


"""
find better way to map features to the corresponding descriptors
"""

