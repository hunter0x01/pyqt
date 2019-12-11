'''
Created on Mar 9, 2015

@author: Sylvain Garcia <garcia.6l20@gmail.com>
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MdHighlighter(QSyntaxHighlighter):
    '''
    classdocs
    '''
    class HighlightingRule(object):
        
        def __init__(self,pattern,format):
            self.patern = QRegExp(pattern)
            self.format = QTextCharFormat(format)

    def __init__(self, document):
        '''
        Constructor
        '''
        super(QSyntaxHighlighter,self).__init__(document)
        
        self.rules = []
        
        self.setupTitleHightlighting()
    
    def setupTitleHightlighting(self):
        
        ptsize = 14
        
        # header
        f = QTextCharFormat()
        color = QColor(90,60,90)
        f.setFontWeight(QFont.Bold)
        for ii in range(1,9):
            f.setFontPointSize(ptsize)
            f.setForeground(color)
            self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'^(#+){' + str(ii) + '}(.*)$'), f))
            ptsize -= 1
            color.setAlphaF(1-ii*0.05)
        
        # list
        f = QTextCharFormat()
        f.setForeground(Qt.gray)
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'^ *-.*$'), f))
        
        # emphasis        
        f = QTextCharFormat()
        f.setFontItalic(True)
        f.setForeground(Qt.gray)     
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'(\*|_)[^\*]+(\*|_)'), f))
        
        # bold
        f = QTextCharFormat()
        f.setFontWeight(QFont.Bold)
        f.setForeground(Qt.gray)
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'(\*|_){2}[^\*]+(\*|_){2}'), f))
        
        # strikeout
        f = QTextCharFormat()
        font = f.font()
        font.setStrikeOut(True)
        f.setFont(font)
        f.setForeground(Qt.gray)
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'~{2}(.*)+~{2}'), f))
        
        # hyperlink         
        f = QTextCharFormat()
        font = f.font()
        font.setUnderline(True)
        f.setFont(font)
        f.setForeground(Qt.blue)
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'\[([^\[]+)\]\(([^\)]+)\)'), f))
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'<(.*)+>'), f))
        
        # quoted
        f = QTextCharFormat()
        font = f.font()
        font.setItalic(True)
        f.setFont(font)
        f.setForeground(Qt.black)
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'\:\"(.*)\"\:'), f))
        
        # TOC
        f = QTextCharFormat()
        f.setForeground(QColor(90,60,90))
        f.setFontWeight(QFont.Bold)
        self.rules.append(MdHighlighter.HighlightingRule(QRegExp(r'\[TOC\]'), f))
        
    def highlightBlock(self, text):
        for r in self.rules:
            exp = r.patern
            index = exp.indexIn(text)
            while index >= 0:
                length = exp.matchedLength()
                self.setFormat(index, length, r.format)
                index = exp.indexIn(text,index+length)
            
