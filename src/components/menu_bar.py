from src.globals import Settings
from PyQt6.QtWidgets import QMenuBar, QMenu, QFileDialog
from PyQt6.QtGui import QAction, QImageReader
from PyQt6.QtCore import QCoreApplication
import cv2 as cv
from dataclasses import dataclass


@dataclass
class MenuBar(QMenuBar):
    '''
    Menu Bar class contains the menus and the options of the application.
    Set the menu bar of the main window.
    '''
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"background-color: #2d2d2d; color: white; min-height: {Settings.TOOLBAR_HEIGHT.value}px;")
        self.set_menu_bar()


    def set_menu_bar(self):
        self.set_file_menu()
        self.set_edit_menu()
        self.set_view_menu()
        self.set_tools_menu()
        self.set_help_menu()


    def set_file_menu(self):
        file_menu = QMenu('File', self)
        # Add the menu to the menu bar
        select_image = QAction('Select Image', self)
        select_image.setShortcut('Ctrl+O')
        select_image.triggered.connect(self.open_file)
        file_menu.addAction(select_image)
        # Add Save Image action
        save_image = QAction('Save Image', self)
        save_image.setStatusTip('Save the image in the current state')
        save_image.setShortcut('Ctrl+S')
        file_menu.addAction(save_image)
        # Add Save Image As action
        save_image_as = QAction('Save Image As', self)
        save_image_as.setShortcut('Ctrl+Shift+S')
        file_menu.addAction(save_image_as)
        # Add a separator
        file_menu.addSeparator()
        # Add Exit action
        exit_app = QAction('Exit', self)
        exit_app.setShortcut('Ctrl+Q')  # xdn't
        exit_app.triggered.connect(QCoreApplication.instance().quit)
        file_menu.addAction(exit_app)

        # Add the menu to the menu bar
        self.addMenu(file_menu)


    def open_file(self):
        name = QFileDialog.getOpenFileName(self, 'Open File', '.\\resources\\img','Image Files ( *.bmp  *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm)')[0]
        cv.imshow('Image', cv.imread(name))
        print(f"\nImage selected: \033[32m{name.split('/')[-1]}\x1B[37m \
                \n    Width: {cv.imread(name).shape[1]}\
                \n    Height: {cv.imread(name).shape[0]}\
                \n    Channels: {cv.imread(name).shape[2]}\n")


    def set_edit_menu(self):
        pass


    def set_view_menu(self):
        pass


    def set_tools_menu(self):
        pass

    
    def set_help_menu(self):
        help_menu = QMenu('Help', self)
        # Add the about action
        about = QAction('About', self)
        about.setShortcut('Ctrl+H')
        about.triggered.connect(lambda: print('Still working on it...!'))
        help_menu.addAction(about)
        # Add the menu to the menu bar
        self.addMenu(help_menu)
        # help_menu.triggered.connect(print(Settings.))