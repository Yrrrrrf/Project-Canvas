from PyQt6.QtWidgets import QPushButton, QWidget
from src.globals import Settings, Resources
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class SideBarButton(QPushButton):
    '''
    SideBarButton class contains a list of operations that can be executed to an image.
    Every operation is a button will appear in the Operations Menu.
    '''
    side_bar: QWidget  # ? Parent Widget
    name: str  # ? name corresponds to the Operation type (Enum)
    operations: list[dict]  # ? list of operations
    button_size: int = 48
    icon_size: int = 40


    def __init__(self, name: str, operations: list[dict], side_bar: QWidget):
        super().__init__()
        from src.components.side_bar import SideBar  # this import is there to avoid circular imports
        self.name = name
        self.operations = operations
        self.setParent(side_bar)
        button_style = 'QPushButton {border-radius: 10%; background: white;}'
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        # If there's only one file with that posible name*, then the path will be autocompleted to the file.
        self.setIcon(QIcon(Resources.ICONS.value+self.name+'.png'))  # Just to be sure that is the format of the icon
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(self.button_size, self.button_size)  # default size

