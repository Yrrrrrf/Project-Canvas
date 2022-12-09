from ..components.display import Display
from src.globals import Settings
from PyQt6.QtWidgets import QMainWindow


def set_menu_bar(app_window: QMainWindow):
    '''
    Set the menu bar of the main window.
    It can also access the SideBar, WorkSpace, and the DataBar.
    '''
    # Set the menu bar style sheet (dark theme)
    app_window.menuBar().setStyleSheet(f"background-color: #2d2d2d; color: white; min-height: {Settings.TOOLBAR_HEIGHT.value}px;")
    # Add the menus
    # File Menu
    app_window.menuBar().addMenu('Edit')
    app_window.menuBar().addMenu('View')
    app_window.menuBar().addMenu('File')
    app_window.menuBar().addMenu('Tools')
