from src.components.side_bar_button import SideBarButton
from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QStackedWidget, QHBoxLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QPen, QImage
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
        # side_bar = QHBoxLayout()
        operations_layout = QFrame(self)


        # side_bar.addWidget(operations_layout)
        operations_layout.setStyleSheet('background-color: white; border-radius: 7%;')
        operations_layout.setGeometry(self.margin*2+SideBarButton.button_size, 0, self.margin*2, 1000)


        self.buttons = [
            SideBarButton('resources\\static\\grid.png', parent=self),
            SideBarButton('resources\\static\\neural-network.png', parent=self),
            SideBarButton('resources\\static\\histogram.png', parent=self),
            SideBarButton('resources\\static\\cube.png', parent=self),
            SideBarButton('resources\\static\\connection.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\log-file.png', parent=self),
            SideBarButton('', parent=self)
        ]
        for i in range(len(self.buttons)):
            self.buttons[i].setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*i), SideBarButton.button_size, SideBarButton.button_size)
