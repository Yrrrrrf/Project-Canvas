from src.components.side_bar_button import SideBarButton
from src.components.operations_menu import OperationsMenu
from src.components.operation_button import OperationButton
from src.globals import Settings
from src.operations import Operations
from PyQt6.QtWidgets import QWidget, QFrame, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor
from dataclasses import dataclass
import time


@dataclass
class SideBar(QWidget):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    buttons_frame: QFrame
    operations_menu: OperationsMenu
    buttons: list[SideBarButton]
    margin: int = 8  # margin between the buttons


    def __init__(self, display: QWidget):
        super().__init__(display)
        # ? by instantiating the buttons_frame, the default position will on TOP
        self.buttons_frame = QFrame(self)
        self.buttons_frame.setStyleSheet('QFrame{background-color: #2d2d2d; border-radius: 8%;}')
        self.buttons_frame.setFixedWidth(self.margin*2+SideBarButton.button_size)

        self.operations_menu = OperationsMenu(self)
        self.load_buttons()
        
        # ? set the operations_menu on the right side of the buttons_frame
        self.operations_menu.setGeometry(self.margin*2+SideBarButton.button_size, 0, self.margin*2, self.margin+self.buttons[-1].y()+SideBarButton.button_size)

        # ? SET ON BOTTOM
        # todo: add this as a function in the menu_bar
        # self.setFixedHeight(self.margin+self.buttons[-1].y()+SideBarButton.button_size)

        self.operations_menu.setFixedWidth(256-self.buttons_frame.width())
        # self.operations_menu.setFixedHeight(self.height())

    def load_buttons(self) -> None:
        '''
        Load the buttons of the side bar.
        '''
        # todo: asociate the buttons with the actions
        # todo: this should be a unit test!
        self.buttons = []
        i = 0
        for operation in Operations:
            op_button = SideBarButton(operation.name, operation.value, self.buttons_frame)
            # set geometry
            op_button.setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*i), SideBarButton.button_size, SideBarButton.button_size)
            # op_button.setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*op_button.data[0]), SideBarButton.button_size, SideBarButton.button_size)
            # op_button.setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*op_button.data[0]), SideBarButton.button_size, SideBarButton.button_size)
            # op_button.clicked.connect(lambda: self.toggle_side_bar(op_button.name))
            self.buttons.append(op_button)
            i+=1
        # for button_data in Operations:
        #     op_button = SideBarButton(button_data.value, self.buttons_frame)
        #     op_button.setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*op_button.data[0]), SideBarButton.button_size, SideBarButton.button_size)
        #     # op_button.clicked.connect(lambda: self.toggle_side_bar(op_button.name))
        #     self.buttons.append(op_button)


        # todo: the button should recive a Enum as a constructor parameter
        # todo: the button should recive a Enum as a constructor parameter
        # todo: the button should recive a Enum as a constructor parameter


        self.buttons[0].clicked.connect(lambda: self.toggle_side_bar(self.buttons[0].name))
        self.buttons[1].clicked.connect(lambda: self.toggle_side_bar(self.buttons[1].name))
        self.buttons[2].clicked.connect(lambda: self.toggle_side_bar(self.buttons[2].name))
        self.buttons[3].clicked.connect(lambda: self.toggle_side_bar(self.buttons[3].name)) 
        self.buttons[4].clicked.connect(lambda: self.toggle_side_bar(self.buttons[4].name))
        self.buttons[5].clicked.connect(lambda: self.toggle_side_bar(self.buttons[5].name))
        self.buttons[6].clicked.connect(lambda: self.toggle_side_bar(self.buttons[6].name))
        self.buttons[7].clicked.connect(lambda: self.toggle_side_bar(self.buttons[7].name))
        self.buttons[8].clicked.connect(lambda: self.toggle_side_bar(self.buttons[8].name))

        # TODO: Why this doesn't work?!?!
        # for button in self.buttons:
        #     button.clicked.connect(lambda: self.toggle_side_bar(button.name))
        # for i in range(len(self.buttons)):
        #     self.buttons[i].clicked.connect(lambda: self.toggle_side_bar(self.buttons[i].name))




    # def toggle_side_bar(title) -> None:
        # SideBar.operations_menu.setFixedWidth(SideBar.margin*2)
    
        # from src.components.display import Display
        # if SideBar.width() == Display.hidden_side_bar_size:
            # todo: make this an attribute of the class (as a boolean)
            # SideBar.setFixedWidth(Display.showing_side_bar_size)
            # SideBar.operations_menu.setFixedWidth(Display.showing_side_bar_size-self.buttons_frame.width())
            # SideBar.show_operations_menu(title)  #
        # else:
            # SideBar.setFixedWidth(Display.hidden_side_bar_size)
            # SideBar.operations_menu.setFixedWidth(SideBar.margin*2)
            # print(title)

    # todo: this should be implemented using Operations Enum xd
    def toggle_side_bar(self, title: str) -> None:
        '''
        Add the toggle effect to the side bar.
        '''
        # todo: still needs an animation
        self.operations_menu.setFixedWidth(self.margin*2)

        from src.components.display import Display
        if self.width() == Display.hidden_side_bar_size:
            # todo: make this an attribute of the class (as a boolean)
            self.setFixedWidth(Display.showing_side_bar_size)
            self.operations_menu.setFixedWidth(Display.showing_side_bar_size-self.buttons_frame.width())
            self.show_operations_menu(title)  #
        else:
            self.setFixedWidth(Display.hidden_side_bar_size)
            self.operations_menu.setFixedWidth(self.margin*2)
            print(f'Hide {title} menu')


    def show_operations_menu(self, name: str) -> None:
        '''
        Show the operations menu.
        Update the title & buttons of the operations menu.
        The operations buttons are loaded from the operations_menu class.
        '''
        
        # print(self.operations_menu.title.text())


        # todo: for operations in Operations(Enum):


        operations = Operations.PIXEL.value


        
        # create the operations buttons and add them to the operations menu
        # self.ops_button = OperationButton()





        # Set the title of the operations menu
        # self.operations_menu.title.setText(list(operations.keys())[0])
        # list operations values
        # operations_values = list(operations.values())
        # get the operations values
        # print(operations_values)



            # set the operation name & icon
            # self.operations_menu.buttons[i].setText(operation_name)
            # self.operations_menu.buttons[i].setIcon(operation_icon)
            # # self.operations_menu.buttons[i].setIconSize(QSize(32, 32))
            # self.operations_menu.buttons[i].setFixedWidth(self.operations_menu.width()-self.operations_menu.margin*2)
            # self.operations_menu.buttons[i].setFixedHeight(self.operations_menu.margin*2+self.operations_menu.buttons[i].iconSize().height())
            # self.operations_menu.buttons[i].setGeometry(self.operations_menu.margin, self.operations_menu.margin+self.operations_menu.title.height()+((self.operations_menu.margin+self.operations_menu.buttons[i].height())*i), self.operations_menu.buttons[i].width(), self.operations_menu.buttons[i].height())
            # # self.operations_menu.buttons[i].clicked.connect(lambda: print(operation_name))
            # self.operations_menu.buttons[i].clicked.connect(lambda: print(operation_name))
            # self.operations_menu.buttons[i].show()


        # get the key name, that corresponds to the name & the icon
 


