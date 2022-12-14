from src.img_operations.load_image import load_cat, open_file
from src.globals import Settings
from src.components.workspace import Workspace
from PyQt6.QtWidgets import QMenuBar, QMenu, QFileDialog
from PyQt6.QtGui import QAction, QFont
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
        # Set the menu bar style sheet
        self.setFont(QFont('Segoe Print', 10, QFont.Weight.Bold))
        menu_bar_style ='QMenuBar{background-color: #2d2d2d; color: white;} QMenuBar::item::selected{background-color: '+f'{Settings.APP_COLOR.value}'+';}'
        menu_style = 'QMenu{background-color: #2d2d2d; color: white; border: 1px solid '+f'{Settings.APP_COLOR.value}'+'; margin: 1px;} QMenu::item::selected{background-color: '+f'{Settings.APP_COLOR.value}'+';}'
        self.setStyleSheet(menu_bar_style+menu_style)
        self.set_menu_bar()


    def set_menu_bar(self):
        '''
        Set all the QMenus and actions of the menu bar.
        '''
        self.set_file_menu()
        self.set_edit_menu()
        self.set_view_menu()
        self.set_tools_menu()
        self.set_help_menu()


    def set_file_menu(self):
        '''
        Set the file menu.
        '''
        file_menu = QMenu('File', self)
        # Add the menu to the menu bar
        select_image = QAction('Select Image', self)
        select_image.setShortcut('Ctrl+O')
        select_image.triggered.connect(lambda: open_file(self))
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
        # Add Separator
        file_menu.addSeparator()
        # Add Save Project action
        random_image = QAction('Random Image', self)
        random_image.setShortcut('Ctrl+R')
        # todo: complete this
        random_image.triggered.connect(lambda: load_cat)
        file_menu.addAction(random_image)
        # Add Separator
        file_menu.addSeparator()
        # Add Exit action
        exit_app = QAction('Exit', self)
        exit_app.setShortcut('Ctrl+W')  # xdn't
        # exit_app.setShortcut('Ctrl+Q')  # xdn't
        exit_app.triggered.connect(QCoreApplication.instance().quit)
        file_menu.addAction(exit_app)

        # Add the menu to the menu bar
        self.addMenu(file_menu)


    def set_edit_menu(self):
        '''
        Set the edit menu.
        '''
        pass


    def set_view_menu(self):
        '''
        Set the view menu.
        '''
        view_menu = QMenu('View', self)
        # Add the zoom in action
        zoom_in = QAction('Zoom In', self)
        zoom_in.setShortcut('Ctrl++')
        zoom_in.triggered.connect(lambda: print(f'[{Settings.SNAPSHOT.value}]    Still working on it...!'))
        view_menu.addAction(zoom_in)
        # Add the zoom out action
        zoom_out = QAction('Zoom Out', self)
        zoom_out.setShortcut('Ctrl+-')
        zoom_out.triggered.connect(lambda: print(f'[{Settings.SNAPSHOT.value}]    Still working on it...!'))
        view_menu.addAction(zoom_out)
        # Add change theme action
        change_theme = QAction('Change Theme', self)
        change_theme.setShortcut('Ctrl+T')
        change_theme.triggered.connect(lambda: print(f'[{Settings.SNAPSHOT.value}]    Still working on it...!\n    The actual color is {Settings.APP_COLOR.value}'))
        view_menu.addAction(change_theme)
        # Add the menu to the menu bar
        self.addMenu(view_menu)
        pass


    def set_tools_menu(self):
        '''
        Set the tools menu.
        '''
        pass

    
    def set_help_menu(self):
        '''
        Set the help menu.
        '''
        help_menu = QMenu('Help', self)
        # Add the about action
        about = QAction('About', self)
        about.setShortcut('Ctrl+H')
        about.triggered.connect(lambda: print(f'[{Settings.SNAPSHOT.value}]    Still working on it...!'))
        help_menu.addAction(about)
        # Add the menu to the menu bar
        self.addMenu(help_menu)
        # help_menu.triggered.connect(print(Settings.))
