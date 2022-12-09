from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QTextEdit, QComboBox
from PyQt6.QtGui import QIcon, QPainter, QFont, QColor
from PyQt6.QtCore import Qt
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Drawing Text")
        self.setWindowIcon(QIcon('images/python.png'))

        self.textToDraw = ""
        self.fontSize = 5

        hbox = QHBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(200)

        self.combo = QComboBox()
        self.combo.setFont(QFont("Times", 15))
        self.combo.addItem("12")
        self.combo.addItem("14")
        self.combo.addItem("16")
        self.combo.addItem("18")

        btn = QPushButton("Create Text")
        btn.setFont(QFont("Times", 15))
        btn.clicked.connect(self.create_text)





        hbox.addWidget(self.textEdit)
        hbox.addWidget(self.combo)
        hbox.addWidget(btn)

        self.setLayout(hbox)


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QColor(168, 30,3))
        painter.setFont(QFont("Times", self.fontSize))
        painter.drawText(event.rect(), Qt.AlignmentFlag.AlignTop, self.textToDraw)
        painter.end()



    def create_text(self):
        self.fontSize = int(self.combo.itemText(self.combo.currentIndex()))
        self.textToDraw = self.textEdit.toPlainText()
        self.update()




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())