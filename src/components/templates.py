from src.img_operations.load_image import load_cat
from src.components.visualizer import Visualizer
from src.components.image_buffer import ImageBuffer
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QImage, QPen, QPainter, QCursor, QKeySequence, QShortcut
from dataclasses import dataclass


@dataclass
class Template(Visualizer):
    '''
    This class contains one or more image buffer's, which are the images that are displayed in the workspace.
    The visualizer is the container of the image buffer's. 
    '''
    margin: int = 16
    scale: float = 1.0


    def __init__(self, workspace: QFrame, scale: float = 1.0, margin: int = 16):
        super().__init__(workspace)
        self.setStyleSheet('background-color: white')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        print(self.width(), self.height())
        self.setFixedSize((int)(self.width()*scale), (int)(self.height()*scale))


        self.t_template()


    def paintEvent(self, event):
        '''
        Main paint event function that draws the elements inside the window.
        '''
        painter = QPainter(self)

        # DRAW A FRAME AROUND THE IMAGE BUFFER
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 5, Qt.PenStyle.SolidLine))
        # draw a diagonal line
        painter.drawLine(0, 0, self.width(), self.height())


    def t_template(self):
        '''
        This function is used to test the template class.
        '''
        # set test layout

        self.imgs = []
        self.imgs.append(ImageBuffer())
        self.imgs[0].setParent(self)
        self.imgs[0].setGeometry(0, 0, 400, 100)
        self.imgs.append(ImageBuffer())
        self.imgs[1].setParent(self)
        self.imgs[1].setGeometry(100, 100,100, 100)
        self.imgs.append(ImageBuffer())
        self.imgs[2].setParent(self)
        self.imgs[2].setGeometry(300, 300, 100, 100)
        # add image buffers

        
        
        


