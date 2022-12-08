from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QImage, QPen, QBrush, QPainter
from PyQt6.QtCore import Qt
import sys


class UI(QWidget):
    '''
    User Interface class referece to the window that contains all the widgets.
    These includes the SideBar ^ the WorkSpace
    '''
    def __init__(self):
        super().__init__()


    def paintEvent(self, event):
        '''Main paint event function that draws the elements inside the window.'''
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
        painter.drawImage(0, 0, QImage('resources\\img\\lena.jpg'))
        painter.drawRect(100, 15, 300,100)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    ui = UI()
    # print(ui.paintEvent.__doc__)  # Print the docstring of the paintEvent function
    ui.show()
    sys.exit(app.exec())  # Start the event loop
