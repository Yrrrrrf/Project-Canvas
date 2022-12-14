from src.components.visualizer import Visualizer
from src.components.templates import Template
from src.img_operations.load_image import load_cat
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor, QKeySequence, QShortcut, QPalette
from dataclasses import dataclass


@dataclass
class Workspace(QScrollArea):
    '''
    Workspace class reference to the workspace of the application.
    Manage the visualizer that are inside the workspace.
    '''
    visualizer: list[Visualizer]


    def __init__(self, display: QWidget):
        '''
        Initialize the Workspace class.
        Needs the display widget as a parameter, which is the main window of the application.
        '''
        super().__init__(display)
        # set scroll content
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setBackgroundRole(QPalette.ColorRole.Dark)

        # set test layout
        frame = QFrame(self)
        frame.setStyleSheet('background-color: #4A4A4A; border-color: blue;')
        template = Template(frame, 2.0, 64) 
        template.move(64, 64)

        frame.setFixedSize(template.width()+128, template.height()+128)
        self.setWidget(frame)

        self.shortcut = QShortcut(QKeySequence("Ctrl+L"), self)

