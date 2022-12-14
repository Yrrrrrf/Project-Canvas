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
    image: str
    q_image: QImage
    import_icon: str = Resources.ICONS.value+'import.png'
    delete_icon: str = Resources.ICONS.value+'delete.png'
    replace_icon: str=Resources.ICONS.value+'replace.png'


    def __init__(self, parent: QWidget, image: str = import_icon):
        '''
        Initialize the ImageBuffer class.
        Needs the image as a parameter.
        :param" image: The image that is displayed in the image buffer.
        '''
        super().__init__(parent)        
        # self.setScaledContents(True)
        style = 'QLabel {background-color: lightgray; border-radius: 10%;}'
        hover_style = "QLabel:hover{background-color : lightgray;}"
        self.setStyleSheet(style+hover_style)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        if image == Resources.ICONS.value+'import.png':
            self.default_import()
        else:
            self.import_image()


    def set_image(self, image: str) -> None:
        '''
        Set the image of the image buffer.
        '''
        self.image = image
        self.q_image = QImage(self.image)
        # self.image_reader.read(self.q_image)
        self.setPixmap(QPixmap.fromImage(self.q_image))
        # self.setFixedSize(self.q_image.width(), self.q_image.height())


    def default_import(self) -> None:
        '''
        Import an image from the file system.
        '''
        self.image = Resources.ICONS.value+'import.png'
        self.import_button = QPushButton(self)
        self.import_button.setIcon(QIcon(self.image))
        self.import_button.setIconSize(QSize(64, 64))
        self.import_button.setFixedSize(72, 72)
        self.import_button.setStyleSheet('QPushButton {background-color: white; border: 1px solid white; border-radius: 10%;} QPushButton:hover{background-color : lightgray;}')
        # set on click event
        self.import_button.clicked.connect(self.import_image)
        # center the button
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.import_button)


    def import_image(self) -> None:
        '''
        Import an image from the file system.
        '''
        try:
            self.set_image(open_file(self))
            # center image by default
            self.import_button.deleteLater()
        except:
            QMessageBox.critical(self, 'Error', 'Please select a file.')
            self.default_import()
            self.update()

