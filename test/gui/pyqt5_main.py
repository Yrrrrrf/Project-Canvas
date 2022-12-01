from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def main_window():
    app = QApplication(sys.argv)
    window = QMainWindow
    window.setGeometry(200, 200, 1080, 720)
    window.setWindowTitle("Project Canvas")

    window.show()
    sys.exit(app.exec_())


main_window()