from A import *
from clicker import *
from utils import *

import operator


class DoubleDescriptor:
    def __init__(self, A, B, dx, dy, ub_radius):
        self.A = A
        self.B = B
        self.dx = dx
        self.dy = dy
        self.ub_radius =ub_radius


    def apply(self,pic, xa,ya):
        # эвристика расчета интереса точки А с учетом данных по интересу точки В.
        # самое простое, что можно придумать, это:
        # - пошарить взглядом_В по окрестности-кругу вокруг ожидаемой точки В
        # - найти в ней все активации В - нормированные поправки.
        # - найти лучшую поправку Б и пересчитать поправку А: сложить
        # поправки А и В и поделить на два: это и есть новая оценка возможности
        # нахождения точки А в координатах xa,ya. Функция
        # возвращает новую оценку А (число) + относительные координаты места + набор гипотез о
        # местонахождении В: это словарь, в котором ключи координаты,
        # а значения это новая оценка А через данное В.
        expected_xb = xa + self.dx
        expected_yb = ya + self.dy

        abs_popravka_a = self.A.get_abs_popravka_at_point(pic, xa, ya)
        if abs_popravka_a is None:
            return None, None, None, None

        normed_a = self.A.get_normed_popravka_at_point(abs_popravka_a)

        hypotheses = {}

        XB, YB = get_coords_less_or_eq_raduis(expected_xb, expected_yb, self.ub_radius)
        for i in range(len(XB)):
            abs_popravka_b = self.B.get_abs_popravka_at_point(pic, XB[i], YB[i])
            if abs_popravka_b is not None:
                normed_b = self.B.get_normed_popravka_at_point(abs_popravka_b)
                A_reevaluated = normed_b + normed_a
                hypotheses[(XB[i]-expected_xb, YB[i]-expected_yb)] = A_reevaluated
        # находим лучшее Б
        val, ddx, ddy = find_best_hypothesys(hypotheses)
        return val, ddx, ddy, hypotheses

def find_best_hypothesys(dict_hypotheses):
    sorted_hypos = sorted(dict_hypotheses, key=operator.itemgetter(1))
    best_hypo = sorted_hypos[0]
    dx= best_hypo[0]
    dy = best_hypo[1]
    val = dict_hypotheses[best_hypo]
    return val, dx, dy

def init_double_descriptor(etalon, x1,y1, x2,y2, side1,side2, checker, pics_for_stat,ub_radius, nbins):
    A = init_descriptor(etalon, x1, y1, side1, checker, pics_for_stat, nbins)
    B = init_descriptor(etalon, x2, y2, side2, checker, pics_for_stat, nbins)
    dx = x2-x1
    dy = y2-y1
    AuB = DoubleDescriptor(A, B, dx, dy, ub_radius)
    return AuB

def init_double_descriptor_by_hand(etalon, side1, side2, checker, pics_for_stat,ub_radius, nbins):
    x,y =select_coord_on_pic(etalon)
    return init_double_descriptor(etalon, x[0], y[0], x[1], y[1], side1, side2, checker, pics_for_stat,ub_radius, nbins)

if __name__ == "__main__":
    from data import *
    from checkers import *

    etalon = etalons_of3()[0]
    pics_for_stat = get_diverse_set_of_numbers(20)
    side1 = 4
    side2 = 4
    checker = check_mean
    nbins = 10
    ub_radius=2
    nbins=10
    AuB = init_double_descriptor_by_hand(etalon, side1, side2, checker, pics_for_stat,ub_radius, nbins)
    AuB.apply(etalon, 10, 20)