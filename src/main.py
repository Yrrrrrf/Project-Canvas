from app_contents.app import Window
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys


settings = {
    'snapshot':'alpha v0.1',
    'width': 1280,
    'height': 720
}


class MainWindow(QMainWindow):
    '''
    Main Window class reference to the main window of the application.
    '''
    def __init__(self, settings: dict):
        # Create the instance of the MainWindow
        super().__init__()
        # Set the Main Window properties
        self.setWindowTitle('Project Canvas')  # Set the window title
        self.setWindowIcon(QIcon('resources\\static\\brush.png'))  # Set the window icon
        self.setMinimumSize(settings['width'], settings['height']+30)  # Set the minimum size of the window
        # Add 24+6 to the height to compensate for the menu bar
        # self.statusBar().showMessage(f'Project Canvas {snapshot}')  # Set the status bar message
        # self.setStyleSheet('background-color: #2d2d2d;')  # Set the window style sheet

        # Set menu bar
        self.set_menu_bar()

        # Set the central widget
        self.app = Window()
        self.setCentralWidget(self.app)  # Set the central widget of the window

        # Show the window
        self.show()


    def set_menu_bar(self):
        '''
        Set the menu bar of the main window.
        It can also access the SideBar, WorkSpace, and the DataBar.
        '''
        # Set the menu bar style sheet (dark theme)
        self.menuBar().setStyleSheet('background-color: #2d2d2d; color: white; min-height: 24px;')
        # Add the menus
        # File Menu
        self.menuBar().addMenu('File')


        self.menuBar().addMenu('Edit')
        self.menuBar().addMenu('View')
        self.menuBar().addMenu('Tools')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    window = MainWindow(settings=settings)
    # window.show()
    sys.exit(app.exec())  # Start the event loop
