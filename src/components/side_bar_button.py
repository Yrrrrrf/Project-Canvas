from PyQt6.QtWidgets import QPushButton, QFrame
from src.globals import Settings, Resources
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class SideBarButton(QPushButton):
    '''
    SideBarButton class contains the icon, options and the action of the button.
    '''
    operations: list  # image operations that the button will perform
    name: str
    icon: str
    button_size: int = 40
    icon_size: int = 32


    def __init__(self, icon: str, side_bar: QFrame, operations_frame: QFrame):
        super().__init__()
        self.name = icon.split('.')[0]  # Assign the name of the button
        self.setParent(side_bar)
        button_style = 'QPushButton {border-radius: 10%; background: white;}'
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        self.setIcon(QIcon(Resources.ICONS.value+icon))
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(self.button_size, self.button_size)  # default size
        self.operations = []


@dataclass
class OperationButton(QPushButton):
    '''
    OperatoinButton class contains executes an operation to an image.
    '''
    name: str
    icon: str
    button_size: int = 32
    icon_size: int = 24


    def __init__(self, icon: str, operations_frame: QFrame):
        super().__init__()
        self.name = icon.split('.')[0]  # Assign the name of the button
        self.setParent(operations_frame)
        button_style = 'QPushButton {border-radius: 10%; background: white;}'
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        self.setIcon(QIcon(Resources.ICONS.value+icon))
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(self.parent.width(), self.button_size)  # default size
        self.operations = []

