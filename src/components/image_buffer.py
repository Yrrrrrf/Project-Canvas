# from 
from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtGui import QIcon, QImage, QPixmap, QImageReader
from PyQt6.QtCore import Qt
import sys
from dataclasses import dataclass


@dataclass
class ImageBuffer(QLabel):
    '''
    Image buffer class reference to the image buffer of the application.
    '''
    image: QImage
    image_reader: QImageReader = QImageReader()


    def __init__(self, image: QImage):
        # Create the instance of the ImageBuffer
        super().__init__()
        
        # show only a ROI of the image
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image = image
        self.image_reader.read(self.image)

        self.setText('Image Buffer')

        # get a ROI of the image & update the image
        self.image = self.image.copy(240, 220, 120, 170)

        self.setPixmap(QPixmap.fromImage(self.image))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    window = ImageBuffer(QImage('resources\\img\\lena.png'))
    window.show()
    sys.exit(app.exec())
