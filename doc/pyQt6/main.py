from PyQt6.QtWidgets import QApplication, QWidget, QIcon
import sys


# App Launcher
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    window = QWidget()  # Create a window
    window.setWindowTitle('Project Canvas')  # Set the window title
    window.show()  # Show the window
    sys.exit(app.exec())
