import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QSlider, QDial
from PyQt5.QtWidgets import QDesktopWidget, QGridLayout, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QCheckBox, QMessageBox, QRadioButton, QComboBox, QProgressBar
from PyQt5.QtWidgets import QFrame, QSplitter, QGroupBox, QMenu, QTabWidget,QTextBrowser
from PyQt5.QtWidgets import QDialogButtonBox, QCalendarWidget, QSpinBox, QDoubleSpinBox
from PyQt5.QtWidgets import QDateEdit, QTimeEdit, QDateTimeEdit, QInputDialog, QColorDialog, QGraphicsView, QGraphicsScene
from PyQt5.QtWidgets import QSizePolicy, QFontDialog, QFileDialog, QLCDNumber, QDockWidget, QTreeWidget, QGraphicsItem
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime, QPointF, QRectF
from PyQt5.QtWidgets import QTreeWidgetItem, QStackedWidget, QTableView, QToolBar
from PyQt5.QtCore import QBasicTimer, pyqtSignal, QObject, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPainter, QBrush, QPen, QPolygonF, QWheelEvent
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import requests
from bs4 import BeautifulSoup
import random


# import mysql3.pyw 

# tutorial
# http://codetorial.net/widget/qpixmap.html  

# good  
# https://freeprog.tistory.com/category/PyQt5  


# dock
# https://www.programcreek.com/python/example/81314/PyQt5.QtWidgets.QWidget


# pyqt DB
# https://blog.dork94.com/179?category=735145


# pyqt Dockable 
# https://programtalk.com/python-examples/PyQt5.QtCore.Qt.ActionsContextMenu/


# pyqt QtreeWidget 
# https://impatientprogrammer.net/2018/10/05/pyside-pyqt-qtreewidget-in-4-minutes/

# Ocean Coding , Chat Server, Client
# https://oceancoding.blogspot.com/2019/05/blog-post_23.html

# QGraphics 
# https://www.oipapio.com/question-1800996

# QListView to QGraphicView
# https://stackoverflow.com/questions/55776728/how-can-i-add-pictures-from-qlistview-to-qgraphicsview-with-drag-drop


# pip3 install QScintilla

# Custom Title Bar
# https://www.manongdao.com/article-383594.html

# pyqt tutorial

# pip3 install python-ctags3

#  pip3 install PyQtWebEngine

