from PyQt6.QtWidgets import QWidget, QStackedWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor
from src.globals import Settings
from dataclasses import dataclass
# import typing


@dataclass
class OperationsMenu(QStackedWidget):
    '''
    '''
    title: QLabel

    def __init__(self, side_bar: QWidget):
        '''
        '''
        super().__init__(side_bar)
        self.setStyleSheet('QFrame{background-color: #dbdbdb; border-radius: 6%; border: 2px solid '+f'{Settings.APP_COLOR.value}'+';}')
        self.title = QLabel('testing...' , self)
        self.title.setGeometry(16, 16, 128, 32)
        self.title.setStyleSheet('QLabel {color: #2d2d2d; font-size: 16px; font-weight: bold;}')


    def paintEvent(self, event):
        '''
        Main paint event function that draws the elements inside the window.
        '''
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 1, Qt.PenStyle.SolidLine))
        painter.drawRect(16, 16, 1280, 720)

