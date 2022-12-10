from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
from dataclasses import dataclass


@dataclass
class SideBarButton(QPushButton):
    '''
    SideBarButton class contains the icon, options and the action of the button.
    '''
    options: list[str]

    # todo: add hover effect to the buttons
    def __init__(self, icon: str, parent):
        super().__init__()
        self.setParent(parent)
        self.setStyleSheet('border-radius: 10%; border: 4px; background: white')
        # self.options = options
        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(32, 32))
        self.setMaximumSize(40, 40)
        self.clicked.connect(lambda: print('clicked'))
