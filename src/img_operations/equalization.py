import numpy as np
import cv2 as cv

path = 'resources\\static\\brush_256.png'


def equalize_hist(img) -> np.ndarray:
    '''
    Equalize the histogram of the image
    :param img: image to equalize
    :return: equalized image
    '''
    r, g, b = cv.split(img)
    r = cv.equalizeHist(r)
    g = cv.equalizeHist(g)
    b = cv.equalizeHist(b)
    return cv.merge((r, g, b))  # Equalized image


if __name__ == '__main__':
    img = cv.imread(path)
    cv.imshow('image', img)
    cv.imshow('equalized', equalize_hist(img))
    

    cv.waitKey(0)
