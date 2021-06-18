from utils import *
import numpy as np

def slide_checker(pic, side, checker):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    pad_left = int(side / 2)
    pad_right = side - (pad_left + 1)
    res = np.zeros((ymax-side+1, xmax-side+1))
    for centery in range(pad_left, ymax-pad_right):
        for centerx in range(pad_left, xmax-pad_right):
            sensory_array = get_sensory_array(pic, centerx, centery, side)
            value = checker(sensory_array)
            res[centery-pad_left, centerx-pad_left] = value
    return res

def slide_descriptor_A(pic, A, likelihood_thr=1):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    pad_left = int(A.side / 2)
    pad_right = A.side - (pad_left + 1)
    res = np.zeros((ymax - A.side + 1, xmax - A.side + 1))
    for centery in range(pad_left, ymax - pad_right):
        for centerx in range(pad_left, xmax - pad_right):
            likelihood = A.get_likelihood_at_point(pic, centerx, centery)
            interest=0
            if likelihood <=likelihood_thr:
                 interest = 1-likelihood
            res[centery - pad_left, centerx - pad_left] = interest
    return res