class Communicate(QObject):
    closeApp = pyqtSignal()

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 
        # cb = QCheckBox('Show Title', self)
        # cb.move(20, 20)
        # cb.toggle()
        # cb.stateChanged.connect(self.changeTitle)

        # -- radio button
        # rbtn1 = QRadioButton('First Button', self)
        # rbtn1.move(100,100)
        # rbtn1.setChecked(True)
        # rbtn1.clicked.connect(self.changeTitle)

        # rbtn2 = QRadioButton(self)
        # rbtn2.move(100, 200)
        # rbtn2.setText('Second Button')
        # rbtn2.clicked.connect(self.changeTitle)


        # -- combobox
        # self.lbl = QLabel('Option1', self)
        # self.lbl.move(50, 150)

        # cb = QComboBox(self)
        # cb.addItem('Option1')
        # cb.addItem('Option2')
        # cb.addItem('Option3')
        # cb.addItem('Option4')
        # cb.move(60,250)
        # cb.adjustSize()

        # cb.activated[str].connect(self.onActivated)

        # -- LineEdit
        # self.lbl01 = QLabel(self)
        # self.lbl01.move(200,300)

        # qle = QLineEdit(self)
        # qle.move(200, 320)
        # qle.textChanged[str].connect(self.onChanged)

        # -- Progress
        # self.pbar = QProgressBar(self)
        # self.pbar.setGeometry(30, 40, 200, 25)

        # self.btn11 = QPushButton('Start', self)
        # self.btn11.move(40, 80)
        # self.btn11.clicked.connect(self.doAction)

        # self.timer = QBasicTimer()
        # self.step = 0


        # -- slider, dial

        # self.slider = QSlider(Qt.Horizontal, self)
        # self.slider.move(30, 30)
        # self.slider.setRange(0, 50)
        # self.slider.setSingleStep(2)
        
        # self.dial = QDial(self)
        # self.dial.move(30,50)
        # self.dial.setRange(0, 50)

        # btn21 = QPushButton('Default', self)
        # btn21.move(35, 160)


        # self.slider.valueChanged.connect(self.dial.setValue)
        # self.dial.valueChanged.connect(self.slider.setValue)
        # self.dial.setNotchesVisible(True)
        # btn21.clicked.connect(self.button_clicked)

        # -- Splitter 
        # hbox01 = QHBoxLayout()

        # top = QFrame()
        # top.setFrameShape(QFrame.Box)

        # midleft = QFrame()
        # midleft.setFrameShape(QFrame.StyledPanel)

        # midright = QFrame()
        # midright.setFrameShape(QFrame.Panel)

        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.WinPanel)
        # bottom.setFrameShadow(QFrame.Sunken)

        # splitter1 = QSplitter(Qt.Horizontal)
        # splitter1.addWidget(midleft)
        # splitter1.addWidget(midright)

        # splitter2 = QSplitter(Qt.Vertical)
        # splitter2.addWidget(top)
        # splitter2.addWidget(splitter1)
        # splitter2.addWidget(bottom)

        # hbox01.addWidget(splitter2)
        # self.setLayout(hbox01)
        # -- splitter end


        # -- QGroupBox 

        # grid = QGridLayout()
        # grid.addWidget(self.createFirstExclusiveGroup(),0,0)
        # grid.addWidget(self.createSecondExclusiveGroup(),1,0)
        # grid.addWidget(self.createNonExclusiveGroup(),0,1)
        # grid.addWidget(self.createPushButtonGroup(),1,1)

        # self.setLayout(grid)

        # -- QGroupBox


        # -- QTabWidget

        # tab1 = QWidget()
        # tab2 = QWidget()

        # tabs = QTabWidget()
        # tabs.addTab(tab1, 'Tab1')
        # tabs.addTab(tab2, 'Tab2')

        # vbox = QVBoxLayout()
        # vbox.addWidget(tabs)

        # self.setLayout(vbox)
        # -- QTabWidget

        # -- QTabWidget Advanced

        # tabs = QTabWidget()
        # tabs.addTab(self.FirstTab(), 'First')
        # tabs.addTab(self.SecondTab(), 'Second')
        # tabs.addTab(self.ThirdTab(), 'Third')

        # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # # buttonbox.accepted.connect(self.accept)
        # # buttonbox.rejected.connect(self.reject)

        # vbox = QVBoxLayout()
        # vbox.addWidget(tabs)
        # vbox.addWidget(buttonbox)
        # self.setLayout(vbox)

        # -- QTabWidget Advanced


        # --  QPixmap

        # pixmap = QPixmap('exit.png')

        # lbl_img = QLabel()
        # lbl_img.setPixmap(pixmap)
        # lbl_size = QLabel('Width: '+str(pixmap.width())+',Height: '+str(pixmap.height()))
        # lbl_size.setAlignment(Qt.AlignCenter)

        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl_img)
        # vbox.addWidget(lbl_size)

        # self.setLayout(vbox)

        # --- QPixmap

        # -- QCalendar

        # cal = QCalendarWidget(self)
        # cal.setGridVisible(True)
        # cal.clicked[QDate].connect(self.showDate)

        # self.lbl = QLabel(self)
        # date = cal.selectedDate()
        # self.lbl.setText(date.toString())

        # vbox = QVBoxLayout()
        # vbox.addWidget(cal)
        # vbox.addWidget(self.lbl)

        # self.setLayout(vbox)

        # -- QCalendar

        # -- SpinBox
        # self.lbl1 = QLabel('QSpinBox')
        # self.spinbox = QSpinBox()
        # self.spinbox.setMinimum(-10)
        # self.spinbox.setMaximum(30)
        # self.spinbox.setSingleStep(2)
        # self.lbl2 = QLabel('0')

        # self.spinbox.valueChanged.connect(self.value_changed)

        # vbox = QVBoxLayout()
        # vbox.addWidget(self.lbl1)
        # vbox.addWidget(self.spinbox)
        # vbox.addWidget(self.lbl2)
        # vbox.addStretch()

        # self.setLayout(vbox)

        # -- SpinBox

        # -- QDoubleSpinBox

        # self.lbl1 = QLabel('QDoubleSpinBox')
        # self.dspinbox = QDoubleSpinBox()
        # self.dspinbox.setRange(0,100)
        # self.dspinbox.setSingleStep(0.5)
        # self.dspinbox.setPrefix('$ ')
        # self.dspinbox.setDecimals(1)
        # self.lbl2 = QLabel('$ 0.0')

        # self.dspinbox.valueChanged.connect(self.value_changed)

        # vbox = QVBoxLayout()
        # vbox.addWidget(self.lbl1)
        # vbox.addWidget(self.dspinbox)
        # vbox.addWidget(self.lbl2)
        # vbox.addStretch()

        # self.setLayout(vbox)

        # -- QDoubleSpinBox



        # -- QDateEdit

        # lbl = QLabel('QDateEdit')

        # dateedit = QDateEdit(self)
        # dateedit.setDate(QDate.currentDate())
        # dateedit.setMinimumDate(QDate(1990,1,1))
        # dateedit.setMaximumDate(QDate(2100,12,31))

        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl)
        # vbox.addWidget(dateedit)
        # vbox.addStretch()

        # self.setLayout(vbox)


        # -- QDateEdit


        # -- QTimeEdit

        # lbl = QLabel('QTimeEdit')

        # timeedit = QTimeEdit(self)
        # timeedit.setTime(QTime.currentTime())
        # timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        # timeedit.setDisplayFormat('hh:mm:ss')

        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl)
        # vbox.addWidget(timeedit)
        # vbox.addStretch()

        # self.setLayout(vbox)

        # -- QTimeEdit


        # -- QDateTimeEdit

        # lbl = QLabel('QTimeEdit')

        # datetimeedit = QDateTimeEdit(self)
        # datetimeedit.setDateTime(QDateTime.currentDateTime())
        # datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        # datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl)
        # vbox.addWidget(datetimeedit)
        # vbox.addStretch()

        # self.setLayout(vbox)

        # -- QDateTimeEdit


        # -- QTextBrowser

        # self.le = QLineEdit()
        # self.le.returnPressed.connect(self.append_text)

        # self.tb = QTextBrowser()
        # self.tb.setAcceptRichText(True)
        # self.tb.setOpenExternalLinks(True)

        # self.clear_btn = QPushButton('Clear')
        # self.clear_btn.pressed.connect(self.clear_text)

        # vbox = QVBoxLayout()
        # vbox.addWidget(self.le, 0)
        # vbox.addWidget(self.tb, 1)
        # vbox.addWidget(self.clear_btn, 2)

        # self.setLayout(vbox)



        # -- QTextBrowser

        # -- QTextBrowser Advanced

        # self.le = QLineEdit()
        # self.le.setPlaceholderText('yymmdd')
        # self.le.returnPressed.connect(self.crawl_news)

        # self.btn = QPushButton('Start')
        # self.btn.clicked.connect(self.crawl_news)

        # self.lbl = QLabel('Please Input Date')

        # self.tb = QTextBrowser()
        # self.tb.setAcceptRichText(True)
        # self.tb.setOpenExternalLinks(True)

        # grid = QGridLayout()
        # grid.addWidget(self.le, 0, 0, 1, 3)
        # grid.addWidget(self.btn, 0, 3, 1, 1)
        # grid.addWidget(self.lbl, 1, 0, 1, 4)
        # grid.addWidget(self.tb, 2, 0, 1, 4)

        # self.setLayout(grid)

        # -- QTextBrowser Advanced

        # -- QTextEdit

        # self.lbl1 = QLabel('Enter your sentence:')
        # self.te = QTextEdit()
        # self.te.setAcceptRichText(False)
        # self.lbl2 = QLabel('The number of words is 0')

        # self.te.textChanged.connect(self.text_changed)

        # vbox = QVBoxLayout()
        # vbox.addWidget(self.lbl1)
        # vbox.addWidget(self.te)
        # vbox.addWidget(self.lbl2)
        # vbox.addStretch()

        # self.setLayout(vbox)
        # -- QTextEdit

        # -- QInputDialog

        # self.btn = QPushButton('Dialog', self)
        # self.btn.move(30, 30)
        # self.btn.clicked.connect(self.showDialog)

        # self.le = QLineEdit(self)
        # self.le.move(120, 35)

        # -- QInputDialog

        # -- QColorDialog

        # col = QColor(0, 0, 0)
        # self.btn = QPushButton('Dialog', self)
        # self.btn.move(30, 30)
        # self.btn.clicked.connect(self.showDialog3)

        # self.frm = QFrame(self)
        # self.frm.setStyleSheet('QWidget { background-color: %s}' % col.name())
        # self.frm.setGeometry(130, 35, 100, 100)
        # -- QColorDialog

        # -- QFontDialog

        # btn = QPushButton('Dialog', self)
        # btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # btn.move(20, 20)
        # btn.clicked.connect(self.showDialog3)

        # vbox = QVBoxLayout()
        # vbox.addWidget(btn)

        # self.lbl = QLabel('The quick brown fox jumps over the lazy dog', self)
        # self.lbl.move(130, 20)

        # vbox.addWidget(self.lbl)
        # self.setLayout(vbox)

        # -- QFontDialog


        # -- QFileDialog

        # 아래 메인에 구현 

        # -- QFileDialog


        # --  QMessageBox

        # 아래 메인 참고 
        # 종료시 이벤트를 받을려고 아래 메인에 구현 함.

        # --  QMessageBox


        # 이벤트 핸들러 만들기 1

        # self.lcd = QLCDNumber(self)
        # self.dial = QDial(self)
        # self.btn1 = QPushButton('Big', self)
        # self.btn2 = QPushButton('Small', self)


        # self.hbox = QHBoxLayout()
        # self.hbox.addWidget(self.btn1)
        # self.hbox.addWidget(self.btn2)

        # self.vbox = QVBoxLayout()
        # self.vbox.addWidget(self.lcd)
        # self.vbox.addWidget(self.dial)
        # self.vbox.addLayout(self.hbox)
        # self.setLayout(self.vbox)

        # self.dial.valueChanged.connect(self.lcd.display)
        # self.btn1.clicked.connect(self.Setvalue_10)
        # self.btn2.clicked.connect(self.SetValue_100)

        # 이벤트 핸들러 만들기 1

        # 이벤트 핸들러 재구성하기 (미동작)

        # def keyPressEvent(self, e):

        #     if e.key() == Qt.Key_Escape:
        #         self.close()
        #     elif e.key() == Qt.Key_F:
        #         self.showFullScreen()
        #     elif e.key() == Qt.Key_N:
        #         self.showNormal()


        # 이벤트 핸들러 재구성하기 

        # 이벤트 핸들러 재구성하기 2 
            
        # x = 0
        # y = 0

        # self.text = 'x: {0}, y:{1}'.format(x,y)
        # self.label = QLabel(self.text, self)
        # self.label.move(20, 20)

        # self.setMouseTracking(True)

        # 이벤트 핸들러 재구성하기 2 

        # 사용자 정의 시그널 (미동작)

        # self.c = Communicate()
        # self.c.closeApp.connect(self.close)


        # 사용자 정의 시그널



        self.setGeometry(300, 100, 350, 150)  # x, y, width, height
        self.setWindowTitle("QWidget")
        self.show()

    # 미동작
    # def mousePressEvent(self, e):
    #     self.c.closeApp.emit()

    # def mouseMoveEvent(self, e):
    #     x = e.x()
    #     y = e.y()

    #     text = 'x: {0}, y: {1}'.format(x, y)
    #     self.label.setText(text)
    #     self.label.adjustSize()

    # 수정필요

    # def Setvalue_10(self):
    #     self.lcd.display.setValue(0)
    

    # def SetValue_100(self):
    #     self.lcd.display.setValue(99)

    def showDialog3(self):

        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)

    def showDialog2(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget {background-color: %s }' % col.name())

    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


        # -- QInputDialog



    def text_changed(self):

        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))

    def crawl_news(self):
        date = self.le.text()

        if date:
            self.lbl.setText('[20' + str(date) + '] Many Read News')
            self.tb.clear()

            url_news = 'https://news.naver.com'
            url = url_news + '/main/ranking/popularDay.nhn?rankingType=popular_day&date20' + date
            r = requests.get(url)
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            titles_html = soup.select('.ranking_section > ol > li > dl > dt > a')

            for i in range(len(titles_html)):
                title = titles_html[i].text
                link = url_news + titles_html[i].get('href')
                self.tb.append(str(i+1) + '. ' + title + ' (' + '<a href="' + link + '">링크</a>' + ')')

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()

    def value_changed(self):
        self.lbl2.setText('$ '+str(self.dspinbox.value()))

    # def value_changed(self):
    #     self.lbl2.setText(str(self.dspinbox.value()))

    # def value_changed(self):
    #     self.lbl2.setText(str(self.spinbox.value()))

    def showDate(self, date):
        self.lbl.setText(date.toString())

    class FirstTab(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            name = QLabel('Name:')
            nameedit = QLineEdit()
            age = QLabel('Age:')
            ageedit = QLineEdit()
            nation = QLabel('Nation:')
            nationedit = QLineEdit()

            vbox = QVBoxLayout()
            vbox.addWidget(name)
            vbox.addWidget(nameedit)
            vbox.addWidget(age)
            vbox.addWidget(ageedit)
            vbox.addWidget(nation)
            vbox.addWidget(nationedit)
            vbox.addStretch()

            self.setLayout(vbox)

    class SecondTab(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):

            lan_group = QGroupBox('Select Your Language')
            combo = QComboBox()
            list = ['Korean', 'English', 'Chinese']
            combo.addItems(list)

            vbox1 = QVBoxLayout()
            vbox1.addWidget(combo)
            lan_group.setLayout(vbox1)

            learn_group = QGroupBox('Select What You Want To Learn')
            korean = QCheckBox('Korean')
            english = QCheckBox('English')
            chinese = QCheckBox('Chinese')

            vbox2 = QVBoxLayout()
            vbox2.addWidget(korean)
            vbox2.addWidget(english)
            vbox2.addWidget(chinese)
            learn_group.setLayout(vbox2)

            vbox = QVBoxLayout()
            vbox.addWidget(lan_group)
            vbox.addWidget(learn_group)
            self.setLayout(vbox)

    class ThirdTab(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):

            lbl = QLabel('Terms and Conditions')
            text_browser = QTextBrowser()
            text_browser.setText('This is the terms and conditions')
            checkbox = QCheckBox('Check the terms and conditions')

            vbox = QVBoxLayout()
            vbox.addWidget(lbl)
            vbox.addWidget(text_browser)
            vbox.addWidget(checkbox)

            self.setLayout(vbox)

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)

        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Button')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('Normal Button')

        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)

        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)

        popupbutton = QPushButton('Popup Button')

        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox




    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)



    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn11.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self, e ):
        if self.timer.isActive():
            self.timer.stop()
            self.btn11.setText('Stop')
        else:
            self.timer.start(100, self)
            self.btn11.setText('Start')

    def onChanged(self, text):
        self.lbl01.setText(text)
        self.lbl01.adjustSize()


    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def changeTitle(self, state):

        if state == Qt.Checked:
            reply = QMessageBox.question(self, 'Message', 'Check Box Yes')

        else:
            reply = QMessageBox.question(self, 'Message', 'Check Box No')


        if reply == QMessageBox.Yes:
            QMessageBox.question(self, 'Message', 'Accepted')
            # event.accept()
        else:
            QMessageBox.question(self, 'Message', 'Ignored')
            # event.ignore()

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        # QMainWindows  경우 자체 레이아웃을 갖고 있기 때문에 
        # CentralWidget을 생성해주어야 함.

        mw = MainWidget()
        self.setCentralWidget(mw)

        # 상태바에 뛰울 
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        """
        self.setWindowTitle('Shape')
        self.setWindowIcon(QIcon(":/images/qt.png"))

        self.shapeWidget = ShapeWidget()
        self.setCentralWidget(self.shapeWidget)

        self.createActions();
        self.createMenus();
        self.createContextMenu();
        self.createToolBar();
        self.createStatusBar();
        self.readSettings();

        """

        # -- Windows Title Bar --
        self.setWindowTitle('Security-HQ') # 윈도우 타이틀 

        # -- Status Bar --
        self.statusBar().showMessage('Ready') #상태바 인스턴스 생성 및 표시 
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # 현재 날짜 표시


        # -- Menu Bar --
        # 메뉴바 엑션 설정 및 메뉴 명칭, 단축, 
        # 종료 action
        exitAction = QAction(QIcon('exit.png'), 'Exit', self) # 아이콘표시, Exit 표시
        exitAction.setShortcut('Ctrl+Q') # 단축키 
        exitAction.setStatusTip('Exit Application') # 상태바 표시
        exitAction.triggered.connect(qApp.quit) # 어플리케이션 종료설정 QApplication quit()

        # 종료 action
        saveAction = QAction(QIcon('save.png'), 'Save', self) # 아이콘표시, Exit 표시
        saveAction.setShortcut('Ctrl+S') # 단축키 
        saveAction.setStatusTip('Save Application') # 상태바 표시
        saveAction.triggered.connect(self.showDialog4) # 

        # 종료 action
        editAction = QAction(QIcon('edit.png'), 'Edit', self) # 아이콘표시, Exit 표시
        editAction.setShortcut('Ctrl+E') # 단축키 
        editAction.setStatusTip('Edit Application') # 상태바 표시
        editAction.triggered.connect(qApp.quit) # 어플리케이션 종료설정 QApplication quit()

        # 종료 action
        printAction = QAction(QIcon('print.png'), 'Print', self) # 아이콘표시, Exit 표시
        printAction.setShortcut('Ctrl+P') # 단축키 
        printAction.setStatusTip('Print Application') # 상태바 표시
        printAction.triggered.connect(qApp.quit) # 어플리케이션 종료설정 QApplication quit()

        menubar = self.menuBar() # 메뉴 인스턴스 생성 
        menubar.setNativeMenuBar(False) # Mac 에서도 윈도우와 동일한 결과 나오게 하기위해 

        # -- 파일메뉴 최초
        fileMenu = menubar.addMenu('&파일') # 메뉴 인스턴스에 실제 메뉴 추가 
        # -- 편집메뉴 최초 
        editMenu = menubar.addMenu('&편집') # 메뉴 인스턴스에 실제 메뉴 추가 

        # -- 파일메뉴 하위
        fileMenu.addAction(saveAction) # 정의된 하위 메뉴 추가 
        fileMenu.addAction(printAction) # 정의된 하위 메뉴 추가 
        fileMenu.addAction(exitAction) # 정의된 하위 메뉴 추가 

        # -- 편집메뉴 하위 
        editMenu.addAction(editAction)

        # -- Tool Bar --
        # 파일 툴바
        self.fileToolbar = self.addToolBar('Exit')
        self.fileToolbar.addAction(exitAction)
        self.fileToolbar.addAction(saveAction)
        self.fileToolbar.addAction(printAction)

        #편집 툴바 
        self.editToolbar = self.addToolBar('Edit')
        self.editToolbar.addAction(editAction)


        self.combo = QComboBox(self)
        self.combo.addItem("Item 1")
        self.combo.addItem("Item 2")
        self.combo.addItem("Item 3")
        self.combo.currentIndexChanged.connect(self.setSomething)
        self.fileToolbar.addWidget(self.combo)
        self.combo.setMinimumSize(self.combo.sizeHint().width(),self.fileToolbar.iconSize().height())
        self.fileToolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)

        # 윈도우 구성요소 스타일 꾸미기 

        # 메인 위젯을 텍스트형태로 변경 !!!!!
        # self.textEdit = QTextEdit()
        # self.setCentralWidget(self.textEdit)

    # def keyPressEvent(self, e):

    #     if e.key() == Qt.Key_Escape:
    #         self.close()
    #     elif e.key() == Qt.Key_F:
    #         self.showFullScreen()
    #     elif e.key() == Qt.Key_N:
    #         self.showNormal()



        # -- QTabWidget

        # tab1 = QWidget()
        # tab2 = QWidget()

        # tabs = QTabWidget()
        # tabs.addTab(tab1, 'Tab1')
        # tabs.addTab(tab2, 'Tab2')

        # vbox = QVBoxLayout()
        # vbox.addWidget(tabs)



        # -- QTabWidget



        dockWidgetLeft    = QWidget()
        dockWidgetRight   = QWidget()
        dockWidgetBottom  = QWidget()
        dockWidgetTree    = QTreeWidget()


        # self.shapesDockWidget = QDockWidget("Shapes")
        # self.shapesDockWidget.setObjectName("shapesDockWidget");
        # self.shapesDockWidget.setWidget(dockWidgetTree)

        # self.shapesDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        # self.shapesDockWidget.setFloating(True)
        # self.shapesDockWidget.widget().setMinimumSize(QSize(90,150))
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.shapesDockWidget);



        self.dockWidget = QDockWidget("메뉴")
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.treeWidget = QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setObjectName("verticalLayout")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.treeWidget.setAlternatingRowColors(True)
        for i in range(3):
            parent = QTreeWidgetItem(self.treeWidget)
            parent.setText(0, "Parent {}".format(i))
            # parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            parent.setFlags(parent.flags() )
            for x in range(5):
                child = QTreeWidgetItem(parent)

                # child.setFlags(child.flags() | Qt.ItemIsUserCheckable)   
                child.setFlags(child.flags() )             
                child.setText(0, "Child {}".format(x))
                # child.setCheckState(0, Qt.Unchecked)
        self.treeWidget.itemClicked.connect(self.login)

        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.treeWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)


        self.dockingWidgetLeft = QDockWidget("Icon panel") # 타이틀 설정
        self.dockingWidgetLeft.setObjectName("IconPanel")
        self.dockingWidgetLeft.setWidget(dockWidgetLeft) # 래핑할 위젯 설정
        self.dockingWidgetLeft.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockingWidgetLeft.setFloating(True)
        self.dockingWidgetLeft.widget().setMinimumSize(QSize(80,150))
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dockingWidgetLeft) # 초기 위치 및 도킹위젯을 메인윈도의 
                                                            

        self.dockingWidgetRight = QDockWidget("속성 창") # 타이틀 설정
        self.dockingWidgetRight.setObjectName("IconPanel")
        self.dockingWidgetRight.setWidget(dockWidgetRight) # 래핑할 위젯 설정
        self.dockingWidgetRight.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockingWidgetRight.setFloating(True)
        self.dockingWidgetRight.widget().setMinimumSize(QSize(200,200))
        self.addDockWidget(Qt.RightDockWidgetArea,self.dockingWidgetRight) # 초기 위치 및 도킹위젯을 메인윈도의 


        self.dockingWidgetBottom = QDockWidget("알람 콘솔") # 타이틀 설정
        self.dockingWidgetBottom.setObjectName("IconPanel")
        self.dockingWidgetBottom.setWidget(dockWidgetBottom) # 래핑할 위젯 설정
        self.dockingWidgetBottom.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.dockingWidgetBottom.setFloating(True)
        self.dockingWidgetBottom.widget().setMinimumSize(QSize(80,60))
        self.addDockWidget(Qt.BottomDockWidgetArea,self.dockingWidgetBottom) # 초기 위치 및 도킹위젯을 메인윈도의 




        # self.cg = QTreeWidgetItem(self.treeWidget, ['carrots', '0.99'])
        # self.cg.setCheckState(0, Qt.Checked)

        # self.c1 = QTreeWidgetItem(self.cg, ['carrot1', '0.33'])
        # self.h1 = QTreeWidgetItem(self.cg, ['carrot2', '0.33'])
        # self.h1.setDisabled(True)

        # self.treeWidget.expandAll()
        # self.treeWidget.itemClicked.connect(self.onItemClicked)
        # self.treeWidget.addTopLevelItem(self.h1)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        Dashboard = DashBoardWidget(self)
        # Dashboard.button.clicked.connect(self.login2)

        
        self.central_widget.addWidget(Dashboard)


        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("/Users/steve/security-hq.db")

        if db.open():
            print("Open Db Success")


 



        # self.setDockOptions(self.AnimatedDocks | self.AllowNestedDocks)
        self.statusBar()

        # 파일열기 

        # openFile = QAction(QIcon('open.png'), 'Open', self)
        # openFile.setShortcut('Ctrl+O')
        # openFile.setStatusTip('Open New File')
        # openFile.triggered.connect(self.showDialog4)


        # 윈도우 표시 정의
        self.setGeometry(0, 0, 1024, 768) # 윈도우 위치 및 크기 
        self.center() #위도우 위치를 중앙에 이동시킴
        self.show() #보여줌 


    def doit(self):
        print("Opening a new popup window...")
        self.w = MyPopup()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()
        # w.exec_()

    def createDB(self):
        query = QSqlQuery()
        query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")
        query.exec_("insert into person values(1, 'Bauer', 'Beijing')")
        query.exec_("insert into person values(2, 'Jack', 'shanghai')")
        query.exec_("insert into person values(3, 'Alex', 'chengdu')")
        print("DB Insert")

    def login(self):
        logged_in_widget = LoggedWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)

    def login2(self):
        log_in_widget = LoginWidget(self)
        self.central_widget.addWidget(log_in_widget)
        self.central_widget.setCurrentWidget(log_in_widget)


    def onItemClicked(self, it, col):
        print(it, col, it.text(col))
        QMessageBox.question(self,'Message', it.text(col), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def setSomething(self):
        print("gogo")

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.parent().db.close() # DB 종료 
            print("Db Close")
            event.accept()

        else:
            event.ignore()


    def showDialog4(self):

        fname = QFileDialog.getOpenFileName(self, 'Open File', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def center(self): # 중앙에 윈도우를 위치시키는 메소드 
        qr = self.frameGeometry() # 창의 위치 정보와 크기정보를 가지고 옴
        cp = QDesktopWidget().availableGeometry().center() # 사용 모니터 가운데 위치 파악 
        qr.moveCenter(cp) # 현재 창을 화면 중심으로 직각사각형 위치로 이동 , 화면중심, 창중심 일치시킴 
        self.move(qr.topLeft())

class DashBoardWidget(QWidget):
    def __init__(self, parent=None):
        super(DashBoardWidget, self).__init__(parent)

        layout = QHBoxLayout()

        self.button1 = QPushButton('Btn1')

        self.button1.clicked.connect(self.parent().doit)
        # self.button2 = QPushButton('Btn2')
        # self.button3 = QPushButton('Btn3')
        # self.button4 = QPushButton('Btn4')
        # self.button5 = QPushButton('Btn5')
        # self.button6 = QPushButton('Btn6')
        # self.button7 = QPushButton('Btn7')
        # self.button8 = QPushButton('Btn8')
        # self.button9 = QPushButton('Btn9')
        # self.btn_createdb = QPushButton('CreateDB')
        # self.btn_createdb.clicked.connect(self.parent().createDB)
        # layout.addWidget(self.button)
        # layout.addWidget(self.btn_createdb)
        # self.setLayout(layout)


        # exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(qApp.quit)

        # toolbar2 = QToolBar()
        # toolbar2.addAction(exitAction)
        # toolbar2.setStyleSheet("QToolBar {border: 1px solid blue }")
        # layout.addWidget(toolbar2)


        vlayout = QVBoxLayout()
        # vlayout.addWidget(self.button1)
        # vlayout.addWidget(self.button2)
        # vlayout.addWidget(self.button3)
        # vlayout.addWidget(self.button4)
        # vlayout.addWidget(self.button5)
        # vlayout.addWidget(self.button6)
        # vlayout.addWidget(self.button7)
        # vlayout.addWidget(self.button8)
        # vlayout.addWidget(self.button9)
        # vlayout.setMenuBar(toolbar2)
        vlayout.setContentsMargins(0,0,0,0)


        self.gv = MyGraphicsView()
        self.gv.setScene(MyGraphicsScene(self))
        # self.setCentralWidget(self.gv)
        # layout.addWidget(self.toolbar)
        layout.addLayout(vlayout)
        layout.addWidget(self.button1)
        layout.addWidget(self.gv)
        self.setLayout(layout)

        self.gv.scene().selectionChanged.connect(self.selection_changed)
        self.populate()


    def populate(self):
        scene = self.gv.scene()

        for i in range(300):
            x = random.randint(-1000, 1000)
            y = random.randint(-1000, 1000)
            r = random.randint(1, 50)
            rect = scene.addEllipse(x, y, r, r, 
                QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), 
                QBrush(QColor(255,128,20,128)))
            rect.setFlag( QGraphicsItem.ItemIsSelectable )
            rect.setFlag( QGraphicsItem.ItemIsMovable )

        rect = scene.addEllipse(10, 20, 20, 20, 
            QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), 
            QBrush(QColor(255,0,0,128)))
        rect.setFlag( QGraphicsItem.ItemIsSelectable )
        rect.setFlag( QGraphicsItem.ItemIsMovable )

        # points = QPolygonF()
        # points.append(QPointF(10.4, 10.5))
        # points.append(QPointF(40.2, 60.2))
        # points.append(QPointF(30.2, 90.2))
        # points.append(QPointF(10.2, 80.2))
        # poly = scene.addPolygon(points, 
        #     QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), 
        #     QBrush(QColor(255,0,0,128)))
        # poly.setFlag( QGraphicsItem.ItemIsSelectable )
        # poly.setFlag( QGraphicsItem.ItemIsMovable )


    def selection_changed(self):

        selection = self.gv.scene().selectedItems()
        print('Selected:', len(selection))
        print("")
        for i in selection:
            i.setPen(QPen(QColor(255,255,255), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))



