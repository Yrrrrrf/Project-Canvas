from src.globals import Settings, Resources
from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class OperationButton(QPushButton):
    '''
    OperatoinButton class contains executes an operation to an image.
    Every operation is a button. The button is a child of the operations frame.
    If the unit test associated to the operation is passed, the button will be enabled.
    '''
    operation: str
    icon: str
    button_size: int = 32
    icon_size: int = 24




    def __init__(self, operation: dict, operations_menu: QWidget):
        super().__init__()
        # self.operation = list(operations.keys())[0]  # Assign the name of the button
        self.setParent(operations_menu)
        button_style = 'QPushButton {border-radius: 10%; background: white;}'
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        # self.setIcon(QIcon(Resources.ICONS.value+icon))
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(self.parent.width(), self.button_size)  # default size
        self.operations = []






