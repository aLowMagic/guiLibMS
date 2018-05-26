# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userManage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QTableWidget
from PyQt5.QtGui import QIcon
import pymysql
import addUser

class Ui_userManage(object):
    def setupUi(self, userManage):
        userManage.setObjectName("userManage")
        userManage.resize(477, 400)
        userManage.setStyleSheet("*{background-color: rgb(255, 255, 255)}")
        userManage.setWindowIcon(QIcon('C:\\Users\\thePr\\Documents\\github\\guiLibMS\\image\\user.png'))
        self.tableWidget = QtWidgets.QTableWidget(userManage)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 311, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 127))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 127))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.lineEdit = QtWidgets.QLineEdit(userManage)
        self.lineEdit.setGeometry(QtCore.QRect(330, 50, 115, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(userManage)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 100, 115, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(userManage)
        self.pushButton.setGeometry(QtCore.QRect(350, 150, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(userManage)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 230, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(userManage)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 270, 80, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(userManage)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 310, 80, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(userManage)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 350, 80, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(userManage)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 350, 80, 30))
        self.pushButton_6.setObjectName("pushButton_6")

        self.msgBox_noUser = QMessageBox(QMessageBox.Information, "查询失败！", "无该用户", QMessageBox.Ok)
        self.msgBox_noSelected = QMessageBox(QMessageBox.Information, "未选中用户", "请选择一个项目！", QMessageBox.Ok)
        self.msgBox_deleteFailed = QMessageBox(QMessageBox.Information, "删除失败！", "无法删除", QMessageBox.Ok)

        self.retranslateUi(userManage)
        self.pushButton.clicked.connect(self.searchUser)
        self.pushButton_2.clicked.connect(self.deleteUser)
        #self.pushButton_3.clicked.connect(self.editStaff)
        self.pushButton_4.clicked.connect(self.addUser)
        self.pushButton_5.clicked.connect(self.beforePage)
        self.pushButton_6.clicked.connect(self.nextPage)
        QtCore.QMetaObject.connectSlotsByName(userManage)

    def retranslateUi(self, userManage):
        _translate = QtCore.QCoreApplication.translate
        userManage.setWindowTitle(_translate("userManage", "读者管理"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("userManage", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("userManage", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("userManage", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("userManage", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("userManage", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("userManage", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("userManage", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("userManage", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("userManage", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("userManage", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("userManage", "读者姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("userManage", "读者证件号码"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.currentPage = 0
        self.tableItems("", "", self.currentPage)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        #self.lineEdit.setText(_translate("userManage", "读者姓名"))
        self.lineEdit.setPlaceholderText("读者姓名")
        #self.lineEdit_2.setText(_translate("userManage", "读者id"))
        self.lineEdit_2.setPlaceholderText("读者id")
        self.pushButton.setText(_translate("userManage", "查询/刷新"))
        self.pushButton_2.setText(_translate("userManage", "删除"))
        self.pushButton_3.setText(_translate("userManage", "修改"))
        self.pushButton_4.setText(_translate("userManage", "添加"))
        self.pushButton_5.setText(_translate("userManage", "上一页"))
        self.pushButton_6.setText(_translate("userManage", "下一页"))


    def searchUser(self):
        self.user_name = self.lineEdit.text()
        self.user_id = self.lineEdit_2.text()
        self.tableItems(self.user_name, self.user_id, 0)

    def deleteUser(self):
        if (self.tableWidget.currentRow() == 0 or self.tableWidget.currentItem() == None):
            self.msgBox_noSelected.show()
        else:
            row = self.tableWidget.currentRow()
            userName = self.tableWidget.item(row, 0).text()
            userId = self.tableWidget.item(row, 1).text()
            try:
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS',
                                       use_unicode=True, charset='utf8')
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                sql = "delete from user_manage where user_name = '%s' and user_id = '%s';"%(userName, userId)
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
                self.tableWidget.clearContents()
                self.tableItems("", "", 0)
            except:
                self.msgBox_deleteFailed.show()

    def addUser(self):
        self.paraAddUser = QtWidgets.QDialog()
        self.window = addUser.Ui_addUser()
        self.window.setupUi(self.paraAddUser)
        self.paraAddUser.setModal(True)
        self.paraAddUser.show()

    def beforePage(self):
        if (self.currentPage == 0):
            pass
        else:
            self.currentPage -= 1
            self.tableItems(self.currentName, self.currentId, self.currentPage)

    def nextPage(self):
        if(self.currentPage == self.pageNum):
            pass
        elif(self.currentPage < self.pageNum):
            self.currentPage += 1
            self.tableItems(self.currentName, self.currentId, self.currentPage)


    def tableItems(self, user_name, user_id, page):
        if (user_name == "读者姓名"):
            user_name = ""
        if (user_id == "读者id"):
            user_id = ""
        self.currentName = user_name
        self.currentId = user_id
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS', use_unicode=True,
                               charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sqlRow = "select user_name, user_id from user_manage where user_name like '%%%s%%' and user_id like '%%%s%%';"\
                 %(user_name, user_id)
        sql = "select user_name, user_id from user_manage where user_name like '%%%s%%' and user_id like '%%%s%%' limit %s,%s;"\
              %(user_name, user_id, page*10, (page+1)*10)

        allRow = cur.execute(sqlRow)
        self.pageNum = int(allRow / 10)

        row = cur.execute(sql)
        if row == 0:
            self.msgBox_noUser.show()
        elif row != 0:
            resultRows = cur.fetchall()
            cur.close()
            conn.close()
            self.tableWidget.clearContents()
            for i in range(row):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i]['user_name']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i]['user_id']))