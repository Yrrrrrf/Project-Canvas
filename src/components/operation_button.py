from src.globals import Settings, Resources
from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtGui import QIcon, QFont, QColor
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class OperationButton(QPushButton):
    '''
    OperatoinButton class contains executes an operation to an image.
    Every operation is a button. The button is a child of the operations frame.
    If the unit test associated to the operation is passed, the button will be enabled.
    '''
    operations_menu: QWidget  # ? Parent Widget
    operation: dict  # contains the name and the function of the operation
    icon: str
    button_height: int = 32
    icon_size: int = 24


    def __init__(self, operations_menu: QWidget, operation: dict):
        super().__init__(operations_menu)
        self.operation = list(operation.keys())[0]  # Assign the name of the button
        self.operations_menu = operations_menu
        button_style = 'QPushButton {border-radius: 10%; background: white; color: gray;} '
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        self.setFont(QFont('Segoe Print', 10, QFont.Weight.Bold))
        # self.setIcon(QIcon(Resources.ICONS.value+icon))
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(122, self.button_height)
        self.setText(self.operation)

        self.set_operation(operation[self.operation])


    def set_operation(self, operation: list[dict]) -> None:
        '''
        Set the operation of the button.
        '''

        print(self.operation)
        # self.setFixedSize(self.parent.width(), self.button_size * len(operations))  # default size

