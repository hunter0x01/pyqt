'''
Created on Mar 9, 2015

@author: Sylvain Garcia <garcia.6l20@gmail.com>
'''
import pkg_resources

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *


import sys
import os

from mdedit.editor.mdeditor import *
from mdedit.generator import *

class MainWindow(QMainWindow):
    '''
    MainWindow
    '''

    def __init__(self, filename=None):

        super(QMainWindow,self).__init__()

        self.setWindowTitle('MdEditor')

        self.tab = QTabWidget()

        self.setCentralWidget(self.tab)
        self.setupMenu()

        # default action
        self.css_file = os.path.join(os.path.dirname(__file__),'css','default.css')

        if filename is None:
            self.onOpenAction()
        else:
            self.tab.addTab(MdEditor(filename,parent=self,css_file=self.css_file), filename)

    def setupMenu(self):

        self.file_menu = self.menuBar().addMenu(self.tr('&File'))
        open_action = self.file_menu.addAction(self.tr('&Open'))
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.onOpenAction)

        save_action = self.file_menu.addAction(self.tr('&Save'))
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.onSaveAction)

        saveas_action = self.file_menu.addAction(self.tr('Save&As'))
        saveas_action.setShortcut(QKeySequence.SaveAs)
        saveas_action.triggered.connect(self.onSaveAsAction)

        build_action = self.file_menu.addAction(self.tr('&Build'))
        build_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_B))
        build_action.triggered.connect(self.onBuildAction)

        # shortcuts

        self.shortcuts = []

        shortcut = QShortcut(QKeySequence.Open, self)
        shortcut.setContext(Qt.ApplicationShortcut)
        shortcut.activated.connect(self.onOpenAction)
        self.shortcuts.append(shortcut)

        shortcut = QShortcut(QKeySequence.Save, self)
        shortcut.setContext(Qt.ApplicationShortcut)
        shortcut.activated.connect(self.onSaveAction)
        self.shortcuts.append(shortcut)

        shortcut = QShortcut(QKeySequence.SaveAs, self)
        shortcut.setContext(Qt.ApplicationShortcut)
        shortcut.activated.connect(self.onSaveAsAction)
        self.shortcuts.append(shortcut)

        shortcut = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_B), self)
        shortcut.setContext(Qt.ApplicationShortcut)
        shortcut.activated.connect(self.onBuildAction)
        self.shortcuts.append(shortcut)

        # @TODO
        #self.edit_menu = self.editor.createStandardContextMenu()
        #self.edit_menu.setTitle('&Edit')
        #self.menuBar().addMenu(self.edit_menu)

    def onBuildAction(self):
        current = self.tab.currentWidget()
        if isinstance(current, MdEditor):
            current.onBuildAction()

    def onOpenAction(self):

        result = QFileDialog.getOpenFileName(parent=self,
            caption=self.tr('Open file'),
            directory=QDir.currentPath(),
            filter='Markdown files (*.md)'
        )
        if result is None:
            return

        filename = result[0]

        self.tab.addTab(MdEditor(filename,parent=self,css_file=self.css_file), filename)

    def onSaveAction(self):
        current = self.tab.currentWidget()
        if isinstance(current, MdEditor):
            current.onOnSaveAction()

    def onSaveAsAction(self):
        current = self.tab.currentWidget()
        if isinstance(current, MdEditor):
            current.onOnSaveAsAction()

def mdeditor():

    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.showMaximized()

    exit(app.exec())

def main():
    mdeditor()

if __name__ == '__main__':
    main()
