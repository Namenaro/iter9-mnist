from checkers import *
from slider import *
from utils import *
import matplotlib.pyplot as plt
import numpy as np


def count_statistics_popravs_for_checker(checker, etalon_val, side, pics_for_stat, n_bins):
    popravs = np.array([])
    for pic in pics_for_stat:
        activations_on_pic = slide_checker(pic, side, checker).flatten()
        popravs_on_pic = np.absolute(activations_on_pic - etalon_val)
        popravs = np.concatenate([popravs, popravs_on_pic])
    (probs, bins, _) = plt.hist(popravs, bins=n_bins,
                                weights=np.ones_like(popravs) / len(popravs), range=(0 ,popravs.max()))
    plt.show()
    return bins, probs

