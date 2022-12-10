from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage
from dataclasses import dataclass


@dataclass
class Visualizer(QWidget):
    '''
    Visuualizer class manage the image(s) that are inside the workspace itself
    '''
    image_history: list[QImage]  # last 10 images
    image: QImage  # current image


    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #a19ea8')

