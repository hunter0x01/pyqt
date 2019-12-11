'''
Created on Mar 9, 2015

@author: Sylvain Garcia <garcia.6l20@gmail.com>
'''
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5 import uic
# import pymysql
# try:
#     import PyQt5.QtWebEngineWidgets as QtWeb
# except ImportError:
#     import PyQt5.QtWebKitWidgets as QtWeb

# from . import PyQt5 PythonQtError


# To test if we are using WebEngine or WebKit

try:
    from PyQt5.QtWebEngineWidgets import QWebEnginePage
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWebEngineWidgets import QWebEngineSettings
    from PyQt5 import QtWebKitWidgets
except ImportError:
    from PyQt5.QtWebKitWidgets import QWebPage as QWebEnginePage
    from PyQt5.QtWebKitWidgets import QWebView as QWebEngineView
    from PyQt5.QtWebKit import QWebSettings as QWebEngineSettings
    from PyQt5 import QtWebKitWidgets
    WEBENGINE = False



from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# try:
#     import PyQt5.QtWebEngineWidgets as QtWeb
# except ImportError:
#     import PyQt5.QtWebKitWidgets as QtWeb

# from PyQt5.QtWebKitWidgets import *

# from PyQt5.QtWebEngineWidgets import *

from mdedit.editor.syntaxhighlighter.md import *
from mdedit.generator import *

import os

class MdFileEditor(QTextEdit):
    '''
    classdocs
    '''
    
    save = pyqtSignal()
    build = pyqtSignal()
    changed = pyqtSignal()
    
    def __init__(self):
        '''
        Constructor
        '''
        super(QTextEdit,self).__init__()
        
        self.setReadOnly(False)
        #self.setOpenExternalLinks(True)
        self.setUndoRedoEnabled(True)
        
        mainlayout = QGridLayout()
        self.setLayout(mainlayout)
        
        self.highlighter = MdHighlighter(self.document())
    
    def setDocument(self, doc):
        print("new document")
        self.highlighter = MdHighlighter(doc)
        return QTextEdit.setDocument(self, doc)
    
    def keyPressEvent(self, event):
        """Redefines keyPress events"""
 
        self.changed.emit()
 
        # ShortCuts with CONTROL key Modifier
        if event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_S:
                self.save.emit()
                return
            elif event.key() == Qt.Key_B:
                self.build.emit()
                return
            
        return QTextEdit.keyPressEvent(self, event)

class MdEditor(QFrame):
    """
    Classdocs
    """
    
    
    def __init__(self,filename,parent=None,css_file=None):
        """
        Constructor
        """
        super(QFrame,self).__init__(parent)
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.splitter = QSplitter()
        layout.addWidget(self.splitter)
        
        self.md_editor = MdFileEditor()
        self.splitter.addWidget(self.md_editor)
        
        self.preview = QWebView()
        self.splitter.addWidget(self.preview)
        
        self.splitter.setStretchFactor(0,1)
        self.splitter.setStretchFactor(1,0)
        
        self.setFile(filename)
        
        self.update_tid = None
        self.css_file=css_file
        # connections
        self.md_editor.save.connect(self.onSaveAction)
        self.md_editor.build.connect(self.onBuildAction)
        self.md_editor.changed.connect(self.onContentChangeAction)
        
        # initial render
        self.onContentChangeAction()
        
    def __del__(self):
        self.file.close()
        
    def setFile(self,filename):
        
        self.file = QFile(filename)        
        doc = QTextDocument()
        if self.file.open(QIODevice.ReadWrite):
            doc.setPlainText(QTextStream(self.file).readAll())        
            self.md_editor.setDocument(doc)            
    
    def timerEvent(self, event):
        if event.timerId() == self.update_tid:
            self.killTimer(self.update_tid)
            self.update_tid = None
            text = self.md_editor.document().toPlainText()
            
            if self.css_file is None:
                css = None
            else:
                with open(self.css_file,'r') as f:
                    css = f.read()
                
            html=Generator.generateHTML(source=text,css=css)
            
            self.preview.page().mainFrame().setHtml(html)
    
    def onContentChangeAction(self):
        if not self.update_tid is None:
            self.killTimer(self.update_tid)
            self.update_tid = None
        self.update_tid = self.startTimer(500)
        
    def onBuildAction(self):
        
        # @todo : check file must be saved
        choice = QMessageBox.warning(self, 
            self.tr('Save file changes'), 
            self.tr('Current file has been modified, would you like to save your changes ?'),
            buttons=QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel, 
            defaultButton=QMessageBox.Yes
        )
        
        if choice == QMessageBox.Yes:
            self.onSaveAction()
        elif choice == QMessageBox.Cancel:
            return
        
        print('building')
        
        md_filename = self.filename
        Generator.generatePDF(md_filename)
        
    def onSaveAction(self):
        self.doSave()
        
    def onSaveAsAction(self):
        result = QFileDialog.getSaveFileName(
            parent=self, 
            caption=self.tr('Save as'), 
            directory=QDir.currentPath(),
            filter='Markdown files (*.md)'
        )
        if result is None:
            return
        
        filename = result[0]
        if not filename.endswith('.md'):
            filename += '.md'
        
        self.file = QFile(filename)
        self.file.open(QIODevice.ReadWrite)
        
        self.doSave()
    
    def doSave(self):
        text = self.md_editor.document().toPlainText()
        self.file.seek(0)
        self.file.write(text)
        self.file.flush()

def main():
    import sys
    
    app = QApplication(sys.argv)
    
    editor = MdEditor('../test_file.md')
    editor.showMaximized()
    
    exit(app.exec())

if __name__ == '__main__':
    main()