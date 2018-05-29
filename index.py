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

class Ui_title_box(QDialog):

    def __init__(self):
        super(Ui_title_box, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("title_box")
        self.setEnabled(True)
        self.resize(600, 400)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.setMaximumSize(QtCore.QSize(600, 400))
        self.setWindowIcon(QIcon('C:\\Users\\thePr\\Documents\\github\\guiLibMS\\image\\logo.png'))
        self.title_label = QtWidgets.QLabel(self)
        self.title_label.setGeometry(QtCore.QRect(175, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.input_button = QtWidgets.QPushButton(self)
        self.input_button.setGeometry(QtCore.QRect(240, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.input_button.setFont(font)
        self.input_button.setObjectName("input_button")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(170, 150, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(175, 200, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(240, 140, 200, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 190, 200, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.msgBox = QMessageBox(QMessageBox.Information, "用户名或密码错误", "用户名或密码错误", QMessageBox.Ok)
        self.otherMsgBox = QMessageBox(QMessageBox.Information, "未知错误", "未知错误", QMessageBox.Ok)


        self.retranslateUi()
        self.input_button.clicked.connect(self.indexJudge)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("title_box", "XXXX图书馆管理系统"))
        self.title_label.setText(_translate("title_box", "XXXX图书馆管理系统"))
        self.input_button.setText(_translate("title_box", "登陆"))
        self.label.setText(_translate("title_box", "用户名"))
        self.label_2.setText(_translate("title_box", "密码"))



    def indexJudge(self):
        try:
            userName = self.lineEdit.text()
            userKey = self.lineEdit_2.text()
            conn = pymysql.connect(host='localhost', port=3306, user='libStaffSelector', password='libStaffSelector',
                                   db='libMS', charset='utf8')
            cur = conn.cursor()
            sql = "select * from manage_list where manage_name = '%s' and manage_key = '%s';" % (userName, userKey)
            if cur.execute(sql) != 0:
                self.accept()
            else:
                self.msgBox.show()
        except:
            self.otherMsgBox.show()

    def ret(self):
        name = self.lineEdit.text()
        key = self.lineEdit_2.text()
        information = {'name': name, 'key': key}
        return information

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.close()