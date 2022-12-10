from PyQt6.QtWidgets import QPushButton, QWidget
from src.globals import Settings
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class SideBarButton(QPushButton):
    '''
    SideBarButton class contains the icon, options and the action of the button.
    '''
    options: list[str]
    button_size: int = 40
    icon_size: int = 32

    # todo: add hover effect to the buttons
    def __init__(self, icon: str, parent):
        super().__init__()
        self.setParent(parent)
        # self.setStyleSheet('border-radius: 10%; border: 4px; background: white')
        self.setStyleSheet(str('QPushButton {border-radius: 10%; background: white;} QPushButton:hover {background-color:'+f'{Settings.APP_COLOR.value}'+';}'))
        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        self.setFixedSize(self.button_size, self.button_size)  # default size
        self.clicked.connect(lambda: print('clicked'))
