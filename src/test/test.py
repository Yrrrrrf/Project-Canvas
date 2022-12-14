import src.img_operations.convolution as convolution
import src.img_operations.histogram as histogram
import src.img_operations.noise as noise
import src.img_operations.pixel as pixel
import cv2 as cv
import unittest


readImage = cv.imread('resources\\img\\lena.png')


class TestHistogram(unittest.TestCase):
    '''
    Test the histogram module.
    '''
    # def test_hisogram(self):
    #     self.test_equalize_img()
    #     self.test_equalize_hist_rgb()
    #     self.test_resize_img_scale()
    #     self.test_resize_img()
    
    def test_equalize_img(self):
        self.assertEqual(histogram.equalize_img(readImage), None)

    def test_equalize_hist_rgb(self):
        self.assertEqual(histogram.equalize_hist_rgb(readImage), None)

    def test_resize_img_scale(self):
        self.assertEqual(histogram.resize_img_scale(readImage, 100), None)

    def test_resize_img(self):
        self.assertEqual(histogram.resize_img(readImage, 100, 100), None)


# todo: implement main thest function
def test_operations():
    '''
    Test the operations module.
    '''
    test_resources()
    test_pixel()
    test_convolutions()
    test_histogram()
    test_noise()


def test_resources():
    '''
    Test the resources module. Shloud be done if all the resources are available
    '''
    # todo: implement tests
    # load_resources() ...
    pass


def test_pixel():
    '''
    Test the pixel module.
    '''
    assert pixel.vertical_flip(None) is None
    assert pixel.horizontal_flip(None) is None
    assert pixel.invert
    assert pixel.clear_zone(None, 1, 1, 1, 1) is None
    assert pixel.change_brightness(None, 1) is None
    assert pixel.change_contrast(None, 1) is None
    assert pixel.logarithmic_transform(None) is None
    assert pixel.exponential_transform(None) is None
    assert pixel.gamma_correction(None, 1) is None
    assert pixel.power_law_transform(None, 1) is None
    assert pixel.piecewise_linear_transform(None, 1, 1, 1, 1) is None


def test_convolutions():
    '''
    Test the convolutions module.
    '''
    assert convolution.absurd_filter(None) is None
    assert convolution.sharpen_filter(None) is None 
    assert convolution.gaussian_filter(None, 1) is None
    assert convolution.mean_filter(None, 1) is None
    assert convolution.median_filter(None, 1) is None
    assert convolution.laplacian_filter(None, 1) is None
    assert convolution.ordered_range_filter(None, 1) is None
    assert convolution.bilateral_filter(None, 1) is None
    assert convolution.sobel_filter(None, 1) is None
    assert convolution.emboss_filter(None, 1) is None
    assert convolution.edge_filter(None, 1) is None


def test_histogram():
    '''
    Test the histogram module.
    '''
    # todo: implement histogram test!
    assert histogram.equalize_img(None) is None
    assert histogram.equalize_hist_rgb(None) is None
    # assert histogram.resize_img_scale(None) is None
    # assert histogram.resize_img(None) is None



def test_noise():
    '''
    Test the noise module.
    '''
    assert noise.gaussian_noise(None, 1) is None
    assert noise.salt_noise(None, 1) is None    
    assert noise.pepper_noise(None, 1) is None    
    assert noise.salt_pepper_noise(None, 1) is None
    assert noise.speckle_noise(None, 1) is None    
    assert noise.rayleigh_noise(None, 1) is None    
    assert noise.laplace_noise(None, 1) is None    
    assert noise.poisson_noise(None, 1) is None    
    assert noise.uniform_noise(None, 1) is None
    assert noise.exponential_noise(None, 1) is None

