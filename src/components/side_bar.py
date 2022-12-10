from src.components.side_bar_button import SideBarButton
from src.globals import Settings
from PyQt6.QtWidgets import QWidget, QFrame
from dataclasses import dataclass


@dataclass
class SideBar(QWidget):  # QWidget, but temporary is a QFrame just for testing
    '''
    Side Bar contains the tools and the settings of the application.
    '''
    buttons_frame: QFrame
    operations_frame: QFrame
    buttons: list[SideBarButton]  # list of buttons
    margin: int = 8  # margin between the buttons


    def __init__(self, display: QWidget):
        super().__init__(display)
        # ? by instantiating the buttons_frame, the default position will on TOP
        self.buttons_frame = QFrame(self)
        self.load_buttons()  # load the buttons
        self.buttons_frame.setStyleSheet('QFrame{background-color: #2d2d2d; border-radius: 8%;}')
        # ? set the operations_frame on the right side of the buttons_frame
        self.operations_frame = QFrame(self)
        self.operations_frame.setStyleSheet('QFrame{background-color: #dbdbdb; border-radius: 6%; border: 2px solid '+f'{Settings.APP_COLOR.value}'+';}')
        self.operations_frame.setGeometry(self.margin*2+SideBarButton.button_size, 0, self.margin*2, self.margin+self.buttons[-1].y()+SideBarButton.button_size)

        # ? SET ON BOTTOM
        # todo: add this as a function in the menu_bar
        self.setFixedHeight(self.margin+self.buttons[-1].y()+SideBarButton.button_size)

        # ! for testing
        self.buttons[0].clicked.connect(lambda: self.toggle_side_bar())


    def load_buttons(self) -> None:
        '''
        Load the buttons of the side bar.
        '''
        # todo: asociate the buttons with the actions
        # todo: this should be a unit test!
        path = 'resources\\static\\'
        self.buttons = [
            SideBarButton(path+'grid.png', self.buttons_frame),
            SideBarButton(path+'neural-network.png', self.buttons_frame),
            SideBarButton(path+'histogram.png', self.buttons_frame),
            SideBarButton(path+'cube.png', self.buttons_frame),
            SideBarButton(path+'connection.png', self.buttons_frame),
            SideBarButton(path+'nucleus.png', self.buttons_frame),
            SideBarButton(path+'nucleus.png', self.buttons_frame),
            SideBarButton(path+'nucleus.png', self.buttons_frame),
            SideBarButton(path+'log-file.png', self.buttons_frame)]
        for i in range(len(self.buttons)):
            self.buttons[i].setGeometry(self.margin, self.margin+((SideBarButton.button_size+self.margin)*i), SideBarButton.button_size, SideBarButton.button_size)


    def toggle_side_bar(self):
        '''
        Add the toggle effect to the side bar.
        '''
        # todo: still needs an animation
        from src.components.display import Display
        if self.width() == Display.hidden_side_bar_size:
            self.setFixedWidth(Display.showing_side_bar_size)
            self.operations_frame.setFixedWidth(Display.showing_side_bar_size-self.buttons_frame.width())
        else:
            self.setFixedWidth(Display.hidden_side_bar_size)
            self.operations_frame.setFixedWidth(self.margin*2)

