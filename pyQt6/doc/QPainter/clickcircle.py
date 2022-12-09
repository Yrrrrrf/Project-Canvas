from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter
from PyQt6.QtCore import QRect, Qt
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Drawing Circle")
        self.setWindowIcon(QIcon('images/python.png'))

        self.pos1 = [0,0]
        self.pos2 = [0,0]

    def paintEvent(self, event):
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]

        painter = QPainter()
        painter.begin(self)

        rect = QRect(self.pos1[0], self.pos1[1], width, height)

        startAngle = 0
        arLength = 360 * 16
        painter.drawArc(rect, startAngle, arLength)
        painter.end()



    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = self.pos().x(), self.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = self.pos().x(), self.pos().y()

        self.update()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())