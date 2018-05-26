# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alterStaff.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox
import pymysql

class Ui_addStaff(object):
    def setupUi(self, addStaff, userName, userId):
        addStaff.setObjectName("addStaff")
        addStaff.resize(400, 300)
        self.nameEdit = QtWidgets.QLineEdit(addStaff)
        self.nameEdit.setGeometry(QtCore.QRect(180, 30, 140, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setText(userName)
        self.idEdit = QtWidgets.QLineEdit(addStaff)
        self.idEdit.setGeometry(QtCore.QRect(180, 80, 140, 30))
        self.idEdit.setObjectName("idEdit")
        self.idEdit.setText(userId)
        self.idEdit.setEnabled(False)
        self.keyEdit = QtWidgets.QLineEdit(addStaff)
        self.keyEdit.setGeometry(QtCore.QRect(180, 130, 140, 30))
        self.keyEdit.setObjectName("keyEdit")
        self.keyEdit.setEchoMode(QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(addStaff)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(addStaff)
        self.label.setGeometry(QtCore.QRect(80, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addStaff)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addStaff)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(addStaff)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(addStaff)
        self.comboBox.setGeometry(QtCore.QRect(180, 180, 100, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(addStaff)

        self.pushButton.clicked.connect(self.ensure)
        QtCore.QMetaObject.connectSlotsByName(addStaff)

        self.msgBox_notFull = QMessageBox(QMessageBox.Information, "有项目未填写", "请填写所有项目！", QMessageBox.Ok)
        self.msgBox_succeed = QMessageBox(QMessageBox.Information, "成功！", "修改成功!", QMessageBox.Ok)
        self.msgBox_failed = QMessageBox(QMessageBox.Information, "修改失败！", "员工信息修改失败", QMessageBox.Ok)

        self.userid = userId

    def retranslateUi(self, addStaff):
        _translate = QtCore.QCoreApplication.translate
        addStaff.setWindowTitle(_translate("addStaff", "员工信息修改"))
        self.pushButton.setText(_translate("addStaff", "确定"))
        self.label.setText(_translate("addStaff", "员工姓名："))
        self.label_2.setText(_translate("addStaff", "员工ID："))
        self.label_3.setText(_translate("addStaff", "密码："))
        self.label_4.setText(_translate("addStaff", "权限："))
        self.comboBox.setItemText(0, _translate("addStaff", "1级权限"))
        self.comboBox.setItemText(1, _translate("addStaff", "2级权限"))
        self.comboBox.setItemText(2, _translate("addStaff", "3级权限"))
        self.comboBox.setItemText(3, _translate("addStaff", "4级权限"))

    def ensure(self):
        name = self.nameEdit.text()
        id = self.userid
        passWord = self.keyEdit.text()
        permission = self.comboBox.currentText()
        perDic = {"4级权限": '4', "3级权限": '3', "2级权限": '2', "1级权限": '1'}
        per = perDic[permission]
        if (name == "" or passWord == ""):
            self.mes_box1.show()
        else:
            try:
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS',
                                       use_unicode=True, charset='utf8')
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                sqlUpdate = "update manage_list set manage_name='%s', manage_key='%s', permission='%s' where manage_id='%s';"\
                            % (name, passWord, per, id)
                cur.execute(sqlUpdate)
                conn.commit()
                cur.close()
                conn.close()
                self.msgBox_succeed.show()
            except:
                self.msgBox_failed.show()
