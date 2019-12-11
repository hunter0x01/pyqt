from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.vboxLayout = QVBoxLayout()

        self.buttons = []

        # Works:
        # self.button_1 = QPushButton('Button 1 manual', self)
        # main_layout.addWidget(self.button_1)
        # self.buttons.append(self.button_1)
        # self.button_1.clicked.connect(self.button_pushed)

        # self.button_2 = QPushButton('Button 2 manual', self)
        # main_layout.addWidget(self.button_2)
        # self.buttons.append(self.button_2)
        # self.button_2.clicked.connect(self.button_pushed)

        self.gridLayout = QGridLayout()
 
        # self.gridLayout.addWidget(QPushButton("CE"), 0, 0)
        # self.gridLayout.addWidget(QPushButton("C"), 0, 1)
        # self.gridLayout.addWidget(QPushButton("Backspace"), 0, 2)
        # self.gridLayout.addWidget(QPushButton("/"), 0, 3)
 
        # self.gridLayout.addWidget(QPushButton("7"), 1, 0)
        # self.gridLayout.addWidget(QPushButton("8"), 1, 1)
        # self.gridLayout.addWidget(QPushButton("9"), 1, 2)
        # self.gridLayout.addWidget(QPushButton("*"), 1, 3)
 
        # self.gridLayout.addWidget(QPushButton("4"), 2, 0)
        # self.gridLayout.addWidget(QPushButton("5"), 2, 1)
        # self.gridLayout.addWidget(QPushButton("6"), 2, 2)
        # self.gridLayout.addWidget(QPushButton("-"), 2, 3)
 
        # self.gridLayout.addWidget(QPushButton("1"), 3, 0)
        # self.gridLayout.addWidget(QPushButton("2"), 3, 1)
        # self.gridLayout.addWidget(QPushButton("3"), 3, 2)
        # self.gridLayout.addWidget(QPushButton("+"), 3, 3)
 
        # self.gridLayout.addWidget(QPushButton("0"), 4, 1)
        # self.gridLayout.addWidget(QPushButton("."), 4, 2)
        # self.gridLayout.addWidget(QPushButton("="), 4, 3)
 

        # Doesn't work:
        ipaddr = 1
        for idx in range (1, 18):
            # print(idx)
            # button = QPushButton(' {} '.format(idx), self)
            # button.clicked.connect(self.button_pushed)
            # self.buttons.append(button)
            # main_layout.addWidget(button)
            for idx2 in range (1, 16):
                self.gridLayout.addWidget(QPushButton(' {} '.format(ipaddr), self), idx, idx2)
                ipaddr = ipaddr + 1




            print(idx)

        self.setLayout(self.gridLayout)
        self.show()
 



    def button_pushed(self):
        print(' {} '.format(self.buttons.index(self.sender())+1))


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())