import numpy as np
import cv2


def gaussian_noise(img, mean=0, sigma=0.1) -> np.ndarray:
    '''
    Add gaussian noise to the image
    :param img: image to add noise
    :param mean: mean of the noise
    :param sigma: standard deviation of the noise
    :return: noisy image
    '''
    row, col, ch = img.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = img + gauss
    return noisy


def salt_noise(img, prob=0.05) -> np.ndarray:
    '''
    Add salt noise to the image
    :param img: image to add noise
    :param prob: probability of the noise
    :return: noisy image
    '''
    output = np.zeros(img.shape, np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    return output


def pepper_noise(img, prob=0.05) -> np.ndarray:
    '''
    Add pepper noise to the image
    :param img: image to add noise
    :param prob: probability of the noise
    :return: noisy image
    '''
    output = np.zeros(img.shape, np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 0
            else:
                output[i][j] = img[i][j]
    return output


def salt_pepper_noise(img, prob=0.05) -> np.ndarray:
    '''
    Add salt and pepper noise to the image
    :param img: image to add noise
    :param prob: probability of the noise
    :return: noisy image
    '''
    output = np.zeros(img.shape, np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    return output


def speckle_noise(img, prob=0.05) -> np.ndarray:
    '''
    Add speckle noise to the image
    :param img: image to add noise
    :param prob: probability of the noise
    :return: noisy image
    '''
    row, col, ch = img.shape
    gauss = np.random.randn(row, col, ch)
    gauss = gauss.reshape(row, col, ch)
    noisy = img + img * gauss
    return noisy


def rayleigh_noise(img, sigma=0.1) -> np.ndarray:
    '''
    Add rayleigh noise to the image
    :param img: image to add noise
    :param sigma: sigma of the rayleigh distribution
    :return: noisy image
    '''
    noisy = np.random.rayleigh(sigma, img.shape) + img
    return noisy


def laplace_noise(img, loc=0, scale=0.1) -> np.ndarray:
    '''
    Add laplace noise to the image
    :param img: image to add noise
    :param loc: location of the laplace distribution
    :param scale: scale of the laplace distribution
    :return: noisy image
    '''
    noisy = np.random.laplace(loc, scale, img.shape) + img
    return noisy


def poisson_noise(img, lambd=0.1) -> np.ndarray:
    '''
    Add poisson noise to the image
    :param img: image to add noise
    :param lambd: lambda of the poisson distribution
    :return: noisy image
    '''
    noisy = np.random.poisson(lambd, img.shape) + img
    return noisy


def uniform_noise(img, a=-0.5, b=0.5) -> np.ndarray:
    '''
    Add uniform noise to the image
    :param img: image to add noise
    :param a: lower bound of the uniform distribution
    :param b: upper bound of the uniform distribution
    :return: noisy image
    '''
    row, col, ch = img.shape
    gauss = np.random.uniform(a, b, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = img + gauss
    return noisy


def exponential_noise(img, lambd=0.1) -> np.ndarray:
    '''
    Add exponential noise to the image
    :param img: image to add noise
    :param lambd: lambda of the exponential distribution
    :return: noisy image
    '''
    noisy = np.random.exponential(lambd, img.shape) + img
    return noisy



if __name__ == '__main__':
    # * Load image
    path = 'resources\\img\\lena.png'
    img = cv2.imread(path)

    # * Test noise
    cv2.imshow('original', img)
    # cv2.imshow('gaussian noise', gaussian_noise(img))
    cv2.imshow('s&p noise', salt_pepper_noise(img))
    cv2.imshow('salt noise', salt_noise(img))
    cv2.imshow('pepper noise', pepper_noise(img))
    cv2.imshow('speckle noise', speckle_noise(img))
    # cv2.imshow('rayleigh noise', rayleigh_noise(img))
    # cv2.imshow('laplace noise', laplace_noise(img))
    # cv2.imshow('poisson noise', poisson_noise(img))
    # cv2.imshow('uniform noise', uniform_noise(img))
    # cv2.imshow('exponential noise', exponential_noise(img))


    cv2.waitKey(0) 
    cv2.destroyAllWindows()
