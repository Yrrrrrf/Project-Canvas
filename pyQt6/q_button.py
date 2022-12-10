from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main Window
    window = QMainWindow()  # Create a window
    window.setWindowTitle('QPushButton')  # Set the window title
    window.setBaseSize(1280, 720)  # Set the base size of the window. This is the size of the window when it is first shown.
    window.setMinimumSize(1280, 720)  # Set the minimum size of the window
    window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon


    # QPushButton
    button = QPushButton('QPushButton', window)
    button.setGeometry(100, 100, 240, 240)
    button.setStyleSheet('background-color: yellow; color: blue; border-radius: 20%;')  # Set the style sheet of the button
    button.setFont(QFont('Consolas', 20, QFont.Weight.Thin))  # Set the font of the button
    button.setIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the icon of the button
    button.setIconSize(QSize(240, 240))  # Set the size of the icon of the button

    # QMenu
    menu = QMenu()
    menu.setFont(QFont('Consolas', 20, QFont.Weight.Thin))  # Set the font of the button
    menu.addAction('Action 1')
    menu.addAction('Action 2')
    button.setMenu(menu)  # Set the menu of the button


    window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

