from src.globals import Settings, Resources
from src.img_operations.load_image import open_file
from PyQt6.QtWidgets import QLabel, QPushButton, QDialog, QFileDialog, QMessageBox, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QImage, QPixmap, QImageReader, QKeySequence, QShortcut
from PyQt6.QtCore import Qt, QSize
import sys
from dataclasses import dataclass


@dataclass
class ImageBuffer(QLabel):
    '''
    Image buffer class reference to the image buffer of the application.
    '''
    image_path: str
    q_image: QImage
    selected_image: QImage
    import_icon: str = Resources.ICONS.value+'import.png'
    delete_icon: str = Resources.ICONS.value+'delete.png'
    replace_icon: str=Resources.ICONS.value+'replace.png'
    empty: bool = True  # The buffer is empty
    selected: bool = False  # The buffer is selected


    def __init__(self, width, height,  parent: QWidget, image_path: str = import_icon):
        '''
        Initialize the ImageBuffer class.
        Needs the image as a parameter.
        :param" image: The image that is displayed in the image buffer.
        '''
        super().__init__(parent)       
        self.setFixedSize(width, height)
        style = 'QLabel {background-color: lightgray; border-radius: 10%;}'
        hover_style = "QLabel:hover{background-color : lightgray; border : 1px solid gray;}"
        self.setStyleSheet(style+hover_style)

        # center the import button
        self.c_layout = QHBoxLayout()
        self.setLayout(self.c_layout)
        self.set_import_button()


    def set_import_button(self) -> None:
        '''
        Import an image from the file system.
        '''
        self.import_button = QPushButton(self)  # create the button
        self.import_button.setIcon(QIcon(self.import_icon))  # set the icon
        self.import_button.setIconSize(QSize(64, 64))  # set the icon size
        self.import_button.setFixedSize(72, 72)  # set the button size
        self.import_button.setStyleSheet('QPushButton {background-color: white; border: 1px solid white; border-radius: 10%;} QPushButton:hover{background-color : lightgray;}')
        self.import_button.clicked.connect(self.import_image)
        # center the button
        self.import_button.move((int)((self.width()-self.import_button.width())/2), (int)((self.height()-self.import_button.height())/2))


    def import_image(self) -> None:
        '''
        Import an image from the file system.
        Creates a file dialog to select the image.
        If the image is not valid, it will show an error message.
        '''
        try:
            self.image_path = open_file(self)
            global active_buffer
            active_buffer = self
            self.set_image(self.image_path)
        except:
            QMessageBox.critical(self, 'Error', 'Please select a file.')
            self.update()


    def set_image(self, image: str) -> None:
        '''
        Set the image of the image buffer.
        '''
        # print(image)
        self.image_path = image
        self.q_image = QImage(self.image_path)
        self.setPixmap(QPixmap.fromImage(self.q_image))
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.empty = False  # the buffer is not empty anymore
        # self.selected_image = self.q_image  # ? Set the selected image to the image buffer image
        self.set_edit_buttons()


    def set_edit_buttons(self) -> None:
        '''
        Set the edit buttons.
        '''
        self.import_button.hide()




