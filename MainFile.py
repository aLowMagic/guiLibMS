# -*- coding: utf-8 -*-

from index import Ui_title_box
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QDialog
import pymysql
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    loginWindow = Ui_title_box()
    loginWindow.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())