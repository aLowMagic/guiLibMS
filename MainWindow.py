# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupMainWindow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.borrow = QtWidgets.QPushButton(self.centralwidget)
        self.borrow.setGeometry(QtCore.QRect(30, 30, 350, 250))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.borrow.setFont(font)
        self.borrow.setObjectName("borrow")
        self.staffManage = QtWidgets.QPushButton(self.centralwidget)
        self.staffManage.setGeometry(QtCore.QRect(420, 320, 350, 250))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.staffManage.setFont(font)
        self.staffManage.setObjectName("staffManage")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(420, 30, 350, 250))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.return_2.setFont(font)
        self.return_2.setObjectName("return_2")
        self.bookManage = QtWidgets.QPushButton(self.centralwidget)
        self.bookManage.setGeometry(QtCore.QRect(30, 320, 350, 250))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        self.bookManage.setFont(font)
        self.bookManage.setObjectName("bookManage")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        #self.borrow.clicked.connect(MainWindow.showBorrowWindow)
        #self.return_2.clicked.connect(MainWindow.showReturnWindow)
        #self.bookManage.clicked.connect(MainWindow.showBooksManage)
        #self.staffManage.clicked.connect(MainWindow.showStaffManage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XXXX图书馆管理系统"))
        self.borrow.setText(_translate("MainWindow", "借书管理"))
        self.staffManage.setText(_translate("MainWindow", "员工管理"))
        self.return_2.setText(_translate("MainWindow", "还书管理"))
        self.bookManage.setText(_translate("MainWindow", "图书管理"))

    def show_mainWindow(self):
        self.show()