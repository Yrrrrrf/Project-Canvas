from src.components.visualizer import Visualizer
from src.test.request_img import load_cat
from PyQt6.QtWidgets import QWidget, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor
from dataclasses import dataclass
# import typing


@dataclass
class Workspace(QFrame):
    '''
    Workspace class reference to the workspace of the application.
    Manage the visualizer that are inside the workspace.
    '''
    visualizer: list[Visualizer]


    def __init__(self, display: QWidget):
        '''
        Initialize the Workspace class.
        Needs the display widget as a parameter, which is the main window of the application.
        '''
        super().__init__(display)
        self.setStyleSheet('background-color: #a19ea8; border-color: red; border-width: 5px;')
        self.setCursor(QCursor(Qt.CursorShape.CrossCursor))

        self.stock_img = load_cat()  # return the memory address of the image
        # self.stock_img = 'resources\\img\\lena.png'


    def paintEvent(self, event):
        '''
        Main paint event function that draws the elements inside the window.
        '''
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 1, Qt.PenStyle.SolidLine))
        painter.drawImage(0, 0, QImage(self.stock_img))
        painter.drawRect(0, 0, 1280, 720)
        painter.drawRect(16, 16, 1280, 720)

