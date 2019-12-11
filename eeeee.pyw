from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

def handler(item, column_no):
    print(item, column_no)

def main():
    app = QApplication(sys.argv)
    win = QTreeWidget()

    items = [QTreeWidgetItem("item: {}".format(i)) for i in range(10)]
    win.insertTopLevelItems(0, items)
    win.itemDoubleClicked.connect(handler)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()