from src.templates import templates
from src.components.visualizer import Visualizer
from src.components.image_buffer import ImageBuffer
from src.img_operations.load_image import load_cat
from PyQt6.QtWidgets import QWidget, QFrame, QScrollArea, QSpinBox, QPushButton
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QKeySequence, QShortcut, QPalette
from dataclasses import dataclass


@dataclass
class Workspace(QScrollArea):
    '''
    Workspace class reference to the workspace of the application.
    Manage the visualizer that are inside the workspace.
    '''
    visualizer: list[Visualizer]


    def __init__(self, display: QWidget, visualizer: list[Visualizer] = []):
        '''
        Initialize the Workspace class.
        Needs the display widget as a parameter, which is the main window of the application.
        '''
        super().__init__(display)
        # set scroll content
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setBackgroundRole(QPalette.ColorRole.Dark)


        # set test layout
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: #4A4A4A; border-color: blue;')
        self.visualizer = []

        # self.select_template()
        # self.visualizer.append(Visualizer(self.frame, 512, 512, 1.0, 16, 't'))
        self.visualizer.append(Visualizer(self.frame, scale=1.0, margin=16, template='cross'))
        self.visualizer[0].move(64, 64)
        self.frame.setFixedSize(self.visualizer[0].width()+128, self.visualizer[0].height()+128)
        self.setWidget(self.frame)


        self.shortcut = QShortcut(QKeySequence("Ctrl+L"), self)


    def select_template(self):
        '''
        Select the template of the visualizer.
        '''
        # create a dialog 
        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(QRect(270, 280, 211, 81))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(len(templates)-1)
        self.spinBox.setSingleStep(1)
        # set font
        font = self.spinBox.font()
        font.setPointSize(16)
        self.spinBox.setFont(font)
        # set alignment
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # set value
        self.spinBox.setValue(0)
        # set prefix
        self.spinBox.setPrefix('Template: ')
        self.spinBox.setSuffix(f'/{len(templates)-1}')
        self.spinBox.setReadOnly(False)
        # set the name of the template as suffix


        # confirmation button
        self.confirm = QPushButton(self)
        self.confirm.setGeometry(QRect(270, 380, 211, 81))
        self.confirm.setObjectName("confirm")
        self.confirm.setText('Confirm')
        self.confirm.clicked.connect(lambda: self.set_template())

        self.spinBox.show()


    def set_template(self):
        '''
        Set the template of the visualizer.
        '''
        self.template = self.spinBox.value()
        self.spinBox.hide()
        self.confirm.hide()
        print(self.template)

        # self.visualizer.append(Visualizer(self.frame, scale=1.0, template='t'))
        # set it by index
        # print(templates[list(templates.keys())[0]], '')
        self.visualizer.append(Visualizer(self.frame, scale=1.0, margin=16, template='cross'))
        # self.visualizer.append(Visualizer(self.frame, scale=1.0, template=templates[list(templates.keys())[self.template]]))

        self.visualizer[0].move(64, 64)
        self.frame.setFixedSize(self.visualizer[0].width()+128, self.visualizer[0].height()+128)
        self.setWidget(self.frame)


