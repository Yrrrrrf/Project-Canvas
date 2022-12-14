from src.img_operations.load_image import load_cat
from src.components.image_buffer import ImageBuffer
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QImage, QPen, QPainter, QCursor
from dataclasses import dataclass


@dataclass
class Visualizer(QFrame):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    image: list[ImageBuffer]


    def __init__(self, workspace: QFrame, width: int = 512, height: int = 512):
        super().__init__(workspace)
        self.setStyleSheet('background-color: white')
        self.setGeometry(QRect(16, 16, width, height))
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))



        # img = QImage(load_cat())
        # self.imgs.append(ImageBuffer(img))
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry(QRect(700, 160, self.imgs[1].width(), self.imgs[1].height()))


    def paintEvent(self, event):
        '''
        Main paint event function that draws the elements inside the window.
        '''
        painter = QPainter(self)

        # DRAW A FRAME AROUND THE IMAGE BUFFER
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 5, Qt.PenStyle.SolidLine))
        # painter.drawRect(self.margin, self.margin, self.width()-self.margin*2, self.height()-self.margin*2)


    def set_image(self, image: QImage):
        '''
        Set the image of the image buffer.
        '''
        # self.image = image
        self.update()

