# -*- coding: utf-8 -*- 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5 import uic
import pymysql


# brew services stop mariadb
# brew services start mariadb

# MariaDB [securityhq]> SHOW VARIABLES WHERE Variable_Name LIKE "%dir";
# +---------------------------+----------------------------------------------------------+
# | Variable_name             | Value                                                    |
# +---------------------------+----------------------------------------------------------+
# | aria_sync_log_dir         | NEWFILE                                                  |
# | basedir                   | /usr/local/opt/mariadb                                   |
# | character_sets_dir        | /usr/local/Cellar/mariadb/10.4.6_1/share/mysql/charsets/ |
# | datadir                   | /usr/local/var/mysql/                                    |
# | innodb_data_home_dir      |                                                          |
# | innodb_log_group_home_dir | ./                                                       |
# | innodb_tmpdir             |                                                          |
# | lc_messages_dir           |                                                          |
# | plugin_dir                | /usr/local/opt/mariadb/lib/plugin/                       |
# | slave_load_tmpdir         | /var/folders/bf/286d40s1677g0g0b7gd4jgl40000gn/T/        |
# | tmpdir                    | /var/folders/bf/286d40s1677g0g0b7gd4jgl40000gn/T/        |
# | wsrep_data_home_dir       | /usr/local/var/mysql/                                    |
# +---------------------------+----------------------------------------------------------+
# 12 rows in set (0.003 sec)

# SHOW VARIABLES WHERE Variable_Name LIKE "%dir";


# create database securityhq;
#-- GRANT ALL PRIVILEGES ON *.* TO 'securityhq'@'%' IDENTIFIED BY 'securityhq';


#Starting with MySQL 8 you no longer can (implicitly) create a user using the GRANT command.
#Use CREATE USER instead, followed by the GRANT statement:

# CREATE USER 'securityhq'@'%' IDENTIFIED BY 'securityhq';
# GRANT ALL PRIVILEGES ON *.* TO 'securityhq'@'%' WITH GRANT OPTION;

# DROP TABLE IPAM;

# CREATE TABLE IPAM ( 
#   num       tinyint(3) unsigned NOT NULL, # 1 to 255 순서번호
#   ip        varchar(11) NOT NULL, # IP 주소
#   mac       char(17) NOT NULL, # Mac 주소
#   compnm    varchar(100) NULL,  # 수행자
#   cmt       varchar(20) NOT NULL, # 사용용도
#   user_req  varchar(10) NULL,  # 요청자
#   user      varchar(10) NULL,  # 수행자
#   created   datetime, # 적용일 
#   memo      tinytext, # 변경 메모
#   PRIMARY KEY (num,ip) # Primary Key 
# );

# insert into ipam(num,ip,mac,cmt,user_req,user,created,memo) values(1,'123.123.123.123','aa:bb:cc:dd:ee:ff','LIBRARY use','박기용','박기용',now(),'최초생성');
# select * from ipam;

# Network Default Input
# insert into ipam(num,ip,mac,cmt,user_req,user,created,memo) values(0,'134.75.122','aa:aa:aa:aa:aa:aa','NET','박기용','박기용',now(),'네트워크기본');
# insert into ipam(num,ip,mac,cmt,user_req,user,created,memo) values(0,'10.75.122' ,'aa:aa:aa:aa:aa:aa','NET','박기용','박기용',now(),'네트워크기본');
# insert into ipam(num,ip,mac,cmt,user_req,user,created,memo) values(0,'12.75.122' ,'aa:aa:aa:aa:aa:aa','NET','박기용','박기용',now(),'네트워크기본');
# insert into ipam(num,ip,mac,cmt,user_req,user,created,memo) values(0,'172.16.1'  ,'aa:aa:aa:aa:aa:aa','NET','박기용','박기용',now(),'네트워크기본');

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


drop table mac_oui;

create table mac_oui (
    oui char(13) NOT NULL,
    priv varchar(1) NULL,
    compnm varchar(100) NULL,
    compaddr varchar(220) NULL,
    countrycd char(2) NULL,
    assignblk char(4) NULL,
    create_dt date NULL,
    update_dt date NULL,
    primary key(oui) 
);

 # ALTER TABLE `mac_oui` DROP TABLESPACE;


# SHOW GLOBAL VARIABLES LIKE 'local_infile';
# SET GLOBAL local_infile = 'ON';
# SHOW GLOBAL VARIABLES LIKE 'local_infile';



# LOAD DATA LOCAL INFILE '/Users/steve/Downloads/macaddress.io-db.csv'  INTO TABLE securityhq.mac_oui FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' ;

SHOW WARNINGS;

