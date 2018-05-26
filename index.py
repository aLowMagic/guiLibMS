# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QDialog, QLineEdit
from PyQt5.QtGui import QIcon
import pymysql
from MainWindow import Ui_MainWindow
import sys

class Ui_title_box(object):
    def setupUi(self, title_box):
        title_box.setObjectName("title_box")
        title_box.setEnabled(True)
        title_box.resize(600, 400)
        title_box.setMinimumSize(QtCore.QSize(600, 400))
        title_box.setMaximumSize(QtCore.QSize(600, 400))
        title_box.setWindowIcon(QIcon('C:\\Users\\thePr\\Documents\\github\\guiLibMS\\image\\logo.png'))
        self.title_label = QtWidgets.QLabel(title_box)
        self.title_label.setGeometry(QtCore.QRect(175, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.input_button = QtWidgets.QPushButton(title_box)
        self.input_button.setGeometry(QtCore.QRect(240, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.input_button.setFont(font)
        self.input_button.setObjectName("input_button")
        self.label = QtWidgets.QLabel(title_box)
        self.label.setGeometry(QtCore.QRect(170, 150, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(title_box)
        self.label_2.setGeometry(QtCore.QRect(175, 200, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(title_box)
        self.lineEdit.setGeometry(QtCore.QRect(240, 140, 200, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(title_box)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 190, 200, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.msgBox = QMessageBox(QMessageBox.Information, "用户名或密码错误", "用户名或密码错误", QMessageBox.Ok)
        self.otherMsgBox = QMessageBox(QMessageBox.Information, "未知错误", "未知错误", QMessageBox.Ok)


        self.retranslateUi(title_box)
        self.input_button.clicked.connect(self.indexJudge)
        QtCore.QMetaObject.connectSlotsByName(title_box)

    def retranslateUi(self, title_box):
        _translate = QtCore.QCoreApplication.translate
        title_box.setWindowTitle(_translate("title_box", "XXXX图书馆管理系统"))
        self.title_label.setText(_translate("title_box", "XXXX图书馆管理系统"))
        self.input_button.setText(_translate("title_box", "登陆"))
        self.label.setText(_translate("title_box", "用户名"))
        self.label_2.setText(_translate("title_box", "密码"))


    def loginSucceed(self, userName, userKey):
        self.mainPara = QtWidgets.QWidget()
        self.main_Window = Ui_MainWindow()
        self.main_Window.setupMainWindow(self.mainPara, userName, userKey)
        self.mainPara.show()

    def indexJudge(self):
        try:
            userName = self.lineEdit.text()
            userKey = self.lineEdit_2.text()
            conn = pymysql.connect(host='localhost', port=3306, user='libStaffSelector', password='libStaffSelector',
                                   db='libMS', charset='utf8')
            cur = conn.cursor()
            sql = "select * from manage_list where manage_name = '%s' and manage_key = '%s';" % (userName, userKey)
            if cur.execute(sql) != 0:
                self.loginSucceed(userName, userKey)
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            else:
                self.msgBox.show()
        except:
            self.otherMsgBox.show()
