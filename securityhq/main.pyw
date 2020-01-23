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

class DashBoardWidget(QWidget):
    def __init__(self, parent=None):
        super(DashBoardWidget, self).__init__(parent)

        hLayout = QHBoxLayout()
        
        self.button1 = QPushButton('버튼1')
        self.button2 = QPushButton('버튼2')
        self.button3 = QPushButton('버튼3')
        self.button4 = QPushButton('버튼4')

        hLayout.addWidget(self.button1)
        hLayout.addWidget(self.button2)
        hLayout.addWidget(self.button3)
        hLayout.addWidget(self.button4)

        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0,0,0,0)
        vLayout.addLayout(hLayout)
        self.setLayout(vLayout)


class AssetList_Widget(QWidget):
    def __init__(self, parent=None):
        super(AssetList_Widget, self).__init__(parent)

        hLayout = QHBoxLayout()
        
        self.button1 = QPushButton('버튼11111')
        self.button2 = QPushButton('버튼22222')
        self.button3 = QPushButton('버튼33333')
        self.button4 = QPushButton('버튼44444')

        hLayout.addWidget(self.button1)
        hLayout.addWidget(self.button2)
        hLayout.addWidget(self.button3)
        hLayout.addWidget(self.button4)

        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0,0,0,0)
        vLayout.addLayout(hLayout)
        self.setLayout(vLayout)


# 분리되어진 위젯중에 메인에 위치하는 윗젯 (Central Widget)
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # self.setGeometry(0, 0, 800, 450)  # x, y, width, height
        # self.setWindowTitle("CentralWidget")

        # self.textLabel = QLabel("Message: ", self)
        # self.textLabel.move(20, 20)

        # self.label = QLabel("", self)
        # self.label.move(80, 20)
        # self.label.resize(150, 30)

        # self.btn1 = QPushButton("Click", self)
        # self.btn1.move(20, 60)
        # # btn1.clicked.connect(self.btn1_clicked)

        # self.btn2 = QPushButton("Clear", self)
        # self.btn2.move(140, 60)
        # # btn2.clicked.connect(self.btn2_clicked)
        self.show()

# 처음 실행되어지는 전체 어플리케이션의 Main Application
class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        # QMainWindows  경우 자체 레이아웃을 갖고 있기 때문에 
        # CentralWidget을 생성해주어야 함.

        mainWidget = MainWidget()
        self.setCentralWidget(mainWidget)

        # 상태바에 뛰울 
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        # -- Windows Title Bar --
        self.setWindowTitle('Security-HQ') # 윈도우 타이틀 

        # -- Status Bar --
        self.statusBar().showMessage('Ready') #상태바 인스턴스 생성 및 표시 
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # 현재 날짜 표시


        # -- Menu Bar --
        # 메뉴바 엑션 설정 및 메뉴 명칭, 단축, 
        # 종료 action
        exitAction = QAction(QIcon('icon/exit.png'), 'Exit', self) # 아이콘표시, Exit 표시
        exitAction.setShortcut('Ctrl+Q') # 단축키 
        exitAction.setStatusTip('Exit Application') # 상태바 표시
        exitAction.triggered.connect(qApp.quit) # 어플리케이션 종료설정 QApplication quit()

        # 종료 action
        saveAction = QAction(QIcon('icon/save.png'), 'Save', self) # 아이콘표시, Exit 표시
        saveAction.setShortcut('Ctrl+S') # 단축키 
        saveAction.setStatusTip('Save Application') # 상태바 표시
        # saveAction.triggered.connect(self.showDialog4) # 

        # 종료 action
        editAction = QAction(QIcon('icon/edit.png'), 'Edit', self) # 아이콘표시, Exit 표시
        editAction.setShortcut('Ctrl+E') # 단축키 
        editAction.setStatusTip('Edit Application') # 상태바 표시
        editAction.triggered.connect(qApp.quit) # 어플리케이션 종료설정 QApplication quit()

        # 종료 action
        printAction = QAction(QIcon('icon/print.png'), 'Print', self) # 아이콘표시, Exit 표시
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

        # 편집 툴바 
        self.editToolbar = self.addToolBar('Edit')
        self.editToolbar.addAction(editAction)


        # 툴바의 콤보박스 
        self.combo = QComboBox(self)
        self.combo.addItem("Item 1")
        self.combo.addItem("Item 2")
        self.combo.addItem("Item 3")
        # self.combo.currentIndexChanged.connect(self.setSomething)
        self.fileToolbar.addWidget(self.combo)
        self.combo.setMinimumSize(self.combo.sizeHint().width(),self.fileToolbar.iconSize().height())
        self.fileToolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)


        ###############################
        # Dockable Widget 정의 
        ###############################

        # dockWidgetTree    = QTreeWidget()
        dockWidgetLeft    = QWidget()
        dockWidgetRight   = QWidget()
        dockWidgetBottom  = QWidget()

        # 독 위젯을 만들고 거기에 위젯을 추가한다.
        self.dockWidget = QDockWidget("메뉴")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable)


        # 
        self.dockWidgetLeftTree = QWidget()
        self.dockWidgetLeftTree.setObjectName("dockWidgetLeftTree")

        # Dockable 트리 위젯 메뉴 
        self.treeWidget = QTreeWidget(self.dockWidgetLeftTree)
        self.treeWidget.setObjectName("verticalLayout")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.treeWidget.setAlternatingRowColors(True)



        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, "자산관리")
        parent.setFlags(parent.flags())
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "자산목록")


        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, "정보보안")
        parent.setFlags(parent.flags())
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "시스템보안1")
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "시스템보안2")


        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, "보안점검")
        parent.setFlags(parent.flags())
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "보안툴1")
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "보안툴2")

        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, "보안점검")
        parent.setFlags(parent.flags())
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "보안툴1")
        child = QTreeWidgetItem(parent) 
        child.setFlags(child.flags())             
        child.setText(0, "보안툴2")



        # self.treeWidget.itemClicked.connect(self.select_wg)
        # 윗젯 선택 하기
        self.treeWidget.itemSelectionChanged.connect(self.select_widget)
