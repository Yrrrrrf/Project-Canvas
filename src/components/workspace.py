from src.components.visualizer import Visualizer
from src.img_operations.load_image import load_cat
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor, QKeySequence, QShortcut, QPalette
from dataclasses import dataclass


@dataclass
class Workspace(QScrollArea):
    '''
    Workspace class reference to the workspace of the application.
    Manage the visualizer that are inside the workspace.
    '''
    visualizer: list[Visualizer]


    def __init__(self, display: QWidget, visualizer: list[Visualizer] = []):
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
        self.visualizer = []
        self.visualizer.append(Visualizer(frame, scale=1.0, template='square'))
        self.visualizer[0].move(64, 64)
        frame.setFixedSize(self.visualizer[0].width()+128, self.visualizer[0].height()+128)
        self.setWidget(frame)

        self.shortcut = QShortcut(QKeySequence("Ctrl+L"), self)

