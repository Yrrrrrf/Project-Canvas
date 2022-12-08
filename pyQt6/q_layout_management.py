from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QPushButton, QGridLayout, QFormLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main window
    main_window = QMainWindow()  # Create a main window
    main_window.setMinimumSize(QSize(480, 240))  # Set the minimum size of the window
    main_window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon
    main_window.setWindowTitle('Layout Management')  # Set the window title

    # Is impossible to modify the layout of a QMainWindow, so we need to create a QWidget and set it as the central widget of the QMainWindow.
    window = QWidget()  # Create a window
    main_window.setCentralWidget(window)  # Set the central widget of the window
    
    # QHBoxLayout - Horizontal layout
    hbox_layout = QHBoxLayout()
    for i in range(5):  # Add 5 buttons to the layout
        hbox_layout.addWidget(QPushButton(f'Button {i}'))

    # QVBoxLayout - Vertical layout
    vbox_layout = QVBoxLayout()
    for i in range(5):  # Add 5 buttons to the layout
        vbox_layout.addWidget(QPushButton(f'Button {i}'))

    # QGridLayout
    # This layout is used to create a grid of widgets, where each widget is placed in a cell of the grid.
    grid_layout = QGridLayout()
    for i in range(5):  # Add 5 buttons to the layout
        for j in range(5):
            grid_layout.addWidget(QPushButton(f'Button {i}'), i, j)

    # QFormLayout - Form layout
    # This layout is used to create forms, where the labels are on the left and any other QWidgets are on the right.
    form_layout = QFormLayout()
    for i in range(5):  # Add 5 buttons to the layout
        form_layout.addRow(f'Label {i}', QPushButton(f'Button {i}'))
    form_layout.addWidget(QPushButton('Extra Button'))

    # Set the layout
    # window.setLayout(hbox_layout)
    # window.setLayout(vbox_layout)
    # window.setLayout(grid_layout)
    window.setLayout(form_layout)

    main_window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

