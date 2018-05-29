# -*- coding: utf-8 -*-

from index import Ui_title_box
from MainWindow import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QDialog
import pymysql
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = Ui_title_box()
    if loginWindow.exec_() == 1:
        information = loginWindow.ret()
        name = information['name']
        key = information['key']
        dialog = QtWidgets.QWidget()
        mainWindow = Ui_MainWindow()
        mainWindow.setupMainWindow(dialog, name, key)
        dialog.show()
        sys.exit(app.exec_())
