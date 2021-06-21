# цели эксперимента:
# - показать, как "затухает" поле А вцелом при учете одного Б
# - ответить на вопрос, какой выбор А и Б позволяет полю А затухнуть сильнее
# - посмотреть, такое ли эффективное затухание поля А наблюдается на остальных эталонах серии
# - проверить наличие следующего гипотетического эффекта: что при слишком
# маленьком радиусе затухание поля А на других эталонах будет "катастрофическим"
# (т.е. не останется ни одного живого кандидата на точку А). Тактическая задача: нащупать правило
# подбора радиуса, как обучаемого параметра модели АюБ.

from data import *
from utils import *
from AB import *

def get_several_etalons():
    etalons = etalons_of3()
    etalons = make_padded_dataset(etalons, padding=7)
    return etalons[0:4]

def get_A_field_on_etalon(A, etalon):
    pic2 = slide_descriptor_A(etalon, A, A.get_abs_popravka_at_point)
    return pic2

def get_AB_field_on_etalon(AB, etalon):
    return etalon

def visualise_all_fields(etalons, Afields, ABfields):
    rows = 3
    cols = len(etalons)
    fig, axs = plt.subplots(rows, cols,sharex=True, sharey=True)

    for i in range(len(etalons)):
        axs[0,i].imshow(etalons[i])
        axs[1, i].imshow(Afields[i])
        axs[2, i].imshow(ABfields[i])
    plt.show()

def make_experiment(ub_radius):
    etalons = get_several_etalons()
    main_etalon = etalons[0]
    pics_for_stat = get_diverse_set_of_numbers(20)
    side1 = 4
    side2 = 4
    checker = check_mean
    nbins =10
    #AuB = init_double_descriptor_by_hand(main_etalon, side1, side2, checker, pics_for_stat, ub_radius, nbins)
    AuB = init_double_descriptor(main_etalon, 20, 10, 10, 15, side1, side2, checker, pics_for_stat, ub_radius, nbins)

    Afields = []
    ABfields = []
    for etalon in etalons:
        Afield = get_A_field_on_etalon(AuB.A, etalon)
        Afields.append(Afield)
        ABfield = get_AB_field_on_etalon(AuB, etalon)
        ABfields.append(ABfield)
    visualise_all_fields(etalons, Afields, ABfields)

if __name__ == "__main__":
    make_experiment(ub_radius=2)





