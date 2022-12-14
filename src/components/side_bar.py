from src.globals import Settings
from src.operations import Operations
from src.components.side_bar_button import SideBarButton
from src.components.operations_menu import OperationsMenu
from src.components.operations_page import OperationsPage
from src.components.operation_button import OperationButton
from PyQt6.QtWidgets import QWidget, QFrame
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
        # ? set the buttons_frame on the left side of the side bar
        self.buttons_frame = QFrame(self)
        self.buttons_frame.setStyleSheet('QFrame{background-color: #2d2d2d; border-radius: 8%;}')
        self.buttons_frame.setFixedWidth(self.margin*2+SideBarButton.button_size)
        # ? load the buttons
        self.load_side_bar_buttons()

        # self.center_side_bar()
        # example
        # OperationButton(self.operations_menu, {'a': lambda: print('a')}).setGeometry(32, 88, 2000, 32)


    def load_side_bar_buttons(self) -> None:
        '''
        Load the buttons of the side bar.
        Every buttons is associated to a Operations Menu, that contains many operations.
        '''
        self.operations_menu = OperationsMenu(self)  # Is a stack widget that contains the operations
        self.buttons = []

        i = 0
        for operation in Operations:
            op_button = SideBarButton(operation.name, operation.value, self.buttons_frame)
            op_button.setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*i), SideBarButton.button_size, SideBarButton.button_size)
            self.buttons.append(op_button)
            self.operations_menu.addWidget(OperationsPage(self.operations_menu, op_button.name, operation.value))
            i+=1


        # ? Connect the buttons to the toggle function
        self.buttons[0].clicked.connect(lambda: self.toggle(0))
        self.buttons[1].clicked.connect(lambda: self.toggle(1))
        self.buttons[2].clicked.connect(lambda: self.toggle(2))
        self.buttons[3].clicked.connect(lambda: self.toggle(3)) 
        # self.buttons[4].clicked.connect(lambda: self.toggle(4))
        # self.buttons[5].clicked.connect(lambda: self.toggle(5))
        # self.buttons[6].clicked.connect(lambda: self.toggle(6))
        # self.buttons[7].clicked.connect(lambda: self.toggle(7))
        # self.buttons[8].clicked.connect(lambda: self.toggle(8))
        # self.buttons[9].clicked.connect(lambda: self.toggle(9))
        # ! why this doesn't work?!?!?!
        # for i in range(len(self.buttons)):
        #     self.buttons[i].clicked.connect(lambda: self.toggle(i))

        # ? set the operations_menu on the right side of the buttons_frame
        self.operations_menu.setGeometry(self.margin*2+SideBarButton.button_size, 0, self.margin*2, self.margin+self.buttons[-1].y()+SideBarButton.button_size)


    def toggle(self, page_index: int) -> None:
        '''
        Toggle the Operations Menu. (show/hide)
        Update the title & buttons of the operations menu.
        '''
        if self.operations_menu.deployed == True:  # if the operations menu is deployed
            if self.operations_menu.currentIndex() == page_index:
                self.operations_menu.hide()  # hide the operations menu
                self.setFixedWidth(self.margin*4+SideBarButton.button_size)
            else:  # if the operations menu is deployed, but the user clicked on a different button
                self.operations_menu.setCurrentIndex(page_index)
                self.operations_menu.setFixedHeight(len(self.buttons[page_index].operations)*(SideBarButton.button_size+self.margin))
        else:  # if the operations menu is hidden
            self.operations_menu.setCurrentIndex(page_index)
            self.operations_menu.deploy()  # show the operations menu
            self.operations_menu.setFixedHeight(len(self.buttons[page_index].operations)*(SideBarButton.button_size+self.margin))
            # update the width of the side bar (to fit the operations menu)
            self.setFixedWidth(self.margin*2+SideBarButton.button_size+self.operations_menu.width())


    def center_side_bar(self) -> None:
        '''
        Center the side bar. (vertical)
        '''        
        self.setFixedHeight(self.margin+self.buttons[-1].y()+SideBarButton.button_size)

