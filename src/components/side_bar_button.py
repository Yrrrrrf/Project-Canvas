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
    data: list[dict]
    button_size: int = 40
    icon_size: int = 32


    def __init__(self, name: str, operations: list[dict], side_bar: QFrame):
        super().__init__()
        self.name = name
        self.operations = operations
        # print(f'name: {self.name} {type(self.data)}')
        # print(self.data)
        self.setParent(side_bar)
        button_style = 'QPushButton {border-radius: 10%; background: white;}'
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        # If there's only one file with that posible name*, then the path will be autocompleted to the file.
        self.setIcon(QIcon(Resources.ICONS.value+self.name+'.png'))  # Just to be sure that is the format of the icon
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(self.button_size, self.button_size)  # default size

        
        # *If there's more than one file with the same name, then the path will be autocompleted to the folder.
        self.clicked.connect(lambda: self.toggle_side_bar(self.name))




    def toggle_side_bar(self, name: str):
        from src.components.side_bar import SideBar  # this import is there to avoid circular imports
        
        print(f'{name} menu Opened')