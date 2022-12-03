# Digital Image Processing "Project Canvas"
# 2120019
# Reza Campos Fernando Bryan

from PyQt5 import QtCore, QtGui, QtWidgets
from app_contents.app import Ui_ProjectCanvas

# App Launcher
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectCanvas = QtWidgets.QMainWindow()
    ui = Ui_ProjectCanvas()
    ui.setupUi(ProjectCanvas)
    ProjectCanvas.show()
    sys.exit(app.exec_())

