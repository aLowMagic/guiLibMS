# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffManage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
import pymysql
import addStaff

class Ui_staffManage(object):
    def setupUi(self, staffManage):
        staffManage.setObjectName("staffManage")
        staffManage.resize(477, 400)
        staffManage.setStyleSheet("*{background-color: rgb(255, 255, 255)}")
        self.tableWidget = QtWidgets.QTableWidget(staffManage)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 311, 331))
        self.tableWidget.setObjectName("tableWidget")
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
        self.lineEdit = QtWidgets.QLineEdit(staffManage)
        self.lineEdit.setGeometry(QtCore.QRect(330, 50, 115, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(staffManage)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 100, 115, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(staffManage)
        self.pushButton.setGeometry(QtCore.QRect(350, 150, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(staffManage)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 200, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(staffManage)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 250, 80, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(staffManage)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 300, 80, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(staffManage)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 350, 80, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(staffManage)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 350, 80, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.retranslateUi(staffManage)

        self.pushButton.clicked.connect(self.searchStaff)
        self.pushButton_2.clicked.connect(self.deleteStaff)
        self.pushButton_3.clicked.connect(self.editStaff)
        self.pushButton_4.clicked.connect(self.addStaff)
        self.pushButton_5.clicked.connect(self.beforePage)
        self.pushButton_6.clicked.connect(self.nextPage)
        QtCore.QMetaObject.connectSlotsByName(staffManage)

        self.msgBox_noItems = QMessageBox(QMessageBox.Information, "无法查询", "请输入查询内容", QMessageBox.Ok)
        self.msgBox_noStaff = QMessageBox(QMessageBox.Information, "查询失败！", "无该用户", QMessageBox.Ok)
        self.msgBox_deleteFailed = QMessageBox(QMessageBox.Information, "删除失败！", "无法删除", QMessageBox.Ok)
        self.msgBox_deleteSuecceed = QMessageBox(QMessageBox.Information, "删除成功!", "删除成功！", QMessageBox.Ok)
        self.msgBox_noSelected = QMessageBox(QMessageBox.Information, "请选择一个项目", "请选择一个项目！", QMessageBox.Ok)
        self.msgBox_noUse = QMessageBox(QMessageBox.Information, "暂未开启该功能", "暂未开启该功能！", QMessageBox.Ok)


    def retranslateUi(self, staffManage):
        _translate = QtCore.QCoreApplication.translate
        staffManage.setWindowTitle(_translate("staffManage", "员工管理"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("staffManage", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("staffManage", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("staffManage", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("staffManage", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("staffManage", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("staffManage", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("staffManage", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("staffManage", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("staffManage", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("staffManage", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("staffManage", "员工姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("staffManage", "员工id"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableItems("", "")

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("staffManage", "员工姓名"))
        self.lineEdit_2.setText(_translate("staffManage", "员工id"))
        self.pushButton.setText(_translate("staffManage", "查询"))
        self.pushButton_2.setText(_translate("staffManage", "删除"))
        self.pushButton_3.setText(_translate("staffManage", "修改"))
        self.pushButton_4.setText(_translate("staffManage", "添加"))
        self.pushButton_5.setText(_translate("staffManage", "上一页"))
        self.pushButton_6.setText(_translate("staffManage", "下一页"))



    def searchStaff(self):
        name = self.lineEdit.text()
        id = self.lineEdit_2.text()
        self.tableItems(name, id)

    def deleteStaff(self):
        if (self.tableWidget.currentRow() == 0 or self.tableWidget.currentItem() == None):
            self.msgBox_noSelected.show()
        else:
            row = self.tableWidget.currentRow()
            managerName = self.tableWidget.item(row, 0).text()
            managerId = self.tableWidget.item(row, 1).text()
            try:
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS',
                                       use_unicode=True, charset='utf8')
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                sql = "delete from manage_list where manage_name = '%s' and manage_id = '%s';"%(managerName, managerId)
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
                self.tableWidget.clearContents()
                self.tableItems("", "")
            except:
                self.msgBox_deleteFailed.show()

    def editStaff(self):
        self.msgBox_noUse.show()

    def addStaff(self):
        self.paraAddStaff = QtWidgets.QDialog()
        self.window = addStaff.Ui_addStaff()
        self.window.setupUi(self.paraAddStaff)
        self.paraAddStaff.show()

    def beforePage(self):
        if (self.currentPage == 0):
            pass
        else:
            self.tableWidget.clearContents()
            resultRows = self.result
            self.currentPage = self.currentPage - 1
            for i in range(10):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i + (self.currentPage)*10]['manage_name']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i + (self.currentPage)*10]['manage_id']))

    def nextPage(self):
        if(self.currentPage == (self.allRows-1) // 10):
            pass
        elif(self.currentPage < (self.allRows-1) // 10):
            self.tableWidget.clearContents()
            resultRows = self.result
            self.currentPage = self.currentPage + 1
            #判断该页行数是否够10
            if (self.allRows >= 10*(self.currentPage + 1)):
                rowNum = 10
            elif (self.allRows <= 10*(self.currentPage + 1)):
                rowNum = self.allRows - 10 * self.currentPage

            for i in range(rowNum):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i + (self.currentPage)*10]['manage_name']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i + (self.currentPage)*10]['manage_id']))

    def tableItems(self, name, id): #刷新表格
        if (name == "员工姓名"):
            name = ""
        if (id == "员工id"):
            id = ""
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS', use_unicode=True,
                               charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select manage_name, manage_id from manage_list"
        if name != "" and id != "":
            sql += " where manage_name='%s' and manage_id='%s';" % (name, id)
        elif name != "":
            sql += " where manage_name='%s';" % name
        elif id != "":
            sql += "where manage_id='%s';" % id
        else:
            sql += ';'
        print(sql)
        row = cur.execute(sql)
        if row == 0:
            self.msgBox_noStaff.show()
            print(row)
        elif row != 0:
            resultRows = cur.fetchall()
            self.result = resultRows
            self.allRows = row
            self.currentPage = 0
            cur.close()
            conn.close()
            self.tableWidget.clearContents()
            for i in range(row):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i]['manage_name']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i]['manage_id']))
