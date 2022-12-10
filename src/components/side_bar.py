from src.components.side_bar_button import SideBarButton
from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QStackedWidget, QHBoxLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QPen, QImage
from dataclasses import dataclass


@dataclass
class SideBar(QWidget):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    buttons: list[SideBarButton]  # list of buttons

    def __init__(self, display: QWidget):
        super().__init__(display)
        # todo: add the custom-buttons to the sidebar
        # todo: asociate the buttons with the actions
        side_bar = QHBoxLayout()
        buttons_layout = QFrame(self)

        side_bar.addWidget(buttons_layout)

        buttons_layout.setStyleSheet('background-color: #2d2d2d; border-radius: 8%;')
        buttons_layout.setGeometry(QRect(0, 0, 80, display.geometry().height()))
        # buttons_layout.setGeometry(QRect(0, 0, 80, display.geometry().height()))

        # functions_layout = QStackedWidget(self)
        # # functions_layout.addWidget(QPushButton('resources\\img\\icons\\open.png'))


        self.buttons = [
            SideBarButton('resources\\static\\grid.png', parent=self),
            SideBarButton('resources\\static\\neural-network.png', parent=self),
            SideBarButton('resources\\static\\histogram.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('resources\\static\\nucleus.png', parent=self),
            SideBarButton('', parent=self)
        ]
        # for button in self.buttons:
        #     buttons_layout.addWidget(button)

        for i in range(len(self.buttons)):
            self.buttons[i].setGeometry(8, 8+(48*i), 64, 64)
