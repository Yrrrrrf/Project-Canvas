import numpy as np
import cv2


def rotate(img, angle, center=None, scale=1.0) -> np.ndarray:
    '''
    Rotate the image
    :param img: image to rotate
    :param angle: angle to rotate
    :param center: center of rotation
    :param scale: scale of rotation
    :return: rotated image
    '''
    # ! to much bro!!!
    (h, w) = img.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(img, M, (w, h))


def rgb_to_gray(img) -> np.ndarray:
    '''
    Convert the image to grayscale
    :param img: image to convert
    :return: grayscale image
    '''
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def gray_to_rgb(img) -> np.ndarray:
    '''
    Convert the image to RGB
    :param img: image to convert
    :return: RGB image
    '''
    return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)


def vertical_flip(img) -> np.ndarray:
    '''
    Flip the image vertically
    :param img: image to flip
    :return: flipped image
    '''
    return cv2.flip(img, 0)  # 0 = vertical


def horizontal_flip(img) -> np.ndarray:
    '''
    Flip the image horizontally
    :param img: image to flip
    :return: flipped image
    '''
    return cv2.flip(img, 1)  # 1 = horizontal


def invert(img) -> np.ndarray:
    '''
    Invert the image
    :param img: image to invert
    :return: inverted image
    '''
    return 255 - img


def clear_zone(img, x, y, w, h) -> np.ndarray:
    '''
    Clear a zone of the image
    :param img: image to clear
    :param x: x coordinate of the zone
    :param y: y coordinate of the zone
    :param w: width of the zone
    :param h: height of the zone
    :return: cleared image
    '''
    img[y:y + h, x:x + w] = 0
    return img


# ? --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def change_brightness(img, value) -> np.ndarray:
    '''
    Change the brightness of the image
    :param img: image to change brightness
    :param value: value to change brightness
    :return: changed brightness image
    '''
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255  # ? if value > 0, set to 255
    v[v <= lim] += value  # ? if value < 0, subtract from 255
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


def change_contrast(img, value) -> np.ndarray:
    '''
    Change the contrast of the image
    :param img: image to change contrast
    :param value: value to change contrast
    :return: changed contrast image
    '''
    f = 131 * (value + 127) / (127 * (131 - value))
    alpha_c = f
    gamma_c = 127 * (1 - f)
    return cv2.addWeighted(img, alpha_c, img, 0, gamma_c)


def logarithmic_transform(img) -> np.ndarray:
    '''
    Apply logarithmic transform to the image
    :param img: image to apply logarithmic transform
    :return: transformed image
    '''
    c = 255 / np.log(1 + np.max(img))
    return c * np.log(1 + img)


def power_transformation(img, c=1, gamma=1) -> np.ndarray:
    '''
    Apply power transformation to the image
    :param img: image to apply power transformation
    :param c: constant value
    :param gamma: gamma value
    :return: transformed image
    '''
    return c * np.power(img, gamma)


def exponential_transform(img, c=1, gamma=1) -> np.ndarray:
    '''
    Apply exponential transform to the image
    :param img: image to apply exponential transform
    :param c: constant value
    :param gamma: gamma value
    :return: transformed image
    '''
    return c * np.power(gamma, img)


def gamma_correction(img, gamma=1.0) -> np.ndarray:
    '''
    Apply gamma correction to the image
    :param img: image to apply gamma correction
    :param gamma: gamma value
    :return: corrected image
    '''
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype('uint8')
    return cv2.LUT(img, table)


def power_law_transform(img, gamma=1.0) -> np.ndarray:
    '''
    Apply power law transform to the image
    :param img: image to apply power law transform
    :param gamma: gamma value
    :return: transformed image
    '''
    return np.power(img / float(np.max(img)), gamma) * 255


def piecewise_linear_transform(img, r1, s1, r2, s2) -> np.ndarray:
    '''
    Apply piecewise linear transform to the image
    :param img: image to apply piecewise linear transform
    :param r1: first r value
    :param s1: first s value
    :param r2: second r value
    :param s2: second s value
    :return: transformed image
    '''
    out = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] < r1:
                out[i, j] = s1 / r1 * img[i, j]
            elif img[i, j] >= r1 and img[i, j] <= r2:
                out[i, j] = (s2 - s1) / (r2 - r1) * (img[i, j] - r1) + s1
            else:
                out[i, j] = (255 - s2) / (255 - r2) * (img[i, j] - r2) + s2
    return out


if __name__ == '__main__':
    # * Load image
    path = 'resources\\img\\lena.png'
    img = cv2.imread(path)

    # * Test functions
    cv2.imshow('Original', img)
    cv2.imshow('rgb2gray', rgb_to_gray(img))
    # cv2.imshow('Vertical flip', vertical_flip(img))
    # cv2.imshow('Horizontal flip', horizontal_flip(img))
    # cv2.imshow('Invert', invert(img))
    # cv2.imshow('Clear zone', clear_zone(img, 100, 100, 100, 100))
    # cv2.imshow('Brightness', change_brightness(img, 50))
    # cv2.imshow('Contrast', change_contrast(img, 50))
    # # cv2.imshow('Logarithmic transform', logarithmic_transform(img))
    # # cv2.imshow('Power transformation', power_transformation(img))
    # # cv2.imshow('Exponential transform', exponential_transform(img))
    # cv2.imshow('Gamma correction', gamma_correction(img))
    # cv2.imshow('Power law transform', power_law_transform(img))
    # # cv2.imshow('Piecewise linear transform', piecewise_linear_transform(img, 50, 0, 200, 255))


    cv2.waitKey(0)
    cv2.destroyAllWindows()
