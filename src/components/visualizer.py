from src.img_operations.load_image import load_cat
from src.templates import templates
from src.components.image_buffer import ImageBuffer
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import QImage, QPen, QPainter, QCursor
from dataclasses import dataclass


@dataclass
class Visualizer(QLabel):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    workspace: QFrame  # ! is this needed?
    images: list[ImageBuffer]  # list of image buffers
    margin: int = 16
    scale: float = 1.0
    template: str = 'square'
    selected: bool = False


    def __init__(self, workspace: QFrame, width: int = 512, height: int = 512, scale: float = 1.0, margin: int = 16, template: str = 'square'):
        super().__init__(workspace)
        self.setStyleSheet('background-color: white')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.scale = scale
        self.margin = margin
        self.template = template
        self.setMinimumSize(QSize((int)(width*scale), (int)(height*scale)))

        self.images = []
        # template = list(templates.keys())[self.template]  # get the n template (name: str)
        for coors in templates[template](self.width(), self.height(), self.margin):
            self.images.append(ImageBuffer(coors[2], coors[3], self))
            self.images[-1].move(coors[0], coors[1])
        # self.set_template()


    def set_template(self):
        '''
        Set the template of the visualizer.
        The template is the layout of the image buffer's.
        '''
        # self.images = []
        # # template = list(templates.keys())[]  # get the n template (name: str)
        # for coors in templates[template](self.width(), self.height(), self.margin):
        #     self.images.append(ImageBuffer(coors[2], coors[3], self))
        #     self.images[-1].move(coors[0], coors[1])

