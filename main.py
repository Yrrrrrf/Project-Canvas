from src.components.display import Display
from src.components.menu_bar import MenuBar
from src.globals import Settings
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys
from dataclasses import dataclass


@dataclass
class AppWindow(QMainWindow):
    '''
    Main Window class reference to the main window of the application.
    '''
    def __init__(self):
        # Create the instance of the MainWindow
        super().__init__()
        # Set the Main Window properties
        self.setWindowTitle('Project Canvas')  # Set the window title
        self.setWindowIcon(QIcon('resources\\static\\brush.png'))  # Set the window icon
        self.setMinimumSize(Settings.WIDTH.value, Settings.HEIGHT.value+6)  # Set the minimum size of the window
        # self.setMinimumSize(Settings.WIDTH.value, Settings.HEIGHT.value+Settings.TOOLBAR_HEIGHT.value+6)  # Set the minimum size of the window
        # Add 6 to the height to compensate for the menu bar
        # self.statusBar().showMessage(f'Project Canvas {snapshot}')  # Set the status bar message
        # self.setStyleSheet('background-color: #2d2d2d;')  # Set the window style sheet

        # Set menu bar
        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)

        # Set the central widget
        self.display = Display()
        self.setCentralWidget(self.display)  # Set the central widget of the window


        # Show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    window = AppWindow()
    sys.exit(app.exec())  # Start the event loop
