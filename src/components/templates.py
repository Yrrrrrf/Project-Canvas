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
        self.setFixedSize((int)(self.width()*scale), (int)(self.height()*scale))
        
        # ! test one template 
        self.t_template()


    def paintEvent(self, event):
        '''
        Main paint event function that draws the elements inside the window.
        '''
        painter = QPainter(self)
        # DRAW A FRAME AROUND THE IMAGE BUFFER
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 5, Qt.PenStyle.SolidLine))
        # draw a diagonal line
        # painter.drawLine(0, 0, self.width(), self.height())


    def t_template(self):
        '''
        This function is used to test the template class.
        '''
        # set test layout
        self.imgs = []

        # T layout 
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, self.width()-self.margin*2, (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry(self.margin, (int)((self.height()/2)+self.margin/2), (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry((int)((self.width()/2)+self.margin/2), (int)((self.height()/2)+self.margin/2), (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))


        # inverted T layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry((int)((self.width()/2)+self.margin/2), self.margin, (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry(self.margin, (int)((self.height()/2)+self.margin/2), self.width()-self.margin*2, (int)((self.height()/2)-self.margin*1.5))


        # lateral t layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)((self.width()/2)-self.margin*1.5), (int)(self.height()-self.margin*2))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry((int)((self.width()/2)+self.margin/2), self.margin, (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry((int)((self.width()/2)+self.margin/2), (int)((self.height()/2)+self.margin/2), (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))

        
        # inverted lateral t layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry(self.margin, (int)((self.height()/2)+self.margin/2), (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry((int)((self.width()/2)+self.margin/2), self.margin, (int)((self.width()/2)-self.margin*1.5), (int)(self.height()-self.margin*2))


        # 3x1 layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)((self.width()/3)-self.margin*1.5), (int)(self.height()-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry((int)((self.width()/3)+self.margin/2), self.margin, (int)((self.width()/3)-self.margin*1.5), (int)(self.height()-self.margin*2))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry((int)((self.width()/3)*2+self.margin/2), self.margin, (int)((self.width()/3)-self.margin*1.5), (int)(self.height()-self.margin*2))


        # 1x3 layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)(self.width()-self.margin*2), (int)((self.height()/3)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry(self.margin, (int)((self.height()/3)+self.margin/2), (int)(self.width()-self.margin*2), (int)((self.height()/3)-self.margin))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry(self.margin, (int)((self.height()/3)*2+self.margin/2), (int)(self.width()-self.margin*2), (int)((self.height()/3)-self.margin*1.5))


        # 2x2 layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry((int)((self.width()/2)+self.margin/2), self.margin, (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry(self.margin, (int)((self.height()/2)+self.margin/2), (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[3].setParent(self)
        # self.imgs[3].setGeometry((int)((self.width()/2)+self.margin/2), (int)((self.height()/2)+self.margin/2), (int)((self.width()/2)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))


        # trident layout
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, self.margin, (int)((self.width()/3)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry((int)((self.width()/3)+self.margin/2), self.margin, (int)((self.width()/3)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry((int)((self.width()/3)*2+self.margin/2), self.margin, (int)((self.width()/3)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[3].setParent(self)
        # # make 3 ocupy the whole width
        # self.imgs[3].setGeometry(self.margin, (int)((self.height()/2)+self.margin/2), (int)(self.width()-self.margin*2), (int)((self.height()/2)-self.margin*1.5))


        # inverse trident layout (the same but the 3rd row is on top)
        # self.imgs.append(ImageBuffer())
        # self.imgs[0].setParent(self)
        # self.imgs[0].setGeometry(self.margin, (int)((self.height()/2)+self.margin/2), (int)((self.width()/3)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[1].setParent(self)
        # self.imgs[1].setGeometry((int)((self.width()/3)+self.margin/2), (int)((self.height()/2)+self.margin/2), (int)((self.width()/3)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[2].setParent(self)
        # self.imgs[2].setGeometry((int)((self.width()/3)*2+self.margin/2), (int)((self.height()/2)+self.margin/2), (int)((self.width()/3)-self.margin*1.5), (int)((self.height()/2)-self.margin*1.5))
        # self.imgs.append(ImageBuffer())
        # self.imgs[3].setParent(self)
        # # make 3 ocupy the whole width
        # self.imgs[3].setGeometry(self.margin, self.margin, (int)(self.width()-self.margin*2), (int)((self.height()/2)-self.margin*1.5))


        # 1 image layout
        self.imgs.append(ImageBuffer())
        self.imgs[0].setParent(self)
        self.imgs[0].setGeometry(self.margin, self.margin, (int)(self.width()-self.margin*2), (int)(self.height()-self.margin*2))

