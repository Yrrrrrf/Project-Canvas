from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QRadialGradient, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QRadialGradient")
        self.setWindowIcon(QIcon('images/python.png'))


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))

        radialGradient = QRadialGradient(100,100,100)

        radialGradient.setColorAt(0.4, Qt.GlobalColor.darkGray)
        radialGradient.setColorAt(0.8, Qt.GlobalColor.green)
        radialGradient.setColorAt(1.0, Qt.GlobalColor.yellow)
        painter.setBrush(QBrush(radialGradient))


        painter.drawRect(10,10,200,200)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())