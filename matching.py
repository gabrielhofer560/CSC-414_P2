"""
Matching images based on using a 
5x5 window as a feature desciptor.

:param img0
:param img1
:returns list of pairs of indices. each pair is a match.
"""
def naive(img0,img1,f0,f1):
    matches=[]
    for i in f0:
        for j in f1:
            if img0[i[0]-2:i[0]+3,i[1]-2:i[1]+3]==img1[j[0]-2:j[0]+3,j[1]-2:j[1]+3]:
                matches.append([i,j])
    return matches

"""
Matches SIFT descriptors using two threshold values for comparing
similar orientations and magnitudes
:param d0 - descriptor list
:param d1 - descriptor list
:param theta_th - threshold for comparing orientation of descriptors
:param mag_th - threshold for comparing magnitude of descriptors
"""
def matchSIFT(d0,d1,theta_th,mag_th):
    matches=[]
    for idxi, i in enumerate(d0):
        for idxj, j in enumerate(d1):
            if abs(i[0]-j[0])<theta_th and abs(i[1]-j[1])<mag_th:
                matches.append([idxi,idxj])
    return matches


