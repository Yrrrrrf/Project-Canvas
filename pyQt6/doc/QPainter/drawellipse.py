from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Drawing Ellipse")
        self.setWindowIcon(QIcon('images/python.png'))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.red, Qt.BrushStyle.CrossPattern))

        painter.drawEllipse(100,100,400,200)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())