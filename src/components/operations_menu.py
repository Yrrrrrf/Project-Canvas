from src.globals import Settings
from src.components.operation_button import OperationButton
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QStackedWidget, QPushButton
from PyQt6.QtGui import QPen, QPainter, QFont
from PyQt6.QtCore import Qt
from dataclasses import dataclass


@dataclass
class OperationsMenu(QStackedWidget):
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
        self.hide()  # ? Hide the operations menu by default


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

