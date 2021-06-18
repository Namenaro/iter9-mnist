from data import *
import matplotlib.pyplot as plt

def draw_several(np_images, np_labels, rows = 5, cols = 7):
    num_of_images = rows*cols
    for index in range(1, num_of_images + 1):
        plt.subplot(rows, cols, index)
        plt.axis('off')
        if np_labels is not None:
            plt.title(np_labels[index-1])
        plt.imshow(np_images[index-1].squeeze(), cmap='gray_r')
    plt.show()

def show_2_gray_pics(pic1, pic2):

    fig = plt.figure()
    plt.gray()  # show the filtered result in grayscale
    ax1 = fig.add_subplot(121)  # left side
    ax2 = fig.add_subplot(122)  # right side
    ax1.imshow(pic1)
    ax2.imshow(pic2)
    plt.show()


def show_parad_of_the_number(the_number):
    np_images = get_numbers_of_type(the_number)
    np_labels = list(range(0, len(np_images)-1))
    i=0
    while True:
        draw_several(np_images[i:i+35], np_labels[i:i+35], rows= 5, cols=7)
        i=i+35