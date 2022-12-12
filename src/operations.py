from enum import Enum
# from img_operations.pixel import *
# from img_operations.convolution import *
# from img_operations.histogram import *
# from img_operations.noise import *
  
# ? import img operations
from src.img_operations.pixel import *
from src.img_operations.convolution import *
from src.img_operations.histogram import *
from src.img_operations.noise import *


class Operations(Enum):
    '''
    ImpOps global variables of the application.
    '''
    PIXEL = [ 
        {'verital flip' : vertical_flip},
        {'horizontal flip' : horizontal_flip},
        {'invert colors' : invert},
        {'clear zone' : clear_zone},
        {'brightness' : change_brightness},
        {'contrast' : change_contrast},
        {'logarithmic transform' : logarithmic_transform},
        {'power transformation' : power_transformation},
        {'exponential transform' : exponential_transform},
        {'gamma correction' : gamma_correction},
        {'power law transform' : power_law_transform},
        {'piecewise linear transform' : piecewise_linear_transform}
    ]

    CONVOLUTION = [
        {'absurd filter' : absurd_filter},
        {'sharpen filter' : sharpen_filter},
        {'gaussian filter' : gaussian_filter},
        {'mean filter' : mean_filter},
        {'median filter' : median_filter},
        {'laplacian filter' : laplacian_filter},
        {'ordered range filter' : ordered_range_filter},
        {'bilateral filter' : bilateral_filter},
        {'sobel filter' : sobel_filter},
        {'emboss filter' : emboss_filter},
        {'edge filter' : edge_filter}
    ]

    HISTOGRAM = [
       {'equalize image' : equalize_img},
       {'equalize histogram rgb' : equalize_hist_rgb},
       {'resize image scale' : resize_img_scale},
       {'resize image' : resize_img}
    ]

    NOISE = [
        {'gaussian noise' : gaussian_noise},
        {'salt noise' : salt_noise},
        {'pepper noise' : pepper_noise},
        {'salt pepper noise' : salt_pepper_noise},
        {'speckle noise' : speckle_noise},
        {'rayleigh noise' : rayleigh_noise},
        {'laplace noise' : laplace_noise},
        {'poisson noise' : poisson_noise},
        {'uniform noise' : uniform_noise},
        {'exponential noise' : exponential_noise}
    ]

    CUBE = [
        {'cube_1': None},
        {'cube_2': None},
        {'cube_3': None},
        {'cube_4': None},
    ]

    GRAPH = [
        {'grapth_1': None},
        {'grapth_2': None},
        {'grapth_3': None},
        {'grapth_4': None},
    ]

    LOG = [
        {'log_1': None},
        {'log_2': None},
        {'log_3': None},
        {'log_4': None},
    ]

    NUCLEUS_1 = [
        {'nucleus_1': None},
        {'nucleus_2': None},
        {'nucleus_3': None},
        {'nucleus_4': None},
    ]

    NUCLEUS_2 = [
        {'nucleus2_1': None},
        {'nucleus2_2': None},
        {'nucleus2_3': None},
        {'nucleus2_4': None},
    ]


if __name__ == '__main__':
    for operation in Operations:
        print(f'\n{type(operation.name)}\n{operation.value}')