ALTER TABLE  mac_oui DROP priv;
ALTER TABLE  mac_oui DROP compaddr;
ALTER TABLE  mac_oui DROP assignblk;
ALTER TABLE  mac_oui DROP create_dt;
ALTER TABLE  mac_oui DROP update_dt;


# ALTER TABLE dbName.tableName DIABLE KEYS;

# ALTER TABLE dbName.tableName ENABLE KEYS;

# select oui,compnm,countrycd from mac_oui where oui='10:93:E9';

# select distinct(substring_index(ip,'.',3)) from ipam;

conn = pymysql.connect(
    host='127.0.0.1',
    user='securityhq',
    password='securityhq',
    db='securityhq',
    charset='utf8'
)

# IP 위 검색 (unique)
def selectIPRange():
    cur = conn.cursor()
    sql = "select distinct(substring_index(ip,'.',3)) from ipam"
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


#no로 검색
def selectTableSearch(_num):
    cur = conn.cursor()
    sql = "SELECT num,ip,mac,compnm,cmt,user_req,user,created,memo FROM ipam WHERE num = %s"
    cur.execute(sql, (str(_num)))

    row = cur.fetchall()
    return row


#table 리스트
def str_get_oui(_mac):

    cur = conn.cursor()
    sql = "SELECT compnm FROM mac_oui where oui = %s"
    cur.execute(sql, _mac[:8].upper())
    rows = cur.fetchall()
    result = ''.join(''.join(elems) for elems in rows)
    if result == "": 
        return "Unknown"
    else:
        return result



