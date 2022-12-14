import sys
from PyQt6.QtWidgets import QWidget, QStackedWidget, QListWidget, QHBoxLayout, QApplication, QFormLayout, QLineEdit, QRadioButton, QLabel, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter, QImage, QCursor

class stackedExample(QWidget):

   def __init__(self):
      super(stackedExample, self).__init__()
      self.leftlist = QListWidget ()
      self.leftlist.insertItem (0, 'Contact' )
      self.leftlist.insertItem (1, 'Personal' )
      self.leftlist.insertItem (2, 'Educational' )
		
      self.stack1 = QWidget()
      self.stack2 = QWidget()
		
      self.stack1UI()
      self.stack2UI()
		
      self.Stack = QStackedWidget (self)
      self.Stack.addWidget (self.stack1)
      self.Stack.addWidget (self.stack2)
		
      hbox = QHBoxLayout(self)
      hbox.addWidget(self.Stack)
      hbox.addWidget(self.leftlist)

      self.setLayout(hbox)
      self.leftlist.currentRowChanged.connect(self.display)
      self.setGeometry(300, 50, 10,10)
      self.setWindowTitle('StackedWidget demo')
      self.show()
		
   def stack1UI(self):
      layout = QFormLayout()
      layout.addRow("Name",QLineEdit())
      layout.addRow("Address",QLineEdit())
      #self.setTabText(0,"Contact Details")
      self.stack1.setLayout(layout)
		
   def stack2UI(self):
      layout = QFormLayout()
      sex = QHBoxLayout()
      sex.addWidget(QRadioButton("Male"))
      sex.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Sex"),sex)
      layout.addRow("Date of Birth",QLineEdit())
		
      self.stack2.setLayout(layout)


   def display(self,i):
      self.Stack.setCurrentIndex(i)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec())