#        
        
# """
#         # 메뉴 구성 
#         for i in range(3):
#             parent = QTreeWidgetItem(self.treeWidget)
#             parent.setText(0, "자산관리  {}".format(i))
#             #> parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
#             parent.setFlags(parent.flags() )
#             for x in range(5):
#                 child = QTreeWidgetItem(parent)

#                 #> child.setFlags(child.flags() | Qt.ItemIsUserCheckable)   
#                 child.setFlags(child.flags() )             
#                 child.setText(0, "Child {}".format(x))
#                 #> child.setCheckState(0, Qt.Unchecked)

#         # self.treeWidget.itemClicked.connect(self.login)
#         # 버티컬 레이아웃
# """
        self.vtlayout_TreeMenu = QVBoxLayout(self.dockWidgetLeftTree)
        self.vtlayout_TreeMenu.setContentsMargins(4, 4, 4, 4)
        self.vtlayout_TreeMenu.setObjectName("verticalLayout")
        self.vtlayout_TreeMenu.addWidget(self.treeWidget)


        # 앞에서 만든 위젯을 
        self.dockWidget.setWidget(self.dockWidgetLeftTree)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)


        #########################################################################
        # 왼쪽 위젯 
        self.dockingWidgetLeft = QDockWidget("Icon panel") # 타이틀 설정
        self.dockingWidgetLeft.setObjectName("IconPanel")
        self.dockingWidgetLeft.setWidget(dockWidgetLeft) # 래핑할 위젯 설정
        self.dockingWidgetLeft.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockingWidgetLeft.setFloating(True)
        self.dockingWidgetLeft.widget().setMinimumSize(QSize(80,150))
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dockingWidgetLeft) # 초기 위치 및 도킹위젯을 메인윈도의 
                                                            
        #########################################################################
        # 오른쪽  위젯 
        self.dockingWidgetRight = QDockWidget("속성 창") # 타이틀 설정
        self.dockingWidgetRight.setObjectName("IconPanel")
        self.dockingWidgetRight.setWidget(dockWidgetRight) # 래핑할 위젯 설정
        self.dockingWidgetRight.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockingWidgetRight.setFloating(True)
        self.dockingWidgetRight.widget().setMinimumSize(QSize(200,200))
        self.addDockWidget(Qt.RightDockWidgetArea,self.dockingWidgetRight) # 초기 위치 및 도킹위젯을 메인윈도의 

        #########################################################################
        # 아래쪽 위젯 
        self.dockingWidgetBottom = QDockWidget("알람 콘솔") # 타이틀 설정
        self.dockingWidgetBottom.setObjectName("IconPanel")
        self.dockingWidgetBottom.setWidget(dockWidgetBottom) # 래핑할 위젯 설정
        self.dockingWidgetBottom.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.dockingWidgetBottom.setFloating(True)
        self.dockingWidgetBottom.widget().setMinimumSize(QSize(80,60))
        self.addDockWidget(Qt.BottomDockWidgetArea,self.dockingWidgetBottom) # 초기 위치 및 도킹위젯을 메인윈도의 


        #########################################################################
        # 가운데 위젯을 QStack으로 바꿔가며 보여준다

        self.wg_center = QStackedWidget()
        self.setCentralWidget(self.wg_center)

        Dashboard = DashBoardWidget(self)        
        self.button1 = QPushButton('Btn1')

        # Dashboard.button.clicked.connect(self.login2)

        self.wg_center.addWidget(Dashboard)
        self.setDockOptions(self.AnimatedDocks | self.AllowNestedDocks)
        self.statusBar()


        # 윈도우 표시 정의
        self.setGeometry(0, 0, 1024, 768) # 윈도우 위치 및 크기 
        self.center() #위도우 위치를 중앙에 이동시킴
        self.show() #보여줌 

        
    # TreeWidget에서 선택된 레이블 값 얻기 
    def select_widget(self):
        self.wg_center = QStackedWidget()
        self.setCentralWidget(self.wg_center)

        getSelected = self.treeWidget.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
            print(getChildNode)

            if getChildNode == "자산목록":
                print("자산목록[선택]")
                wg_Asset = AssetList_Widget(self)        
                self.button1 = QPushButton('Btn1')
                self.wg_center.addWidget(wg_Asset)




    # def select_wg(self): 
    #     print("select")



    def center(self): # 중앙에 윈도우를 위치시키는 메소드 
        qr = self.frameGeometry() # 창의 위치 정보와 크기정보를 가지고 옴
        cp = QDesktopWidget().availableGeometry().center() # 사용 모니터 가운데 위치 파악 
        qr.moveCenter(cp) # 현재 창을 화면 중심으로 직각사각형 위치로 이동 , 화면중심, 창중심 일치시킴 
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())

