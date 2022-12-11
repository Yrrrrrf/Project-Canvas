import numpy as np
import cv2
import matplotlib.pyplot as plt


def plot_histogram(img, title) -> None:
    '''
    Plot the histogram of the image
    :param image: image to plot
    :return: None
    '''
    plt.figure()
    plt.title(f"{title} Histogram")
    for i,col in enumerate(('b','g','r')):
        plt.plot(cv2.calcHist([img],[i],None,[256],[0,256]),color = col)
        plt.xlim([0,256])
    plt.show()



if __name__ == '__main__':
    # path = 'resources\\img\\lena.jpg'
    # path = 'resources\\img\\waterfall.jpg'
    path = 'resources\\img\\rgb_test.jpg'
    img = cv2.imread(path)
    print(img.shape)
    # b, g, r = cv2.split(img)
    # cv2.imshow('original', img)
    # cv2.imshow('r', r)
    # cv2.imshow('g', g)
    # cv2.imshow('b', b)
    plot_histogram(img, 'original')

    cv2.waitKey(0)  # wait for key press

