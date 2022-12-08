from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main window
    main_window = QMainWindow()  # Create a main window
    main_window.setMinimumSize(QSize(1280, 720))  # Set the minimum size of the window
    main_window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon
    main_window.setWindowTitle('Event Handling')  # Set the window title
    # Is impossible to modify the layout of a QMainWindow, so we need to create a QWidget and set it as the central widget of the QMainWindow.
    window = QWidget()  # Create a window
    layout = QVBoxLayout()
    main_window.setCentralWidget(window)  # Set the central widget of the window

    def create_button():
        layout.addWidget(QPushButton('New Button'))
    
    # Create a main
    main_button = QPushButton('Add new Button')
    main_button.clicked.connect(create_button)
    layout.addWidget(main_button)
    


    window.setLayout(layout)

    main_window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

