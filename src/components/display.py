from src.components.workspace import Workspace
from src.components.side_bar import SideBar
from src.components.side_bar_button import SideBarButton
from PyQt6.QtWidgets import QApplication, QWidget, QApplication, QHBoxLayout
from PyQt6.QtCore import QRect
import sys
from dataclasses import dataclass
import time

# temp


@dataclass
class Display(QWidget):
    '''
    Display class referece to the window that contains all the widgets.
    Also manage the position of the widgets and the size of the window.
    '''
    sidebar: SideBar
    # these variables are used to toggle the side bar
    hidden_side_bar_size = SideBar.margin*4+SideBarButton.button_size
    showing_side_bar_size = 256

    workspace: Workspace


    def __init__(self):
        super().__init__()
        # The layout had the same name as the class because is the main layout of the application. So all the widgets will be added to this layout, and the'll be resized automatically.
        display = QHBoxLayout()
        self.setLayout(display)
        self.workspace = Workspace(self)
        self.sidebar = SideBar(self)
        # self.sidebar.setFixedWidth(self.hidden_side_bar_size)
        self.sidebar.setFixedWidth(self.showing_side_bar_size)
        display.addWidget(self.sidebar)
        display.addWidget(self.workspace)


# def toggle_side_bar(sidebar: Display):
#     if sidebar.width() == self.hident_side_bar_size:
#         sidebar.setFixedWidth(showing_side_bar_size)
#     else:
#         sidebar.setFixedWidth(hident_side_bar_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    ui = Display()
    # ui.show()
    sys.exit(app.exec())  # Start the event loop
