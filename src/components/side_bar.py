from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from dataclasses import dataclass


@dataclass
class SideBar(QWidget):
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    def __init__(self):
        super().__init__()

