import numpy as np
import cv2
import matplotlib.pyplot as plt


def plot_histogram(img, title: str = '') -> None:
    '''
    Plot the histogram of the image
    :param image: image to plot
    :return: None
    '''
    plt.figure()
    # plt.title(f"{title} Histogram")
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
    r, g, b = cv2.split(img)
    r = cv2.equalizeHist(r)
    g = cv2.equalizeHist(g)
    b = cv2.equalizeHist(b)
    return cv2.merge((r, g, b))  # Equalized image


def resize_img_scale(img, scale: float = 0.4) -> np.ndarray:
    '''
    Resize the image in it's original dimensions.
    This function is on percent scale, so a 100% scale will return the original image
    :param img: image to resize
    :param scale: [%] scale to resize
    :return: resized image
    '''
    return cv2.resize(img, (int(img.shape[1] * scale / 100), int(img.shape[0] * scale / 100)))


def resize_img(img, width: int = 512, height: int = 512) -> np.ndarray:
    '''
    Reisze the image to the given dimensions
    :param img: image to stretch
    :param width: width of the new image
    :param height: height of the new image
    :return: stretched image
    '''
    return cv2.resize(img, (width,  height), interpolation=cv2.INTER_AREA)


# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# wdf ???
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
    # path = 'resources\\img\\lena.png'
    path = 'resources\\img\\color_montains.png'
    img = cv2.imread(path)

    # * Test Histogram Operations
    cv2.imshow('Original', img)
    cv2.imshow('resized_scale', resize_img_scale(img, 120))
    cv2.imshow('resized_w&h', resize_img(img, 240, 360))
    cv2.imshow('equalized', equalize_img(img))
    cv2.imshow('equalized rgb', equalize_hist_rgb(img))


    cv2.waitKey(0)
    cv2.destroyAllWindows()

