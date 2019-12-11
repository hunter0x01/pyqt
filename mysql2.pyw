# -*- coding: utf-8 -*- 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pymysql

#
# create database securityhq;
# GRANT ALL PRIVILEGES ON *.* TO 'securityhq'@'%' IDENTIFIED BY 'securityhq';

# DROP TABLE IPAM;

# CREATE TABLE IPAM ( 
#   num       tinyint(3) unsigned NOT NULL, # 1 to 255 순서번호
#   ip        varchar(15) NOT NULL, # IP 주소
#   mac       char(17) NOT NULL, # Mac 주소
#   cmt       varchar(20) NOT NULL, # 사용용도
#   user_req  varchar(10) NULL,  # 요청자
#   user      varchar(10) NULL,  # 수행자
#   created   datetime, # 적용일 
#   memo      tinytext, # 변경 메모
#   PRIMARY KEY (num) # Primary Key 
# );

# insert into ipam(num,ip,mac,cmt,user_req,user,created,memo) values(1,'123.123.123.123','aa:bb:cc:dd:ee:ff','LIBRARY use','박기용','박기용',now(),'최초생성');
# select * from ipam;

# 255.255.255.255
# 12:34:56:78:90:AB

# auto resize header

# dump_conn = pymysql.connect(
#     host=app.config[ 'DUMP_SQLALCHEMY_HOST' ],
#     port=int( app.config[ 'DUMP_SQLALCHEMY_PORT' ] ),
#     user=vault[ 'data' ][ 'username' ],
#     passwd=vault[ 'data' ][ 'password' ],
#     db=app.config[ 'DUMP_SQLALCHEMY_DB' ]
# )


conn = pymysql.connect(
    host='127.0.0.1',
    user='securityhq',
    password='securityhq',
    db='securityhq',
    charset='utf8'
)
#no로 검색
def selectTableSearch(_num):
    cur = conn.cursor()
    sql = "SELECT num,ip,mac,cmt,user_req,user,created,memo FROM ipam WHERE num = %s"
    cur.execute(sql, (str(_num)))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    return rows

#table 리스트
def selectTableList():
    cur = conn.cursor()
    sql = "SELECT num,ip,mac,cmt,user_req,user,created,memo FROM ipam ORDER BY num asc"
    cur.execute(sql)

    rows = cur.fetchall()

    return rows

#table num return list
def selectTableList_ToList():
    cur = conn.cursor()
    sql = "SELECT num FROM ipam"
    cur.execute(sql)

    # rows = list(cur)
    rows = cur.fetchall()
    return rows

 # rows = list( cursor )

#table 데이터 추가
def insertTable(_num, _ip, _mac, _cmt, _user_req, _user, _memo):
    print(_num, _ip, _mac, _cmt, _user_req, _user, _memo)

    cur = conn.cursor()
    sql = "INSERT INTO ipam (num,ip,mac,cmt,user_req,user,created,memo) VALUES (%s, %s, %s, %s, %s, %s, now(), %s)"
    cur.execute(sql, (str(_num), _ip, _mac, _cmt, _user_req, _user, _memo))
    conn.commit()

#table 데이터 수정
def updateTable(_num, _ip, _mac, _cmt, _user_req, _user, _memo):
    cur = conn.cursor()
    sql = """UPDATE ipam SET ip = %s , mac = %s, cmt = %s, user_req = %s, user = %s, created = now(), memo = %s WHERE num = %s"""
    cur.execute(sql, (_ip, _mac, _cmt, _user_req, _user, _memo, str(_num)))
    conn.commit()

#table 데이터 삭제
def deleteTable(_num):
    cur = conn.cursor()
    sql = """DELETE from ipam WHERE num = %s"""
    cur.execute(sql, str(_num))
    conn.commit()

