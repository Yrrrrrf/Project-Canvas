from PyQt6 import QtGui

# Create a QImage with a fixed size
image = QtGui.QImage(20, 100, QtGui.QImage.Format.Format_RGB32)

# Set the pixel at position (x, y) to the given color
image.setPixel(90, 50, QtGui.qRgb(255, 0, 0))

# Save the image to a file
image.save('image.png')


