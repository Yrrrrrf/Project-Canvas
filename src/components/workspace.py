from ..components.visualizer import Visualizer
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from dataclasses import dataclass
# import typing


@dataclass
class Workspace(QWidget):
    '''
    Workspace class reference to the workspace of the application.
    '''
    visualizer: list[Visualizer]


    def __init__(self):
        super().__init__()