#table 리스트
def selectTableList():
    cur = conn.cursor()
    # sql = "SELECT num,ip,mac,compnm,cmt,user_req,user,created,memo FROM ipam WHERE num != '0' ORDER BY num asc"
    sql = "SELECT num,ip,mac,compnm,cmt,user_req,user,created,memo FROM ipam where num <> 0 ORDER BY num asc"
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
def insertTable(_num, _ip, _mac, _cmt, _user_req, _user, _memo, _compnm):
    print(_num, _ip, _mac, _cmt, _user_req, _user, _memo, _compnm)

    cur = conn.cursor()
    sql = "INSERT INTO ipam (num,ip,mac,cmt,user_req,user,created,memo,compnm) VALUES (%s, %s, %s, %s, %s, %s, now(), %s, %s)"
    cur.execute(sql, (str(_num), _ip, _mac, _cmt, _user_req, _user, _memo, _compnm))
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
        self.pbtn_search.clicked.connect(self.btn_clicked)
        self.pbtn_add.clicked.connect(self.btn_add_clicked)
        self.pbtn_modify.clicked.connect(self.btn_modify_clicked)
        self.pbtn_delete.clicked.connect(self.btn_delete_clicked)
        self.pbtn_oui.clicked.connect(self.oui_btn_clicked)
        # self.pbtn_oui.clicked.connect(self.btn_oui_clicked)



        #     self.btn
        #     print(num)

        # self.gridLayout

        # QTW = QTreeWidget()


        
        headerItem  = QTreeWidgetItem()
        item    = QTreeWidgetItem()

        for i in range(1):
            parent = QTreeWidgetItem(self.QTreeIpAddress)
            parent.setText(0, "관리 대역")
            # parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            parent.setFlags(parent.flags())

            get_rows = selectIPRange()
            # cnt = 0
            # for row in get_rows:
            #     ti_Loc.setText(cnt, row[0])
            #     cnt = cnt + 1


            for x in get_rows:
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, "IP 대역 : {}.0".format(x[0]))
                child.setCheckState(0, Qt.Unchecked)


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


        # print(self.lstNum)

        #테이블 수정 불가능하게 변경
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)


        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.itemDoubleClicked.connect(self.btn_table2_double_clicked)
        self.tableWidget_2.setRowCount(17)
        # self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        # self.tableWidget_2.horizontalHeader().setVisible(False) 
        # self.tableWidget_2.horizontalHeader().setVisible(True) 




        self.refresh()
        self.refresh2()
        self.refresh3()

        # 255 개 IP 그리기 




    def btn_oui_clicked(self):
        if(self.le_Mac.text()):
            txtOui = str_get_oui(self.le_Mac.text())
            print(txtOui)
        # print(''.join(elems) for elems in row)
        


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
            self.tableWidget.setItem(count, 6, QTableWidgetItem(row[6]))
            self.tableWidget.setItem(count, 7, QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(count, 8, QTableWidgetItem(row[8]))
            count += 1

    def refresh2(self):
        cnt = 1
        for x in range(0, 17):
            for y in range(0, 15):
                self.tableWidget_2.setItem(x, y, QTableWidgetItem(str(cnt)))
                cnt = cnt + 1


    def refresh3(self):
        self.lstNum = selectTableList_ToList()
        cnt = 1
        for x in range(0, 17):
            for y in range(0, 15):

                for num in self.lstNum:
                    if cnt == int(num[0]):
                        #print(cnt,int(num[0]))
                        font = QFont()
                        font.setBold(True)
                        self.tableWidget_2.item(x, y).setBackground(QColor(255,255,0))
                        self.tableWidget_2.item(x, y).setForeground(QBrush(QColor(255, 0, 0)))
                        self.tableWidget_2.item(x, y).setFont(font)
                cnt += 1



    def btn_table2_double_clicked(self):
        try:
            tw_si = self.tableWidget_2.selectedIndexes()
            for idx in tw_si:
                pass
            item = self.tableWidget_2.item(idx.row(), idx.column())


            self.lstNum = selectTableList_ToList()

            bUsedFlag = False

            for x in range(0, 17):
                for y in range(0, 15):

                    for num in self.lstNum:
                        if int(item.text()) == int(num[0]):
                            bUsedFlag = True
                            break


            if bUsedFlag:
                rows = selectTableSearch(item.text())
                for row in rows:
                    self.le_Num.setText(str(row[0]))
                    self.le_IP.setText(row[1])
                    self.le_Mac.setText(row[2])
                    self.le_Oui.setText(row[3])
                    self.le_Cmt.setText(row[4])
                    self.le_User.setText(row[5])
                    self.le_User_Req.setText(row[6])
                    self.le_Created.setText(str(row[7]))
                    self.le_Memo.setText(row[8])

                # QMessageBox.information(self, "알림", "IP : "+item.text()+" 가 이미 할당 되었습니다.")

            else:
                self.le_Num.setText("")
                self.le_IP.setText("")
                self.le_Mac.setText("")
                self.le_Cmt.setText("")
                self.le_Oui.setText("")
                self.le_User.setText("")
                self.le_User_Req.setText("")
                self.le_Created.setText("")
                self.le_Memo.setText("")

                self.le_Num.setText(item.text())
                self.le_IP.setText('134.75.122.'+item.text())
                QMessageBox.information(self, "선택된 IP를 할당합니다.", "IP : "+item.text()+" 를 할당합니다.")

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

            item = self.tableWidget.item(idx.row(), 3)
            if item is not None:
                txt = item.text()
                self.le_Oui.setText(txt)
            else:
                txt = "no data"

            # row의 3번째 etc
            item = self.tableWidget.item(idx.row(), 4)
            if item is not None:
                txt = item.text()
                self.le_Cmt.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 5)
            if item is not None:
                txt = item.text()
                self.le_User_Req.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 6)
            if item is not None:
                txt = item.text()
                self.le_User.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 7)
            if item is not None:
                txt = item.text()
                self.le_Created.setText(txt)
            else:
                txt = "no data"

            item = self.tableWidget.item(idx.row(), 8)
            if item is not None:
                txt = item.text()
                self.le_Memo.setText(txt)
            else:
                txt = "no data"




            self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    def oui_btn_clicked(self):
        try:
            selectIPRange()


        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " + str(e))
            print(e)
            print(type(e))

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
            insertTable(self.le_Num.text(), self.le_IP.text(), self.le_Mac.text(), self.le_Cmt.text(), self.le_User_Req.text(), self.le_User.text(), self.le_Memo.text(), str_get_oui(self.le_Mac.text()))
            QMessageBox.information(self, "알림", "추가완료")
            self.refresh()
            self.refresh2()
            self.refresh3()

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

            # tw_si = self.tableWidget.selectedIndexes()

            # for idx in tw_si:
            #     pass

            #row의 0번째 no
            item = self.le_Num.text()
            if item is not None:

                deleteTable(item)
                self.le_Num.setText("")
                self.le_IP.setText("")
                self.le_Mac.setText("")
                self.le_Cmt.setText("")
                self.le_Oui.setText("")
                self.le_User.setText("")
                self.le_User_Req.setText("")
                self.le_Created.setText("")
                self.le_Memo.setText("")
                QMessageBox.information(self, "알림", "삭제 완료")
                self.refresh()
                self.refresh2()
                self.refresh3()
            else:
                QMessageBox.information(self, "알림", "삭제 할 수 없습니다.")


        except Exception as e:
            QMessageBox.warning(self, "[Error Message]", "에러타입 : " + str(type(e)) + "\n에러내용 : " + str(e))
            print(e)
            print(type(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
