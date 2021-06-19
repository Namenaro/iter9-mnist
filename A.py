from hists import *
class Descriptor:
    def __init__(self, side, checker):
        self.checker = checker
        self.side = side
        self.etalon_val = None
        self.bins = None
        self.likelihoods = None

    def eval_likelihood_of_popravka(self, popravka):
        for i in range(0, len(self.bins)-1):
            if popravka >= self.bins[i] and popravka < self.bins[i+1]:
                return self.likelihoods[i]
        return None

    def get_abs_popravka_at_point(self, pic, x, y):
        sensory_array = get_sensory_array(pic, x, y, side)
        if sensory_array is None:
            return None
        value = checker(sensory_array)
        popravka = abs(self.etalon_val - value)
        return popravka

    def get_normed_popravka_at_point(self,pic, x, y):
        popravka = self.get_abs_popravka_at_point( pic, x, y)
        max_popravka = self.bins[-1]
        normed_popravka = popravka/max_popravka
        return normed_popravka # belongs to [0,1]

def init_descriptor(etalon, x, y, side, checker, pics_for_stat, nbins):
    A = Descriptor(side, checker)
    sensory_array = get_sensory_array(etalon, x, y, side)
    if sensory_array is None:
        return None
    A.etalon_val = A.checker(sensory_array)
    bins, probs = count_statistics_popravs_for_checker(checker, A.etalon_val, side, pics_for_stat, nbins)
    A.bins = bins
    A.likelihoods = probs
    return A


if __name__ == "__main__":
    from data import *
    from checkers import *
    from visualisation_data import *
    etalon = etalons_of3()[0]
    pics_for_stat = get_diverse_set_of_numbers(20)
    x=5
    y=20
    side=4
    checker = check_mean
    nbins=10
    descr = init_descriptor(etalon, x, y, side, checker, pics_for_stat,nbins)
    print(descr.get_likelihood_of_popravka(etalon, x, y))

    pic2=slide_descriptor_A(etalon, descr, 0.1)
    show_2_gray_pics(etalon, pic2)



