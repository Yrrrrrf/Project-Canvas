from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main Window
    window = QMainWindow()  # Create a window
    window.setWindowTitle('QLineEdit')  # Set the window title
    window.setBaseSize(1280, 720)  # Set the base size of the window. This is the size of the window when it is first shown.
    # window.setGeometry(100, 100, 1280, 720)  # Set the window geometry
    window.setMinimumSize(1280, 720)  # Set the minimum size of the window
    window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon


    # QLineEdit
    line_edit = QLineEdit(window)
    line_edit.setGeometry(100, 100, 320, 40)
    line_edit.setPlaceholderText('Enter your password here')
    # line_edit.setText('default text')
    line_edit.setStyleSheet('color: blue;')  # Set the style sheet of the line edit
    line_edit.setFont(QFont('Consolas', 16, QFont.Weight.Thin))  # Set the font of the line edit
    # line_edit.setEnabled(False)  # Set the line edit enabled or disabled
    line_edit.setEchoMode(QLineEdit.EchoMode.Password)  # Set the echo mode of the line edit



    window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