class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.button = QPushButton('Login')


        self.model = QSqlTableModel()
        self.initializedModel()

        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        self.layout = QVBoxLayout()
        addButton = QPushButton("Add")
        deleteButton = QPushButton("Delete")

        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(addButton)
        self.hLayout.addWidget(deleteButton)

        layout.addWidget(self.tableView)
        layout.addLayout(self.hLayout)

        self.setLayout(layout)
        self.button.clicked.connect(self.parent().login)

        addButton.clicked.connect(self.onAddRow)
        deleteButton.clicked.connect(self.onDeleteRow)

    def onAddRow(self):
        self.model.insertRows(self.model.rowCount(),1)
        self.model.submit()

    def onDeleteRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.submit()
        self.model.select()

    def initializedModel(self):
        self.model.setTable("person")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Address")


    def sizeHint(self):
        return QSize(150, 75)

        # you might want to do self.button.click.connect(self.parent().login) here





class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super(MyGraphicsView, self).__init__()
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self._isPanning = False
        self._mousePressed = False
        # self.setBackgroundBrush(QImage("C:/Users/jmartini/Desktop/Temp/images/flag_0140.jpg"))
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setHorizontalScrollBarPolicy( Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy( Qt.ScrollBarAlwaysOff )


    def mousePressEvent(self,  event):
        if event.button() == Qt.LeftButton:
            self._mousePressed = True
            if self._isPanning:
                self.setCursor(Qt.ClosedHandCursor)
                self._dragPos = event.pos()
                event.accept()
            else:
                super(MyGraphicsView, self).mousePressEvent(event)
        elif event.button() == Qt.MiddleButton:
            self._mousePressed = True
            self._isPanning = True
            self.setCursor(Qt.ClosedHandCursor)
            self._dragPos = event.pos()
            event.accept()


    def mouseMoveEvent(self, event):
        if self._mousePressed and self._isPanning:
            newPos = event.pos()
            diff = newPos - self._dragPos
            self._dragPos = newPos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - diff.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - diff.y())
            event.accept()
        else:
            super(MyGraphicsView, self).mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self._isPanning:
                self.setCursor(Qt.OpenHandCursor)
            else:
                self._isPanning = False
                self.setCursor(Qt.ArrowCursor)
            self._mousePressed = False
        elif event.button() == Qt.MiddleButton:
            self._isPanning = False
            self.setCursor(Qt.ArrowCursor)
            self._mousePressed = False
        super(MyGraphicsView, self).mouseReleaseEvent(event)


    def mouseDoubleClickEvent(self, event): 
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        pass


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space and not self._mousePressed:
            self._isPanning = True
            self.setCursor(Qt.OpenHandCursor)
        else:
            super(MyGraphicsView, self).keyPressEvent(event)


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Space:
            if not self._mousePressed:
                self._isPanning = False
                self.setCursor(Qt.ArrowCursor)
        else:
            super(MyGraphicsView, self).keyPressEvent(event)


    def wheelEvent(self,  event):
        # zoom factor
        factor = 1.25

        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor
        self.scale(factor, factor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())


