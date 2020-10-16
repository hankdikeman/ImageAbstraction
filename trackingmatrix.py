import numpy as np

class track_mat:
    def __init__(self, i_len, j_len):
        self.t_mat = np.full((i_len,j_len), True)
        self.i_length = i_len-1
        self.j_length = j_len-1

    def setTrue(self, i, j):
        if (i <= self.i_length and j <= self.j_length):
            self.t_mat[i,] = True

    def setFalse(self, i, j):
        if (i <= self.i_length and j <= self.j_length):
            self.t_mat[i,j] = False

    def getBool(self, i, j):
        if (i <= self.i_length and j <= self.j_length):
            return self.t_mat[i, j]
        else:
            return False

    def getDim(self):
        return np.shape(self.t_mat)
