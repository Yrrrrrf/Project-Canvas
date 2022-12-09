from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QImage, QPen, QBrush, QPainter
from PyQt6.QtCore import Qt
# from PyQt6 import QtCore
import sys
from ..globals import Settings 


class Window(QWidget):
    '''
    User Interface class referece to the window that contains all the widgets.
    These includes the SideBar ^ the WorkSpace
    '''
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove the window frame


    def paintEvent(self, event):
        '''Main paint event function that draws the elements inside the window.'''
        painter = QPainter(self)
        # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
        painter.setPen(QPen(Qt.GlobalColor.darkCyan, 1, Qt.PenStyle.SolidLine))
        painter.drawImage(0, 0, QImage('resources\\img\\lena.jpg'))
        painter.drawRect(0, 0, Settings.HEIGHT.value//2, Settings.WIDTH.value//2)
        painter.drawRect(16, 16, Settings.HEIGHT.value//2, Settings.WIDTH.value//2)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    ui = Window()
    # print(ui.paintEvent.__doc__)  # Print the docstring of the paintEvent function
    ui.show()
    sys.exit(app.exec())  # Start the event loop
