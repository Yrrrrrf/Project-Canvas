from src.components.side_bar_button import SideBarButton
from src.components.operations_menu import OperationsMenu
from src.components.operation_button import OperationButton
from src.globals import Settings
from src.operations import Operations
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

        # ? Connect the buttons to the toggle function
        self.buttons[0].clicked.connect(lambda: self.toggle(self.buttons[0].name, self.buttons[0].operations))
        self.buttons[1].clicked.connect(lambda: self.toggle(self.buttons[1].name, self.buttons[1].operations))
        self.buttons[2].clicked.connect(lambda: self.toggle(self.buttons[2].name, self.buttons[2].operations))
        self.buttons[3].clicked.connect(lambda: self.toggle(self.buttons[3].name, self.buttons[3].operations)) 
        self.buttons[4].clicked.connect(lambda: self.toggle(self.buttons[4].name, self.buttons[4].operations))
        self.buttons[5].clicked.connect(lambda: self.toggle(self.buttons[5].name, self.buttons[5].operations))
        self.buttons[6].clicked.connect(lambda: self.toggle(self.buttons[6].name, self.buttons[6].operations))
        self.buttons[7].clicked.connect(lambda: self.toggle(self.buttons[7].name, self.buttons[7].operations))
        # for button in self.buttons:
        #     button.clicked.connect(lambda: self.toggle(button.name))


    def toggle(self, name: str, operations: list[dict]) -> None:
        '''
        Toggle the Operations Menu. (show/hide)
        '''
        if self.operations_menu.deployed == True:  # if the operations menu is deployed
            self.operations_menu.hide()  # hide the operations menu
            self.setFixedWidth(self.margin*4+SideBarButton.button_size)
        else:  # if the operations menu is hidden
            self.operations_menu.title.setText(name.lower())  # ? update the title of the operations menu
            self.operations_menu.deploy()  # show the operations menu
            self.setFixedWidth(self.margin*2+SideBarButton.button_size+self.operations_menu.width())
            self.update_operations_menu()  # update the operations menu
        print(name.lower())


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

