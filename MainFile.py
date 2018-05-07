# -*- coding: utf-8 -*-

from index import Ui_title_box
from MainWindow import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QDialog
import pymysql
from PyQt5 import QtWidgets

class indexWindow(Ui_title_box):

    mainWindow = Ui_MainWindow()
    def indexJudge(self):
        userName = self.lineEdit.text()
        userKey = self.lineEdit_2.text()
        conn = pymysql.connect(host='localhost', port=3306, user='libStaffSelector', password='libStaffSelector', db='libMS', charset='utf8')
        cur = conn.cursor()
        sql = "select * from manage_list where manage_name = '%s' and manage_key = '%s';" %(userName, userKey)
        if cur.execute(sql) != 0:
            para.close()
            self.mainWindow.setupMainWindow(para)
            para.show()
        else:
            self.msgBox.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    para = QtWidgets.QWidget()
    index = indexWindow()
    index.setupUi(para)
    para.show()
    sys.exit(app.exec_())