from PyQt6.QtWidgets import QWidget, QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor, QFont
from src.globals import Settings
from dataclasses import dataclass
# import typing


@dataclass
class OperationsMenu(QFrame):
    '''
    Operations menu contains the operations that can be applied to the image.
    These operations are displayed as buttons.
    '''
    title: QLabel

    def __init__(self, side_bar: QWidget):
        '''
        '''
        super().__init__(side_bar)
        self.setStyleSheet('QFrame{background-color: #dbdbdb; border-radius: 6%; border: 2px solid '+f'{Settings.APP_COLOR.value}'+';}')
        self.set_title('Testing...')
        self.title.setStyleSheet('QLabel {color: #2d2d2d; font-size: 16px; font-weight: bold;}')


    def paintEvent(self, event):
        '''
        Main paint event function that draws the elements inside the window.
        '''
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 1, Qt.PenStyle.SolidLine))
        # painter.drawRect(16, 16, 1280, 720)


    def set_title(self, title: str) -> None:
        '''
        Set the title of the operations menu.
        Every time the title is changed, the title label is recentered.
        '''
        self.title = QLabel(self)
        self.title.setFont(QFont('Segoe Print', 10, QFont.Weight.Bold))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setText(title)
        # todo: recenter the title label
        self.title.setGeometry(16, 16, self.width(), 32)

        # self.title.setGeometry(16, 16, self.width(), 32)
        # center the title label


    def set_operations(self, operations: list[str]) -> None:
        '''
        Set the operations of the operations menu.
        '''
        pass
    
