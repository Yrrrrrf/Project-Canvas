from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from dataclasses import dataclass


@dataclass
class SidebarButton(QPushButton):
    '''
    SideBarButton class contains the icon, options and the action of the button.
    '''
    options: list[str]
