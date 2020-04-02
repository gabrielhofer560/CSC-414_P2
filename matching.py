"""
Matching images based on using a 
5x5 window as a feature desciptor.

:param img0
:param img1
:returns list of pairs of indices. each pair is a match.
"""
def naive(img0,img1,f0,f1):
    # convert f0, f1 to maps so that we
    # can easily lookup keypoints
    matches=[]
    r,c=img0.shape 
    for i in range(r-5):
        for j in range(c-5):
            if img0[i:i+5,j:j+5]==img1[i:i+5,j:j+5]:
                matches.append([i,j])

def matchSIFT(img0,img1,f0,f1,d0,d1,theta_th,mag_th):
    matches=[]
    for i in d0:
        for j in d1:
            if abs(i[0]-j[0])<=theta_th and abs(i[1]-j[1])<=mag_th 
            matches.append([i,j])
    return matches



