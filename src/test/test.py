from enum import Enum
import src.img_operations.convolution as convolution
import src.img_operations.histogram as histogram
import src.img_operations.noise as noise
import src.img_operations.pixel as pixel


def test_operations():
    '''
    Test the operations module.
    '''
    test_convolutions()
    test_histogram()
    test_noise()
    test_pixel()


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
    pass


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

