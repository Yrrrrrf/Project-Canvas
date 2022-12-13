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

