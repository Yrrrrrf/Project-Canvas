from src.globals import Settings
from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
from dataclasses import dataclass
import cv2 as cv
import numpy as np


@dataclass
class OperationButton(QPushButton):
    '''
    OperatoinButton class contains executes an operation to an image.
    Every operation is a button. The button is a child of the operations frame.
    If the unit test associated to the operation is passed, the button will be enabled.
    '''
    operations_menu: QWidget  # ? Parent Widget
    # operation: dict  # contains the name and the function of the operation
    icon: str
    button_height: int = 32
    icon_size: int = 24


    def __init__(self, operations_menu: QWidget, operation: dict):
        super().__init__(operations_menu)
        self.name = list(operation.keys())[0]  # Assign the name of the button
        self.operation = operation[self.name]  # Assign the function of the button
        self.operations_menu = operations_menu
        button_style = 'QPushButton {border-radius: 10%; background: white; color: gray;} '
        hover_style = 'QPushButton:hover {border-radius: 8%; border: 3px solid '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(button_style + hover_style)
        self.setFont(QFont('Segoe Print', 10, QFont.Weight.Bold))
        # self.setIcon(QIcon(Resources.ICONS.value+icon))
        self.setIconSize(QSize(self.icon_size, self.icon_size))
        # self.setFixedSize(122, self.button_height)
        self.setText(self.name)

        self.set_operation()


    def set_operation(self) -> None:
        '''
        Set the operation of the button.
        '''
        # path = 'resources\\img\\lena.png'
        self.clicked.connect(self.execute_operation)


    def execute_operation(self) -> None:
        '''
        Execute the operation of the button.
        Converts an array to a QImage and sets it as the active image.
        Also sets the active image path.
        '''
        try:
            from src.components.image_buffer import active_buffer, QImage, QPixmap
            # global active_image_path
            cv_image = cv.imread(active_buffer.image_path)
            # apply the operation
            # cv.imshow('image', cv_image)
            cv_image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)
            cv_image = self.operation(cv_image)
            print(f'Executing operation: {self.name}')
            # cast it as a numpy ndarray
            cv_image = np.ndarray(shape=(cv_image.shape[0], cv_image.shape[1], 3), dtype=np.uint8, buffer=cv_image.data, strides=(cv_image.strides[0], cv_image.strides[1], cv_image.strides[2]))
            height, width, bytesPerComponent = cv_image.shape
            bytesPerLine = bytesPerComponent*width
            active_buffer.q_image = QImage(cv_image.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            active_buffer.setPixmap(QPixmap.fromImage(active_buffer.q_image))
            # save the image
            active_buffer.image_path = 'resources\\img\\temp\\edit.png'  # update image path
            # img = cv.imwrite('resources\\img\\temp\\edit.png', cv_image., format=)  # save it in the temp directory 
            # save it in bgr format
            cv_image = cv.cvtColor(cv_image, cv.COLOR_RGB2BGR)
            cv.imwrite('resources\\img\\temp\\edit.png', cv_image)
            # cv.imshow('image', img)

            active_buffer.update()
        except ImportError:
            print('\nError: No image selected')

