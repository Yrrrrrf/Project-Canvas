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


def equalize_img(img) -> np.ndarray:
    '''
    Equalize the histogram of the image
    :param img: image to equalize
    :return: equalized image
    '''
    # or sliding the r g b channels
    # b, g, r = cv2.split(img)
    # b = cv2.equalizeHist(b)
    # g = cv2.equalizeHist(g)
    # r = cv2.equalizeHist(r)
    # return cv2.merge((b, g, r))
    return cv2.equalizeHist(img)


def shrink_img(img, scale) -> np.ndarray:
    '''
    Shrink the image
    :param img: image to shrink
    :param scale: scale to shrink
    :return: shrunk image
    '''
    return cv2.resize(img, (0, 0), fx=scale, fy=scale)


def stretch_img(img, scale) -> np.ndarray:
    '''
    Stretch the image
    :param img: image to stretch
    :param scale: scale to stretch
    :return: stretched image
    '''
    return cv2.resize(img, (0, 0), fx=scale, fy=scale)


# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????


def equalize_hist_rgb(img) -> np.ndarray:
    '''
    Equalize the histogram of the image
    :param img: image to equalize
    :return: equalized image
    '''
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)





# ? MAIN -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # * Load image
    path = 'resources\\img\\lena.png'
    img = cv2.imread(path)

    # todo: implement tests

    cv2.waitKey(0)
    cv2.destroyAllWindows()
