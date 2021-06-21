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

def slide_descriptor_A(pic, A, getval):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    pad_left = int(A.side / 2)
    pad_right = A.side - (pad_left + 1)
    res = np.zeros((ymax - A.side + 1, xmax - A.side + 1))
    for centery in range(pad_left, ymax - pad_right):
        for centerx in range(pad_left, xmax - pad_right):
            val = getval(pic, centerx, centery)
            res[centery - pad_left, centerx - pad_left] = val
    return res

def reeval_A_by_B(AuB, pic):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    pad_left = int(AuB.A.side / 2)
    pad_right = AuB.A.side - (pad_left + 1)
    res = np.zeros((ymax - AuB.A.side + 1, xmax - AuB.A.side + 1))
    for centery in range(pad_left, ymax - pad_right):
        for centerx in range(pad_left, xmax - pad_right):
            val, ddx, ddy, hypotheses = AuB.apply(pic, centerx, centery)
            res[centery - pad_left, centerx - pad_left] = val
    return res