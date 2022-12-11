from enum import Enum

class Settings(Enum):
    '''
    Settings global variables of the application.
    '''
    WIDTH = 1280
    HEIGHT = 720
    TOOLBAR_HEIGHT = 24
    APP_COLOR = 'DarkTurquoise'
    SNAPSHOT = 'alpha v0.1'


class Resources(Enum):
    '''
    Resources global paths of the application.
    '''
    ICONS = 'resources\\static\\'
    IMAGES = 'resources\\img\\'


class ImpOps(Enum):
    '''
    ImpOps global variables of the application.
    '''
    PIXEL = {
        'pixel': [0, lambda: print('siuuuuuuuu'), 0]
    }
    
    CONVOLUTION = {
        'convolution': [1, 1, 1]
    }

    HISTOGRAM = {
        'histogram': [2, 2, 2]
    }

    NOISE = {
        'noise': [3, 3, 3]
    }

    CUBE = {
        'cube': [4, 4, 4]
    }

    GRAPH = {
        'graph': [5, 5, 5]
    }

    LOG = {
        'log-file': [6, 6, 6]
    }

    NUCLEUS_1 = {
        'nucleus': [7, 7, 7]
    }

    NUCLEUS_2 = {
        'nucleus': [8, 8, 8]
    }
