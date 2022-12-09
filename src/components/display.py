from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QImage, QPen, QBrush, QPainter
from PyQt6.QtCore import Qt
import sys
from dataclasses import dataclass
from src.components.side_bar import SideBar
from src.components.workspace import Workspace


@dataclass
class Display(QWidget):
    '''
    Display class referece to the window that contains all the widgets.
    '''
    sidebar: SideBar
    workspace: Workspace


    def __init__(self):
        super().__init__()


    def paintEvent(self, event):
        '''Main paint event function that draws the elements inside the window.'''
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 1, Qt.PenStyle.SolidLine))
        # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
        painter.drawImage(0, 0, QImage('resources\\img\\lena.jpg'))
        painter.drawRect(0, 0, 1280, 720)
        painter.drawRect(16, 16, 1280, 720)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    ui = Display()
    # print(ui.paintEvent.__doc__)  # Print the docstring of the paintEvent function
    ui.show()
    sys.exit(app.exec())  # Start the event loop
