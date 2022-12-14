from enum import Enum


class Settings(Enum):
    '''
    Settings global variables of the application.
    '''
    WIDTH = 1280
    HEIGHT = 720
    TOOLBAR_HEIGHT = 24
    APP_COLOR = 'DarkTurquoise'
    SNAPSHOT = 'alpha v0.0.4'


class Resources(Enum):
    '''
    Resources global paths of the application.
    '''
    ICONS = 'resources\\static\\'
    IMAGES = 'resources\\img\\'


class Templates(Enum):
    '''
    It's a certain configuration of a visualizer.
    It contians the default settings (position, size, etc.) of all the Images in the visualizer.
    Every template can have a different amount of images.
    '''
    ALONE = ('1x1', 1280, 720)

    TOGETHER = ('2x1', 1280, 720)

    SIDE_BY_SIDE = ('1x2', 1280, 720)

    QUAD = ('2x2', 1280, 720)

    T_POS = ('3x1', 1280, 720)


