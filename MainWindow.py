# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
import pymysql
from PyQt5.QtGui import QIcon
from borrow_return import *
from staffManage import *
from userManage import *
from bookManage import *

class Ui_MainWindow(object):
    def setupMainWindow(self, MainWindow, para1, para2):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon('image/logo.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.borrow_return  = QtWidgets.QPushButton(self.centralwidget)
        self.borrow_return.setGeometry(QtCore.QRect(30, 30, 350, 250))
        self.borrow_return.setStyleSheet('QPushButton{border-image:url(image/br.png)}')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.borrow_return.setFont(font)
        self.borrow_return.setObjectName("borrow")
        self.staffManage = QtWidgets.QPushButton(self.centralwidget)
        self.staffManage.setGeometry(QtCore.QRect(420, 320, 350, 250))
        self.staffManage.setStyleSheet('QPushButton{border-image:url(image/manager.png)}')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.staffManage.setFont(font)
        self.staffManage.setObjectName("staffManage")
        self.user_manage = QtWidgets.QPushButton(self.centralwidget)
        self.user_manage.setGeometry(QtCore.QRect(420, 30, 350, 250))
        self.user_manage.setStyleSheet('QPushButton{border-image:url(image/user.png)}')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.user_manage.setFont(font)
        self.user_manage.setObjectName("return_2")
        self.bookManage = QtWidgets.QPushButton(self.centralwidget)
        self.bookManage.setGeometry(QtCore.QRect(30, 320, 350, 250))
        self.bookManage.setStyleSheet('QPushButton{border-image:url(image/logo.jpg)}')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.bookManage.setFont(font)
        self.bookManage.setObjectName("bookManage")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        self.borrow_return.clicked.connect(self.showBorrow_ReturnWindow)
        self.user_manage.clicked.connect(self.showUserManageWindow)
        self.bookManage.clicked.connect(self.showBooksManage)
        self.staffManage.clicked.connect(self.showStaffManage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.msgbox = QMessageBox(QMessageBox.Information, "密码错误！", "密码错误！", QMessageBox.Ok)
        self.msgbox_wrongSelect = QMessageBox(QMessageBox.Information, "error", "无服务器信号")
        self.msgbox_noPermission = QMessageBox(QMessageBox.Information, "error", "您无相应权限！", QMessageBox.Ok)

        #判断该用户的权限级别
        self.userName = para1
        self.userKey = para2
        try:
            conn = pymysql.connect(host='localhost', port=3306, user='libStaffSelector', password='libStaffSelector',
                                   db='libMS', charset='utf8')
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            sql = "select permission from manage_list where manage_name = '%s' and manage_key = '%s';" % (self.userName, self.userKey)
            cur.execute(sql)
            res = cur.fetchall()
            self.permission = int(res[0]['permission'])
        except:
            self.msgbox_wrongSelect.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XXXX图书馆管理系统"))
        self.borrow_return.setText(_translate("MainWindow", "借,还书管理"))
        self.staffManage.setText(_translate("MainWindow", "员工管理"))
        self.user_manage.setText(_translate("MainWindow", "用户管理"))
        self.bookManage.setText(_translate("MainWindow", "图书管理"))



    def showBorrow_ReturnWindow(self):#权限码<=4
        if self.permission <= 4:
            self.para1 = QtWidgets.QDialog()
            self.window1 = Ui_borrow_return()
            self.window1.setupUi(self.para1)
            self.para1.setModal(True)
            self.para1.show()
        else:
            self.msgbox_noPermission.show()

    def showUserManageWindow(self):#权限码<=2
        if self.permission <= 2:
            password, ok = QInputDialog.getText(QtWidgets.QWidget(), "权限验证", "请再次输入密码：", QLineEdit.Password, "")
            if password == self.userKey:
                self.para2 = QtWidgets.QDialog()
                self.window2 = Ui_userManage()
                self.window2.setupUi(self.para2)
                self.para2.show()
            else:
                self.msgbox.show()
        else:
            self.msgbox_noPermission.show()

    def showBooksManage(self):#权限码<=3
        if self.permission <= 3:
            self.para3 = QtWidgets.QDialog()
            self.window3 = Ui_booksManage()
            self.window3.setupUi(self.para3)
            self.para3.show()
        else:
            self.msgbox_noPermission.show()

    def showStaffManage(self):#权限码<=1
        if self.permission <= 1:
            password, ok = QInputDialog.getText(QtWidgets.QWidget(), "权限验证", "请再次输入密码：", QLineEdit.Password, "")
            if password == self.userKey:
                self.para4 = QtWidgets.QDialog()
                self.window4 = Ui_staffManage()
                self.window4.setupUi(self.para4)
                self.para4.show()
            else:
                self.msgbox.show()
        else:
            self.msgbox_noPermission.show()