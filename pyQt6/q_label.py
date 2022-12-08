from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)  # Manage the GUI application's control flow and main settings.
    # Main Window
    window = QMainWindow()  # Create a window
    window.setWindowTitle('QLabel')  # Set the window title
    window.setBaseSize(1280, 720)  # Set the base size of the window. This is the size of the window when it is first shown.
    # window.setGeometry(100, 100, 1280, 720)  # Set the window geometry
    window.setMinimumSize(1280, 720)  # Set the minimum size of the window
    window.setWindowIcon(QIcon('pyQt6/doc/qt_logo.png'))  # Set the window icon


    # QLabel
    label = QLabel("QLabel example", window)
    label.setText('New Text')
    label.setFixedSize(240, 360)  # Set the size of the label that contains the text
    # label.move(1000, 100)  # Move the label (x, y) pixels from the original position (fixed size)
    label.setFont(QFont('Consolas', 20))  # Set the font of the label
    label.setStyleSheet('color: magenta;')  # Set the style sheet of the label

    # QPixmap allow us to load an image from a file and display it on a label
    pixmap = QPixmap('pyQt6/doc/qt_logo.png')
    label.setPixmap(pixmap)  # Set the pixmap of the label

    # QMovie allow us to load an animated gif and display it on a label
    movie = QMovie('pyQt6/doc/sky.gif')
    label.setMovie(movie)  # Set the movie of the label
    movie.setSpeed(500)  # Set the [%] speed of the movie
    movie.start()  # Start the movie



    # Display the window
    window.show()  # Show the window    
    sys.exit(app.exec())  # Start the event loop

