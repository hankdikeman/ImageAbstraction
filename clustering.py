import numpy as np
from trackingmatrix import track_mat
from math import log

# recursive function to sum and average rgb values in clusters
def rgb_avg_cluster(count, i, j, track_mat, img):
    if(track_mat.getBool(i,j) and count < 50):
        # set tracking matrix at (i,j) to false
        track_mat.setFalse(i,j)
        # calculate top bottom left and right sums if true
        t = rgb_avg_cluster(count+1, i, j+1, track_mat, img)
        b = rgb_avg_cluster(count+1, i, j-1, track_mat, img)
        l = rgb_avg_cluster(count+1, i-1, j, track_mat, img)
        r = rgb_avg_cluster(count+1, i+1, j, track_mat, img)
        # sum up total pixels added
        sum_n = t[2]+b[2]+l[2]+r[2]+1
        # average rgb values
        red = sum([t[0][0]*t[2], b[0][0]*b[2], l[0][0]*l[2], r[0][0]*r[2], img[i,j,0]])/sum_n
        green = sum([t[0][1]*t[2], b[0][1]*b[2], l[0][1]*l[2], r[0][1]*r[2], img[i,j,1]])/sum_n
        blue = sum([t[0][2]*t[2], b[0][2]*b[2], l[0][2]*l[2], r[0][2]*r[2], img[i,j,2]])/sum_n
        # get all indices where color will be reset
        tuple_list = [(i,j)]+t[1]+b[1]+r[1]+l[1]
        # return rgb, tuple list, and count
        return ((red,green,blue), tuple_list, sum_n)
    # return blank values if false
    else:
        return ((0,0,0), [], 0)

def turnCartoon(img, edgemat, imshape):
    # make subarray with slice of image edge detected
    CTimg = img.copy()
    # instantiate new tracking matrix
    tracking_mat = track_mat(imshape[0]-1,imshape[1]-1)
    # write false on edges
    for i in range(imshape[0]-1):
        for j in range(imshape[1]-1):
            if edgemat[i,j] == 1:
                tracking_mat.setFalse(i,j)
                #CTimg[i,j,:] = [0,0,0]
    # average out cluster values
    for i in range(imshape[0]):
        print(chr(27) + "[2J")
        print(str(int(i/imshape[0]*100))+"% \tcomplete: "+("-"*int(i*50/imshape[0]))+("."*int((imshape[0]-i)*50/imshape[0])))
        for j in range(imshape[1]):
            if tracking_mat.getBool(i,j):
                rgb, ind, sum_n = rgb_avg_cluster(0, i, j, tracking_mat, CTimg)
                for r, c in ind:
                    CTimg[r,c,:] = [int(rgb[0]),int(rgb[1]),int(rgb[2])]
                    #CTimg[x[0],x[1],1] = int(cluster[0][1])
                    #CTimg[x[0],x[1],2] = int(cluster[0][2])
    # return modified image
    return CTimg
