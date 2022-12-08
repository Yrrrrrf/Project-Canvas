from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


def paintEvent(self, event):
    painter = QPainter(self)
    painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.SolidLine))
    painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
    painter.drawRect(100, 15, 300,100)



if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main window
    main_window = QMainWindow()  # Create a main window
    main_window.setMinimumSize(480, 240)  # Set the minimum size of the window
    main_window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon
    main_window.setWindowTitle('QPainter')  # Set the window title

    # Is impossible to modify the layout of a QMainWindow, so we need to create a QWidget and set it as the central widget of the QMainWindow.
    window = QWidget()  # Create a window
    main_window.setCentralWidget(window)  # Set the central widget of the window

    # QImage
    # This class is used to store and manipulate images.
    # The QImage class can be used to load and save images in a variety of formats.
    image = QImage('pyQt6/doc/qt_logo.png')
    print(image.size())  # Print the image size
    print(image.format())  # Print the image format
    print(image.depth())  # Print the image depth



    main_window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

