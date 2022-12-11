import numpy as np
import cv2


def kernel_filter(img, kernel) -> np.ndarray:
    '''
    Apply a kernel filter to the image
    :param img: image to filter
    :param kernel: kernel
    :return: filtered image
    '''
    return cv2.filter2D(img, -1, kernel)


# todo: implement kernel size
def sharpen_filter(img) -> np.ndarray:
    '''
    Apply a sharpen filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(img, -1, kernel)


def gaussian_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a gaussian filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def mean_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a mean filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    return cv2.blur(img, (kernel_size, kernel_size))


def median_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a median filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    return cv2.medianBlur(img, kernel_size)


def ordered_range_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply an ordered range filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    # todo: implement ordered range filter
    return img


def laplacian_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a laplacian filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    return cv2.Laplacian(img, cv2.CV_64F, ksize=kernel_size)


def bilateral_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a bilateral filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    return cv2.bilateralFilter(img, kernel_size, 75, 75)


def sobel_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a sobel filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    return cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=kernel_size)


def emboss_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a emboss filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
    return cv2.filter2D(img, -1, kernel)


def edge_filter(img, kernel_size) -> np.ndarray:
    '''
    Apply a edge filter to the image
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    kernel = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])
    return cv2.filter2D(img, -1, kernel)


def absurd_filter(img) -> np.ndarray:
    '''
    Apply a absurd filter to the image. This filter is not a real filter, it is just for testing purposes
    :param img: image to filter
    :param kernel_size: kernel size
    :return: filtered image
    '''
    kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    return cv2.filter2D(img, -1, kernel)


# def n_filter(img, kernel_size) -> np.ndarray:
#     '''
#     Apply a n filter to the image
#     :param img: image to filter
#     :param kernel_size: kernel size
#     :return: filtered image
#     '''
#     kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)  
#     return cv2.filter2D(img, -1, kernel)



# ? MAIN ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # * Load image
    path = 'resources\\img\\lena.png'
    img = cv2.imread(path)

    # * Test Convolutions
    cv2.imshow('Original', img)
    cv2.imshow('Sharpen', sharpen_filter(img))  # just 3x3 kernel
    cv2.imshow('Gaussian', gaussian_filter(img, 3))
    cv2.imshow('Mean', mean_filter(img, 3))
    cv2.imshow('Median', median_filter(img, 3))
    cv2.imshow('Laplacian', laplacian_filter(img, 3))
    # cv2.imshow('Ordered Range', ordered_range_filter(img, 3))
    # cv2.imshow('Bilateral', bilateral_filter(img, 3))
    cv2.imshow('Sobel', sobel_filter(img, 3))
    cv2.imshow('Emboss', emboss_filter(img, 3))
    cv2.imshow('Edge', edge_filter(img, 3))
    cv2.imshow('Absurd', absurd_filter(img))
    # cv2.imshow('N', n_filter(img, 3))


    cv2.waitKey(0)
    cv2.destroyAllWindows()
