from src.components.side_bar_button import SideBarButton
from src.components.workspace import Workspace
from src.components.side_bar import SideBar
from PyQt6.QtWidgets import QWidget, QHBoxLayout
from dataclasses import dataclass


@dataclass
class Display(QWidget):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    This class must the the main class of the application.
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
        # Set the initial side bar size (hidden)
        # self.sidebar.setFixedWidth(SideBar.margin*4+SideBarButton.button_size)
        display.addWidget(self.sidebar)
        display.addWidget(self.workspace)

