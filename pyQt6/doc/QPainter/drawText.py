from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QTextDocument
from PyQt6.QtCore import QRect, Qt, QRectF
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Drawing Text")
        self.setWindowIcon(QIcon('images/python.png'))


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawText(100,100, "PyQt6 Course")

        rect = QRect(100, 150, 250,25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "PyQt6 Course - Udemy.com")


        document = QTextDocument()
        rect2 = QRectF(0,0, 250,250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Welcome to PyQt6 Course </b><i>Udemy Course </i> \n <font size ='15' color='red'>Enjoy The Course</font>")

        document.drawContents(painter, rect2)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())