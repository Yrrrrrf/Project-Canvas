from src.components.side_bar_button import SideBarButton
from src.components.operations_menu import OperationsMenu
from src.components.operation_button import OperationButton
from src.globals import Settings
from src.operations import Operations
from PyQt6.QtWidgets import QWidget, QFrame
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QPen, QPainter, QImage, QCursor
from dataclasses import dataclass


@dataclass
class SideBar(QWidget):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    buttons_frame: QFrame
    buttons: list[SideBarButton]
    operations_menu: OperationsMenu  # contains the operation buttons
    margin: int = 8  # margin between the buttons


    def __init__(self, display: QWidget):
        super().__init__(display)
        self.setFixedWidth(self.margin*4+SideBarButton.button_size)  # set the initial size of the side bar

        self.buttons_frame = QFrame(self)
        self.buttons_frame.setStyleSheet('QFrame{background-color: #2d2d2d; border-radius: 8%;}')
        self.buttons_frame.setFixedWidth(self.margin*2+SideBarButton.button_size)

        self.operations_menu = OperationsMenu(self)
        self.load_buttons()
        # ? set the operations_menu on the right side of the buttons_frame
        self.operations_menu.setGeometry(self.margin*2+SideBarButton.button_size, 0, self.margin*2, self.margin+self.buttons[-1].y()+SideBarButton.button_size)


    def load_buttons(self) -> None:
        '''
        Load the buttons of the side bar.
        '''
        self.buttons = []
        i = 0
        for operation in Operations:
            op_button = SideBarButton(operation.name, operation.value, self.buttons_frame)
            op_button.setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*i), SideBarButton.button_size, SideBarButton.button_size)
            self.buttons.append(op_button)
            i+=1


    def toggle(self) -> None:
        '''
        Toggle the Operations Menu. (show/hide)
        '''
        if self.operations_menu.deployed == True:  # if the operations menu is deployed
            self.operations_menu.hide()  # hide the operations menu
            self.setFixedWidth(self.margin*4+SideBarButton.button_size)
        else:  # if the operations menu is hidden
            self.operations_menu.deploy()  # show the operations menu
            self.setFixedWidth(self.margin*2+SideBarButton.button_size+self.operations_menu.width())

            self.update_operations_menu()  # update the operations menu


    def update_operations_menu(self) -> None:
        '''
        Show the operations menu.
        Update the title & buttons of the operations menu.
        The operations buttons are loaded from the operations_menu class.
        '''
        # print(self.operations_menu.title.text())
        operations = Operations.PIXEL.value
        # create the operations buttons and add them to the operations menu
        pass


    def center_side_bar(self) -> None:
        '''
        Center the side bar. (vertical)
        '''        
        self.setFixedHeight(self.margin+self.buttons[-1].y()+SideBarButton.button_size)

