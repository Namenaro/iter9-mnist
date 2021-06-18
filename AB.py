from A import *
from clicker import *

class DoubleDescriptor:
    def __init__(self, A, B, dx, dy):
        self.A = A
        self.B = B
        self.dx = dx
        self.dy = dy

def init_double_descriptor(etalon, x1,y1, x2,y2, side1,side2, checker, pics_for_stat):
    A = init_descriptor(etalon, x1, y1, side1, checker, pics_for_stat, nbins)
    B = init_descriptor(etalon, x2, y2, side2, checker, pics_for_stat, nbins)
    dx = x2-x1
    dy = y2-y1
    AuB = DoubleDescriptor(A, B, dx, dy)
    return AuB

def init_double_descriptor_by_hand(etalon, side1, side2, checker, pics_for_stat):
    x,y =select_coord_on_pic(etalon)
    return init_double_descriptor(etalon, x[0], y[0], x[1], y[1], side1, side2, checker, pics_for_stat)

if __name__ == "__main__":
    from data import *
    from checkers import *

    etalon = etalons_of3()[0]
    pics_for_stat = get_diverse_set_of_numbers(20)
    side1 = 4
    side2 = 4
    checker = check_mean
    nbins = 10
    AuB = init_double_descriptor_by_hand(etalon, side1, side2, checker, pics_for_stat)