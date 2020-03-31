"""
Author: Gabriel Hofer
Course: CSC-414
Instructor: Dr. Randy Hoover

Step 2: Feature description.

Now that you’ve identified points of interest, the next step is to come up with a descriptor for
the feature centered at each interest point. This descriptor will be the representation you’ll
use to compare features in different images to see if they match.

For starters, try using a small square window (say 5x5) as the feature descriptor. This should
be very easy to implement and should work well when the images you’re comparing are
related by a translation.

Next, try implementing a better feature descriptor. You can define it however you want, but
you should design it to be robust to changes in position, orientation, and illumination. You
are welcome to use techniques described in lecture (e.g., detecting dominant orientations,
using image pyramids), or come up with your own ideas.
"""

"""
returns histogram?
"""
import numpy as np
from gk import gk
import math


def printH(H):
    for i in H: print(str(i)+' ',end='')

def makeH(W):
    H=np.zeros(8)
    for i in range(1,5):
        for j in range(1,5):
            m = math.sqrt((W[i+1,j]-W[i-1,j])**2 + (W[i,j+1]-W[i,j-1])**2)
            theta = math.atan((W[i,j+1]-W[i,j-1]) / (W[i+1,j]-W[i-1,j]))
            norm=math.floor((theta+math.pi/2)*8/math.pi)
            H[norm]+=m
    m=0
    theta=-1
    for i,j in enumerate(H):
        if j>m:
            m=j
            theta=i

    printH(H)

    return [m,theta]

"""
Sift Feature Desciptor
makes HOG: Histogram of Oriented Gradients
:param feat - list of interest points a.k.a. keypoints
:returns 
"""
def sift(img,feat):
    dscr=[]
    print("THIS IS SIFT!")
    for i in feat:
        r,c=i[0],i[1]
        A=np.zeros((4,4,2)) 
        # let's avoid the margins 
        if r<9 or r>img.shape[0]-9 or c<8 or c>img.shape[1]-9:
            continue
        print(i)

        for j in range(4):
            for k in range(4):
                print(gk(6,6,1).shape)
                print(img[r-9+(j*4):r-3+(j*4),c-9+(k*4):c-3+(k*4)].shape)

                print("r1: "+str(r-9+(j*4)))
                print("r2: "+str(r-3+(j*4)))

                print("c1: "+str(c-9+(k*4)))
                print("c2: "+str(c-3+(k*4)))
                
                print(img.shape)

                #A[j,k]=makeH(gk(6,6,1)*img[r-9+(j*4):r-3+(j*4),c-9+(k*4):c-3+(k*4)])
                print("\n----------------------------------------------")
        print("here")

        B=np.zeros(8)
        for j in range(4):
            for k in range(4):
                B[A[j,k,0]]+=A[j,k,1]
        m=0
        theta=-1
        for i,j in enumerate(B):
            if j>m:
                m=j
                theta=i
        dscr.append([m,theta])







