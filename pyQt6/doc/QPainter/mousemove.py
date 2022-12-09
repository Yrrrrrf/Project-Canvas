from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Mouse Event")
        self.setWindowIcon(QIcon('images/python.png'))
        self.setMouseTracking(True)

        hbox = QHBoxLayout()

        self.label = QLabel("Mouse Track")
        self.label.setFont(QFont("Times", 15))


        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def mouseMoveEvent(self, event):
        x = self.x()
        y = self.y()

        text = "X: {0}, Y: {1}".format(x,y)

        self.label.setText(text)
        self.update()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())