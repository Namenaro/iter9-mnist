from A import *
from clicker import *

class DoubleDescriptor:
    def __init__(self, A, B, dx, dy, ub_radius):
        self.A = A
        self.B = B
        self.dx = dx
        self.dy = dy
        self.ub_radius =ub_radius


    def apply(self,pic, xa,ya, topn):
        # эвристика расчета интереса точки А с учетом данных по интересу точки В.
        # самое простое, что можно придумать, это:
        # - пошарить взглядом_В по окрестности-кругу вокруг ожидаемой точки В
        # - найти в ней наиболее топ Н наиболее интереснуых активаций В.
        # - резульаты приложения Аюб к точке это набор из нескольких потовых гипотез о положении Б,
        # координаты лучшей из них, а также новая оценка интересности А на основе лучшей гипотезы.
        # Лучшесть гипотезы пока меняем исключительно по интересу_Б.
        expected_xb = xa + self.dx
        expected_yb = ya + self.dy
        interest_a = self.A.get_likelihood_of_popravka(pic, xa, ya)
        hypotheses = {}
        for radius in range(0,self.ub_radius+1):
            interests_B =[]
            XB, YB = get_coords_at_raduis(expected_xb, expected_yb, radius)
            for i in range(len(XB)):
                interest_b = self.B.get_likelihood_of_popravka(pic, XB[i], YB[i])
                if interest_b>0:


def init_double_descriptor(etalon, x1,y1, x2,y2, side1,side2, checker, pics_for_stat,ub_radius):
    A = init_descriptor(etalon, x1, y1, side1, checker, pics_for_stat, nbins)
    B = init_descriptor(etalon, x2, y2, side2, checker, pics_for_stat, nbins)
    dx = x2-x1
    dy = y2-y1
    AuB = DoubleDescriptor(A, B, dx, dy, ub_radius)
    return AuB

def init_double_descriptor_by_hand(etalon, side1, side2, checker, pics_for_stat,ub_radius):
    x,y =select_coord_on_pic(etalon)
    return init_double_descriptor(etalon, x[0], y[0], x[1], y[1], side1, side2, checker, pics_for_stat,ub_radius)

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
    AuB = init_double_descriptor_by_hand(etalon, side1, side2, checker, pics_for_stat,ub_radius)