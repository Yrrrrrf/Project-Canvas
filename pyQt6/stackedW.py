from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton
from PyQt6.QtGui import QIcon
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main Window
    window = QMainWindow()  # Create a window
    window.setWindowTitle('QStsckedWidget')  # Set the window title
    window.setBaseSize(1280, 720)  # Set the base size of the window. This is the size of the window when it is first shown.
    # window.setGeometry(100, 100, 1280, 720)  # Set the window geometry
    window.setMinimumSize(1280, 720)  # Set the minimum size of the window
    window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon

    stack = QStackedWidget(window)  # Create a QStackedWidget

    # Add widgets to the QStackedWidget
    b1=QPushButton('Page 1')
    b2=QPushButton('Page 2')
    b1.clicked.connect(lambda: stack.setCurrentIndex(1))
    b2.clicked.connect(lambda: stack.setCurrentIndex(0))

    stack.addWidget(b1)
    stack.addWidget(b2)
    # Set the position of the QStackedWidget
    stack.setGeometry(0, 0, 1280, 720)

    # Display the window
    window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop
