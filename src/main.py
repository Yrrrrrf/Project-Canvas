from app_contents.app import UI
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys


snapshot = 'alpha v0.1'




class Window(QMainWindow):
    def __init__(self):
        # Create the instance of the MainWindow
        super().__init__()
        # Set the Main Window properties
        self.setWindowTitle('Project Canvas')  # Set the window title
        self.setWindowIcon(QIcon('resources\\static\\brush.png'))  # Set the window icon
        self.setMinimumSize(1280, 720)  # Set the minimum size of the window
        self.statusBar().showMessage(f'Project Canvas {snapshot}')  # Set the status bar message
        # self.setStyleSheet('background-color: #2d2d2d;')  # Set the window style sheet
        # self.menuBar().addMenu('File')
        # self.menuBar().addMenu('Edit')
        # self.menuBar().addMenu('View')
        # self.menuBar().addMenu('Tools')

        self.app = UI()
        self.setCentralWidget(self.app)  # Set the central widget of the window

        self.show()  # Show the window


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    window = Window()
    sys.exit(app.exec())  # Start the event loop
