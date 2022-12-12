from src.globals import Settings
from PyQt6.QtWidgets import QWidget, QFrame, QLabel
from PyQt6.QtGui import QPen, QPainter, QFont
from PyQt6.QtCore import Qt
from dataclasses import dataclass


@dataclass
class OperationsMenu(QFrame):
    '''
    Operations menu contains the operations that can be applied to the image.
    These operations are displayed as buttons.
    '''
    side_bar: QWidget  # ? Parent Widget
    title: QLabel
    deployed: bool = False  # ? Whether the operations menu is deployed or not
    showing_size = 240  # ? The width of the operations menu when it is deployed


    def __init__(self, side_bar: QWidget):
        '''
        Initialize the operations menu.
        '''
        super().__init__(side_bar)
        self.setStyleSheet('QFrame {background-color: #dbdbdb; border-radius: 6%; border: 2px solid '+f'{Settings.APP_COLOR.value}'+';}')
        self.title = QLabel(self)
        self.set_title('Testing...')


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
        from src.components.side_bar import SideBar
        self.title.setText(title)
        self.title.setStyleSheet('QLabel {color: white;}')
        self.title.setFont(QFont('Segoe Print', 16, QFont.Weight.Bold))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setGeometry(SideBar.margin*3, 12, self.showing_size-SideBar.margin*6, 32)


    def deploy(self) -> None:
        '''
        Deploy the operations menu.
        Also update's the operations that are displayed.
        '''
        self.deployed = True
        self.setFixedWidth(self.showing_size)


    def hide(self) -> None:
        '''
        Hide the operations menu.
        '''
        from src.components.side_bar import SideBar
        self.deployed = False
        self.setFixedWidth(SideBar.margin*2)

