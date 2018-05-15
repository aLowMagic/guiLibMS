# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addStaff.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox
import pymysql

class Ui_addStaff(object):
    def setupUi(self, addStaff):
        addStaff.setObjectName("addStaff")
        addStaff.resize(400, 300)
        self.nameEdit = QtWidgets.QLineEdit(addStaff)
        self.nameEdit.setGeometry(QtCore.QRect(190, 40, 140, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.idEdit = QtWidgets.QLineEdit(addStaff)
        self.idEdit.setGeometry(QtCore.QRect(190, 90, 140, 30))
        self.idEdit.setObjectName("idEdit")
        self.keyEdit = QtWidgets.QLineEdit(addStaff)
        self.keyEdit.setGeometry(QtCore.QRect(190, 140, 140, 30))
        self.keyEdit.setObjectName("keyEdit")
        self.pushButton = QtWidgets.QPushButton(addStaff)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(addStaff)
        self.textBrowser.setGeometry(QtCore.QRect(60, 45, 100, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(addStaff)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 145, 100, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(addStaff)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 95, 100, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.keyEdit.setEchoMode(QLineEdit.Password)
        self.retranslateUi(addStaff)
        self.mes_box1 = QMessageBox(QMessageBox.Information, "", "请输入所有信息！", QMessageBox.Ok)
        self.mes_box2 = QMessageBox(QMessageBox.Information, "出现重复内容", "请更改后重新注册！", QMessageBox.Ok)
        self.mes_box3 = QMessageBox(QMessageBox.Information, "未知错误", "未知错误!", QMessageBox.Ok)
        self.mes_box_succeed = QMessageBox(QMessageBox.Information, "成功", "注册成功", QMessageBox.Ok)

        self.pushButton.clicked.connect(self.enSure)
        QtCore.QMetaObject.connectSlotsByName(addStaff)

    def retranslateUi(self, addStaff):
        _translate = QtCore.QCoreApplication.translate
        addStaff.setWindowTitle(_translate("addStaff", "员工添加"))
        self.pushButton.setText(_translate("addStaff", "确定"))
        self.textBrowser.setHtml(_translate("addStaff",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">员工姓名：</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("addStaff",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">员工密码：</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("addStaff",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">员工id：</span></p></body></html>"))

    def enSure(self):
        manageName = self.nameEdit.text()
        manageId = self.idEdit.text()
        manageKey = self.keyEdit.text()
        if(manageName == "" or manageId == "" or manageKey == ""):
            self.mes_box1.show()
        else:
            try:
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS',
                                       use_unicode=True, charset='utf8')
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                sqlSelect = "select * from manage_list where manage_name = '%s' or manage_id = '%s';" % (manageName, manageId)
                row = cur.execute(sqlSelect)
                if row == 0:
                    print(row)
                    sqlInsert = "insert into manage_list(manage_name, manage_key, manage_id) values('%s','%s','%s');"%(manageName, manageKey, manageId)
                    cur.execute(sqlInsert)
                    conn.commit()
                    cur.close()
                    conn.close()
                    self.mes_box_succeed.show()
                else:
                    self.mes_box2.show()

            except:
                self.mes_box3

