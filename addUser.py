# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addUser.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql

class Ui_addUser(object):
    def setupUi(self, addUser):
        addUser.setObjectName("addUser")
        addUser.resize(400, 250)
        self.nameEdit = QtWidgets.QLineEdit(addUser)
        self.nameEdit.setGeometry(QtCore.QRect(190, 50, 140, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.idEdit = QtWidgets.QLineEdit(addUser)
        self.idEdit.setGeometry(QtCore.QRect(190, 110, 140, 30))
        self.idEdit.setObjectName("idEdit")
        self.pushButton = QtWidgets.QPushButton(addUser)
        self.pushButton.setGeometry(QtCore.QRect(160, 170, 80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(addUser)
        self.textBrowser.setGeometry(QtCore.QRect(60, 55, 100, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(addUser)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 115, 100, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.mes_box1 = QMessageBox(QMessageBox.Information, "", "请输入所有信息！", QMessageBox.Ok)
        self.mes_box2 = QMessageBox(QMessageBox.Information, "出现重复内容", "请更改后重新注册！", QMessageBox.Ok)
        self.mes_box3 = QMessageBox(QMessageBox.Information, "未知错误", "未知错误!", QMessageBox.Ok)
        self.mes_box_succeed = QMessageBox(QMessageBox.Information, "成功", "注册成功", QMessageBox.Ok)

        self.retranslateUi(addUser)
        self.pushButton.clicked.connect(self.enSure)
        QtCore.QMetaObject.connectSlotsByName(addUser)

    def retranslateUi(self, addUser):
        _translate = QtCore.QCoreApplication.translate
        addUser.setWindowTitle(_translate("addUser", "用户添加"))
        self.pushButton.setText(_translate("addUser", "确定"))
        self.textBrowser.setHtml(_translate("addUser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">用户姓名：</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("addUser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">用户id：</span></p></body></html>"))

    def enSure(self):
        user_name = self.nameEdit.text()
        user_id = self.idEdit.text()
        if(user_name == "" or user_id == ""):
            self.mes_box1.show()
        else:
            try:
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS',
                                       use_unicode=True, charset='utf8')
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                sqlSelect = "select * from user_manage where user_id = '%s';" % (user_id)
                row = cur.execute(sqlSelect)
                if row == 0:
                    sqlInsert = "insert into user_manage(user_name, user_id) values('%s','%s');"%(user_name, user_id)
                    cur.execute(sqlInsert)
                    conn.commit()
                    cur.close()
                    conn.close()
                    self.mes_box_succeed.show()
                else:
                    self.mes_box2.show()

            except:
                self.mes_box3