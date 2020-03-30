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
def makeH(window):
    H=np.zeros(8)
    return H


"""
sift feature desciptor
:param feat - list of interest points a.k.a. keypoints
:returns something...
"""
def sift(img,feat):
    # make HOG: histogram of oriented gradients
    for i in feat:
        # 16x16 window of 16 4x4 sub-windows
        r,c=i[0],i[1]
        A=np.zeros((4,4))
        for j in range(4):
            for k in range(4):
                A[j,k]=makeH([(img[r-8+(j*4):r-4+(j*4),c-8+(k*4):c-4+(k*4)]))
        





