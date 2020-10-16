# import numpy
import numpy as np

def to_gray(img, imshape):
    # make new np matrix
    newimg = np.zeros((imshape[0],imshape[1]))

    # average rgb and connvert to grayscale
    for i in range(imshape[0]):
        for j in range(imshape[1]):
            newimg[i,j] = (int(img[i,j,0])+int(img[i,j,1])+int(img[i,j,2]))/3

    return newimg
