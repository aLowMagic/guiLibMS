# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userManage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userManage(object):
    def setupUi(self, userManage):
        userManage.setObjectName("userManage")
        userManage.resize(477, 400)
        userManage.setStyleSheet("*{background-color: rgb(255, 255, 255)}")
        self.tableWidget = QtWidgets.QTableWidget(userManage)
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

        self.retranslateUi(userManage)
        #self.pushButton.clicked.connect(self.searchStaff)
        #self.pushButton_2.clicked.connect(self.deleteStaff)
        #self.pushButton_3.clicked.connect(self.editStaff)
        #self.pushButton_4.clicked.connect(self.addStaff)
        #self.pushButton_6.clicked.connect(self.nextPage)
        #self.pushButton_5.clicked.connect(self.beforePage)
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
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("userManage", "读者姓名"))
        self.lineEdit_2.setText(_translate("userManage", "读者id"))
        self.pushButton.setText(_translate("userManage", "查询"))
        self.pushButton_2.setText(_translate("userManage", "删除"))
        self.pushButton_3.setText(_translate("userManage", "修改"))
        self.pushButton_4.setText(_translate("userManage", "添加"))
        self.pushButton_5.setText(_translate("userManage", "下一页"))
        self.pushButton_6.setText(_translate("userManage", "上一页"))