form_class = uic.loadUiType("main_ui2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn_add_clicked)
        self.pushButton_3.clicked.connect(self.btn_modify_clicked)
        self.pushButton_4.clicked.connect(self.btn_delete_clicked)



        #     self.btn
        #     print(num)

        # self.gridLayout

        # QTW = QTreeWidget()

        ti_Top = QTreeWidgetItem(self.QTreeIpAddress)
        ti_Top.setText(0, '아산캠퍼스')
        ti_Loc = QTreeWidgetItem(ti_Top)
        ti_Loc.setText(0,'전산실')
        ti_Zone_Dmz = QTreeWidgetItem(ti_Loc)
        ti_Zone_Dmz.setText(0, 'DMZ')
        ti_Zone_Dmz_Ip = QTreeWidgetItem(ti_Zone_Dmz)
        ti_Zone_Dmz_Ip.setText(0, '134.75.122.0')
        ti_Zone_Int = QTreeWidgetItem(ti_Loc)
        ti_Zone_Int.setText(0, 'INT')
        ti_Zone_Int_Ip = QTreeWidgetItem(ti_Zone_Int)
        ti_Zone_Int_Ip.setText(0, '20.134.75.0')

        self.QTreeIpAddress.expandAll()
        self.QTreeIpAddress.itemDoubleClicked.connect(self.func_TiDoubleClick)
        # init widgets


        #테이블에 더블클릭 이벤트주기
        self.tableWidget.itemDoubleClicked.connect(self.btn_table_double_clicked)

        # 자동 컬럼 리사이징
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeToContents)


        self.lstNum = selectTableList_ToList()
        # print(self.lstNum)

        #테이블 수정 불가능하게 변경
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.refresh()

        # 255 개 IP 그리기 
        self.tableWidget_2.itemDoubleClicked.connect(self.btn_table2_double_clicked)
        self.tableWidget_2.setRowCount(17)

        cnt = 1
        for x in range(0, 17):
            for y in range(0, 15):
                if cnt == 255 : 
                    self.tableWidget_2.setItem(x, y, QTableWidgetItem('BC'))
                else: 
                    for num in self.lstNum:
                        #print(cnt,num[0])
                        type(cnt)
                        type(num[0])
                        if cnt == num[0]:
                            print(cnt,num[0])
                            self.tableWidget_2.setItem(x, y, QTableWidgetItem(str(cnt)))
                            self.tableWidget_2.item(x, y).setBackground(QColor(255,255,0))

                        if cnt != num[0]:
                            print(cnt,num[0])
                            self.tableWidget_2.setItem(x, y, QTableWidgetItem(str(cnt)))
                            self.tableWidget_2.item(x, y).setBackground(QColor(222,222,222))
                            
                    # self.tableWidget.setItem(3, 5,QTableWidgetItem())
                    # self.tableWidget.setItem(3, 5, QtGui.QTableWidgetItem())
                    # self.tableWidget.item(3, 5).setBackground(QtGui.QColor(100,100,150))
                    
                # print(cnt)
                cnt += 1


    def func_TiDoubleClick(self):
        getSelected = self.QTreeIpAddress.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
            print(getChildNode)
            self.refresh()

    # 조회
    def refresh(self):
        rows = selectTableList()
        self.tableWidget.setRowCount(len(rows))
        count  = 0;
        for row in rows:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(count, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(count, 5, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(count, 6, QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(count, 7, QTableWidgetItem(row[7]))
            count += 1


    def btn_table2_double_clicked(self):
        try:
           
            tw_si = self.tableWidget_2.selectedIndexes()

            for idx in tw_si:
                pass
            item = self.tableWidget_2.item(idx.row(), idx.column())
            # self.btn_table_double_clicked()
            QMessageBox.information(self, "Cell", item.text())

        except Exception as e:
            print(e)
            print(type(e))



    #테이블 더블클릭
    def btn_table_double_clicked(self):
        try:
            # QMessageBox.information(self, "message", "더블클릭")

            tw_si = self.tableWidget.selectedIndexes()

            for idx in tw_si:
                pass

            # num,ip,mac,cmt,user_req,user,created,memo 

            #row의 0번째 no
            item = self.tableWidget.item(idx.row(), 0)
            if item is not None:
                txt = item.text()
                self.le_Num.setText(txt)
            else:
                txt = "no data"

            # row의 1번째 name
            item = self.tableWidget.item(idx.row(), 1)
            if item is not None:
                txt = item.text()
                self.le_IP.setText(txt)
            else:
                txt = "no data"

            # row의 2번째 tel
            item = self.tableWidget.item(idx.row(), 2)
            if item is not None:
                txt = item.text()
                self.le_Mac.setText(txt)
            else:
                txt = "no data"

            # row의 3번째 etc
            item = self.tableWidget.item(idx.row(), 3)
            if item is not None:
                txt = item.text()
                self.le_Cmt.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 4)
            if item is not None:
                txt = item.text()
                self.le_User_Req.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 5)
            if item is not None:
                txt = item.text()
                self.le_User.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 6)
            if item is not None:
                txt = item.text()
                self.le_Created.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 7)
            if item is not None:
                txt = item.text()
                self.le_Memo.setText(txt)
            else:
                txt = "no data"

            self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    
    # 조회 버튼
    def btn_clicked(self):
        try:
            QMessageBox.information(self, "message", "조회")
            self.refresh()
        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " + str(e))
            print(e)
            print(type(e))

    # 추가 버튼  # num,ip,mac,cmt,user_req,user,created,memo 
    def btn_add_clicked(self):
        try:
            # QMessageBox.information(self, "message", "추가")
            # def insertTable(_num, _ip, _mac, _cmt, _user_req, _user, _memo):
            #     cur = conn.cursor()
            #     sql = "INSERT INTO ipam (num,ip,mac,cmt,user_req,user,created,memo) VALUES (%s, %s, %s, %s, %s, %s, now(), %s)"
            #     cur.execute(sql, str(_num), _ip, _mac, _cmt, _user_req, _user, _memo)
            #     conn.commit()

            print(self.le_Num.text(), self.le_IP.text(), self.le_Mac.text(), self.le_Cmt.text(), self.le_User_Req.text(), self.le_User.text(), self.le_Memo.text())
            insertTable(self.le_Num.text(), self.le_IP.text(), self.le_Mac.text(), self.le_Cmt.text(), self.le_User_Req.text(), self.le_User.text(), self.le_Memo.text())

            self.refresh()
        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " +str(e))
            print(e)
            print(type(e))
    # 수정 버튼
    def btn_modify_clicked(self):
        try:
            QMessageBox.information(self, "message", "수정")
            updateTable(self.le_Num.text(), self.le_IP.text(), self.le_Mac.text(), self.le_Cmt.text(), self.le_User_Req.text(), self.le_User.text(), self.le_Memo.text())

            self.refresh()
        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " + str(e))
            print(e)
            print(type(e))



    # 삭제 버튼 (no 위치에 가져다 놓고 삭제를 누르면 실행 됨)
    def btn_delete_clicked(self):

        try:
            QMessageBox.information(self, "message", "삭제")

            tw_si = self.tableWidget.selectedIndexes()

            for idx in tw_si:
                pass

            #row의 0번째 no
            item = self.tableWidget.item(idx.row(), 0)
            if item is not None:
                no_txt = item.text()
            else:
                no_txt = "no data"

            deleteTable(no_txt)
            self.refresh()

        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " + str(e))
            print(e)
            print(type(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
