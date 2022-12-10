from src.components.side_bar_button import SideBarButton
from src.globals import Settings
from PyQt6.QtWidgets import QWidget, QFrame
from dataclasses import dataclass


@dataclass
class SideBar(QFrame):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    buttons: list[SideBarButton]  # list of buttons
    margin: int = 8  # margin between the buttons


    def __init__(self, display: QWidget):
        super().__init__(display)
        # todo: add the custom-buttons to the sidebar
        # todo: asociate the buttons with the actions
        self.setStyleSheet('background-color: #2d2d2d; border-radius: 8%;')
        operations_frame = QFrame(self)
        operations_frame.setStyleSheet('background-color: #dbdbdb; border-radius: 6%; border:2px solid '+f'{Settings.APP_COLOR.value}'+';}')


        self.buttons = [
            SideBarButton('resources\\static\\grid.png', parent=self),
            SideBarButton('resources\\static\\neural-network.png', parent=self),
            SideBarButton('resources\\static\\histogram.png', parent=self),
            SideBarButton('resources\\static\\cube.png', parent=self),
            SideBarButton('resources\\static\\connection.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\log-file.png', parent=self)
        ]
        #  Add the buttons to the layout
        for i in range(len(self.buttons)):
            self.buttons[i].setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*i), SideBarButton.button_size, SideBarButton.button_size)
        # Add the operations
        operations_frame.setGeometry(self.margin*2+SideBarButton.button_size, 0, self.margin*2, self.margin+self.buttons[-1].y()+SideBarButton.button_size)