class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)



class MyGraphicsScene(QGraphicsScene):
    def __init__(self,  parent):
        super(MyGraphicsScene,  self).__init__()
        self.setBackgroundBrush(QBrush(QColor(50,50,50)))
        #self.setSceneRect(50,50,0,0)





class LoggedWidget(QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel('logged in!')
        self.button01 = QPushButton("Click Here")
        layout.addWidget(self.label)
        layout.addWidget(self.button01)
        self.setLayout(layout)
        self.button01.clicked.connect(self.parent().login2)



"""
        self.setCentralWidget(QTextEdit())

        self.docked = QDockWidget("Dockable", self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.docked)
        self.dockedWidget = QWidget(self)
        self.docked.setWidget(self.dockedWidget)
        self.setWindowTitle("Dock demo")
        self.dockedWidget.setLayout(QVBoxLayout())
        for i in range(5):
            self.dockedWidget.layout().addWidget(QPushButton("{}".format(i)))
"""

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


        # 현재 날짜 출력 (console)
        # now = QDate.currentDate()
        # print(now.toString()) # 목 9월 12 2019

        # print(now.toString('d.M.yy')) # 12.9.19
        # print(now.toString('dd.MM.yyyy')) # 12.09.2019
        # print(now.toString('ddd.MMMM.yyyy')) # 목.9월.2019
        # print(now.toString(Qt.ISODate)) # 2019-09-12
        # print(now.toString(Qt.DefaultLocaleLongDate)) # 2019년 9월 12일

        # 현재 시간 출력 (console)
        # time = QTime.currentTime()
        # print(time.toString()) # 22:52:07

        # print(time.toString('h.m.s')) # 22.52.7
        # print(time.toString('hh.mm.ss')) #  22.52.07
        # print(time.toString('hh.mm.ss.zzz')) # 22.52.07.863
        # print(time.toString(Qt.DefaultLocaleLongDate)) # 오후 10시 52분 7초 GMT+9
        # print(time.toString(Qt.DefaultLocaleShortDate)) # 오후 10:52

        # 현재 날짜와 시간 출력 (console)
        #datetime = QDateTime.currentDateTime()
        #print(datetime.toString('d.M.yy hh:mm:ss')) # 12.9.19 22:55:26
        #print(datetime.toString('dd.MM.yyyy hh:mm:ss')) # 12.09.2019 22:55:26
        #print(datetime.toString(Qt.DefaultLocaleLongDate)) # 2019년 9월 12일 오후 10시 55분 26초 KST
        #print(datetime.toString(Qt.DefaultLocaleShortDate)) # 2019. 9. 12. 오후 10:55
        #print(datetime.toString(Qt.ISODate)) # 2019-09-12T22:56:49



        # lbl_red = QLabel('Red')
        # lbl_green = QLabel('Green')
        # lbl_blue = QLabel('Blue')

        # lbl_red.setStyleSheet("color: red;"
        #                       "border-style: solid;"
        #                       "border-width: 2px;"
        #                       "border-color: #FA8072;"
        #                       "border-radius: 3px")
        # lbl_green.setStyleSheet("color: green;"
        #                         "background-color: #7FFFD4")
        # lbl_blue.setStyleSheet("color: blue;"
        #                        "background-color: #87CEFA;"
        #                        "border-style: dashed;"
        #                        "border-width: 3px;"
        #                        "border-color: #1E90FF")

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addWidget(lbl_red)
        # vbox.addWidget(lbl_green)
        # vbox.addWidget(lbl_blue)
        # vbox.addStretch(1)

        # # 절대적 배치 

        # label1 = QLabel('Label1', self)
        # label1.move(20, 20)
        # label2 = QLabel('label2', self)
        # label2.move(20, 60)

        # btn1 = QPushButton('Button1', self)
        # btn1.move(80, 20)
        # btn2 = QPushButton('Button2', self)
        # btn2.move(80, 60)

        # # Grid Layout

        # grid = QGridLayout()
        # grid.addWidget(QLabel('Title:'), 0, 0)
        # grid.addWidget(QLabel('Author:'), 1, 0)
        # grid.addWidget(QLabel('Review:'), 2, 0)

        # grid.addWidget(QLineEdit(),0,1)
        # grid.addWidget(QLineEdit(),1,1)
        # grid.addWidget(QLineEdit(),2,1)


        # # 윈도우 레이아웃 
        # okButton = QPushButton('OK')
        # canceButton = QPushButton('Cancel')

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(canceButton)
        # hbox.addStretch(1)

        # vbox2 = QVBoxLayout()
        # vbox2.addStretch(1)
        # vbox2.addLayout(vbox)
        # vbox2.addLayout(hbox)
        # vbox2.addLayout(grid)
        # vbox2.addStretch(1)

        # #self.setLayout(vbox2) 

        # # Grid Layout

        # btn01 = QPushButton('&Button1', self)
        # btn01.setCheckable(True)
        # btn01.toggle()

        # btn02 = QPushButton(self)
        # btn02.setText('Button&2')

        # btn03 = QPushButton('Button3', self)
        # btn03.setEnabled(False)

        # vbox3 = QVBoxLayout()
        # vbox3.addWidget(btn01)
        # vbox3.addWidget(btn02)
        # vbox3.addWidget(btn03)



        # label01 = QLabel('First Label', self)
        # label01.setAlignment(Qt.AlignCenter)

        # label02 = QLabel('Second Label', self)
        # label02.setAlignment(Qt.AlignVCenter)

        # font01 = label01.font()
        # font01.setPointSize(20)

        # font02 = label02.font()
        # font02.setFamily('Times New Roman')
        # font02.setBold(True)

        # label01.setFont(font01)
        # label02.setFont(font02)

        # layout = QVBoxLayout()
        # layout.addWidget(label01)
        # layout.addWidget(label02)

        # # self.setLayout(layout)
        # # self.setLayout(vbox3) 
