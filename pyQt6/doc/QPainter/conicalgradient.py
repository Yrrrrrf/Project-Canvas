from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QConicalGradient, QBrush, QPen, QPainter
from PyQt6.QtCore import Qt
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QConicalGradient")
        self.setWindowIcon(QIcon('images/python.png'))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.SolidLine))

        concicalGradient = QConicalGradient(100,100,10)

        concicalGradient.setColorAt(0.0, Qt.GlobalColor.red)
        concicalGradient.setColorAt(0.8, Qt.GlobalColor.green)
        concicalGradient.setColorAt(1.0, Qt.GlobalColor.yellow)
        painter.setBrush(QBrush(concicalGradient))

        painter.drawRect(10,10, 200,200)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())