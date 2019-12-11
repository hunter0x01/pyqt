# -*- coding: utf-8 -*- 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.setCentralWidget(self.table)
        data1 = ['row1','row2','row3','row4']
        data2 = ['1','2.0','3.00000001','3.9999999']

        self.table.setRowCount(4)

        for row in range(4):
            item1 = QTableWidgetItem(data2[row])
            if row % 2 == 0:
                item1.setBackground(QColor(255, 128, 128))
            self.table.setItem(row,0,item1)

        self.table.item(1,0).setBackground(QColor(125,125,125))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())