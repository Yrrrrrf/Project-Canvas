import numpy as np
import cv2
from enum import Enum


def convolve(img, kernel):
    '''
    Convolve the image with the kernel.
    '''
    # img = cv2.imread(img_path)
    # kernel = np.ones((5, 5), np.float32) / 25
    return np.convolve


class KernelType(Enum):
    '''
    Enum class that contains the types of kernels.
    '''
    BLUR = 0
    SHARPEN = 1
    GAUSSIAN = 2  # nxn matrix
    MEAN = 4
    MEDIAN = 5
    MODE = 6
    LAPLACE = 7
    ORDERED_RANGE = 8  # nxn matrix

