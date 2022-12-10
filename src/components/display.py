from src.components.workspace import Workspace
from src.components.side_bar import SideBar
from PyQt6.QtWidgets import QApplication, QWidget, QApplication, QHBoxLayout
from PyQt6.QtCore import QRect
import sys
from dataclasses import dataclass
import time




@dataclass
class Display(QWidget):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    '''
    sidebar: SideBar
    workspace: Workspace


    def __init__(self):
        super().__init__()
        # The layout had the same name as the class because is the main layout of the application. So all the widgets will be added to this layout, and the'll be resized automatically.
        display = QHBoxLayout()
        self.setLayout(display)
        self.workspace = Workspace(self)
        self.sidebar = SideBar(self)
        self.sidebar.setMaximumWidth(72)
        # self.sidebar.setMaximumWidth(128)
        display.addWidget(self.sidebar)
        display.addWidget(self.workspace)



if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    ui = Display()
    # ui.show()
    sys.exit(app.exec())  # Start the event loop
