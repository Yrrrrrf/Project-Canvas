from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main Window
    window = QMainWindow()  # Create a window
    window.setWindowTitle('Project Canvas')  # Set the window title
    window.setBaseSize(1280, 720)  # Set the base size of the window. This is the size of the window when it is first shown.
    # window.setGeometry(100, 100, 1280, 720)  # Set the window geometry
    window.setMinimumSize(1280, 720)  # Set the minimum size of the window
    window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon

    window.setWindowOpacity(0.9)  # Set the window opacity
    window.setStyleSheet('background-color: #2d2d2d;')  # Set the window style sheet

    # Status Bar
    window.statusBar().showMessage('Project Canvas (alpha v0.1)')  # Set the status bar message
    
    
    # Menu Bar
    window.menuBar().addMenu('File')
    window.menuBar().addMenu('Edit')
    window.menuBar().addMenu('View')
    window.menuBar().addMenu('Tools')


    window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

