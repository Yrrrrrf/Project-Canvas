from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene,QGraphicsItem
from PyQt6.QtGui import QIcon, QPen, QBrush
from PyQt6.QtCore import Qt
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QGraphicsView")
        self.setWindowIcon(QIcon('images/python.png'))

        scene  =QGraphicsScene()

        greenBrush = QBrush(Qt.GlobalColor.green)
        yellowBrush = QBrush(Qt.GlobalColor.yellow)

        redPen = QPen(Qt.GlobalColor.red)
        redPen.setWidth(7)

        ellipse = scene.addEllipse(100,100, 200,200, redPen, greenBrush)
        rect = scene.addRect(-100,-100, 200,200, redPen, yellowBrush)

        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)




        view = QGraphicsView(scene, self)
        view.setGeometry(0,0, 680, 400)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())