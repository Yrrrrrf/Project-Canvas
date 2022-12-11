from enum import Enum


class Operations(Enum):
    '''
    ImpOps global variables of the application.
    '''
    PIXEL = {'pixel': [0, lambda: ('siuuuuuuuu'),
         0]
    }

    CONVOLUTION = {'convolution': [1, 1, 1]
    }

    HISTOGRAM = {'histogram': [2, 2, 2]
    }

    NOISE = {'noise': [3, 3, 3]
    }

    CUBE = {'cube': [4, 4, 4]
    }

    GRAPH = {'graph': [5, 5, 5]
    }

    LOG = {'log-file': [6, 6, 6]
    }

    NUCLEUS_1 = {'nucleus': [7, 7, 7]
    }

    NUCLEUS_2 = {'nucleus': [8, 
        (lambda: print('f1')), 
        (lambda: print('f2')),
        (lambda: print('f3')),
        (lambda: print('f4')),
        (lambda: print('f5'))
    ]}
