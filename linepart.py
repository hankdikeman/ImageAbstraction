# import numpy
import numpy as np


def geom_diff(rgb1, rgb2):
    # return geometric mean of differences
    return abs(int(rgb1[0]) - int(rgb2[0])) + abs(int(rgb1[1]) - int(rgb2[1])) + abs(int(rgb1[2]) - int(rgb2[2]))


def partition_img(img, imshape, dlim=30):
    # make edge matrix
    edge_detected = np.zeros((imshape[0] - 1, imshape[1] - 1))

    # loop over array
    for i in range(imshape[0] - 1):
        for j in range(imshape[1] - 1):
            diag = geom_diff(img[i, j], img[i + 1, j + 1])
            right = geom_diff(img[i, j], img[i + 1, j + 1])
            under = geom_diff(img[i, j], img[i + 1, j + 1])
            if (diag > dlim or right > dlim or under > dlim):
                edge_detected[i, j] = 1

    # send up edge detected matrix
    return edge_detected


def convo_edge_det(img, imshape, dlim=30):
    # make edge matrix
    edge_detected = np.ones((imshape[0] - 2, imshape[1] - 2))
    # construct edge detection filter
    filter = np.full((3, 3), -1)
    filter[1, 1] = 8
    print(filter)
    # loop over array
    for i in range(imshape[0] - 2):
        for j in range(imshape[1] - 2):
            print(img[i:i + 3, j:j + 3, :])
            rgb_sum = np.sum(filter * img[i:i + 3, j:j + 3, :], axis=2)
            tot_sum = np.sum(np.absolute(rgb_sum))
            if(tot_sum > dlim):
                print((tot_sum, dlim))
                edge_detected[i, j] = 1

    # send up edge detected matrix
    return edge_detected
