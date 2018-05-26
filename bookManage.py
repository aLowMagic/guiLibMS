# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookManage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QIcon
import pymysql
import datetime
import addBooks

class Ui_booksManage(object):
    def setupUi(self, booksManage):
        booksManage.setObjectName("booksManage")
        booksManage.resize(761, 411)
        booksManage.setStyleSheet("*{background-color: rgb(255, 255, 255)}")
        booksManage.setWindowIcon(QIcon('C:\\Users\\thePr\\Documents\\github\\guiLibMS\\image\\logo.png'))
        self.tableWidget = QtWidgets.QTableWidget(booksManage)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 621, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(65)
        self.lineEdit = QtWidgets.QLineEdit(booksManage)
        self.lineEdit.setGeometry(QtCore.QRect(630, 40, 113, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(booksManage)
        self.lineEdit_2.setGeometry(QtCore.QRect(630, 90, 113, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(booksManage)
        self.lineEdit_3.setGeometry(QtCore.QRect(630, 140, 113, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(booksManage)
        self.lineEdit_4.setGeometry(QtCore.QRect(630, 190, 113, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(booksManage)
        self.pushButton.setGeometry(QtCore.QRect(650, 250, 80, 30))
        self.pushButton.setStyleSheet("*{background-color: #969696}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(booksManage)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 350, 110, 30))
        self.pushButton_3.setStyleSheet("*{background-color: #969696}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(booksManage)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 350, 110, 30))
        self.pushButton_4.setStyleSheet("*{background-color: #969696}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(booksManage)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 350, 110, 30))
        self.pushButton_5.setStyleSheet("*{background-color: #969696}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(booksManage)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 300, 80, 30))
        self.pushButton_6.setStyleSheet("*{background-color: #969696}")
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(booksManage)
        self.pushButton_3.clicked.connect(self.returnToFirstPage)
        self.pushButton_4.clicked.connect(self.beforePage)
        self.pushButton_5.clicked.connect(self.nextPage)
        self.pushButton.clicked.connect(self.bookSearch)
        self.pushButton_6.clicked.connect(self.insertBook)
        QtCore.QMetaObject.connectSlotsByName(booksManage)

    def retranslateUi(self, booksManage):
        _translate = QtCore.QCoreApplication.translate
        booksManage.setWindowTitle(_translate("booksManage", "图书管理"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("booksManage", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("booksManage", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("booksManage", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("booksManage", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("booksManage", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("booksManage", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("booksManage", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("booksManage", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("booksManage", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("booksManage", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("booksManage", "书名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("booksManage", "图书ISBN号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("booksManage", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("booksManage", "分类"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("booksManage", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("booksManage", "在架数目"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("booksManage", "上架时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("booksManage", "图书位置"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("booksManage", "图书价格"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableItems("", "", "", "")

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        #self.lineEdit.setText(_translate("booksManage", "书名"))
        self.lineEdit.setPlaceholderText("书名")
        #self.lineEdit_2.setText(_translate("booksManage", "ISBN号"))
        self.lineEdit_2.setPlaceholderText("ISBN号")
        #self.lineEdit_3.setText(_translate("booksManage", "作者"))
        self.lineEdit_3.setPlaceholderText("作者")
        #self.lineEdit_4.setText(_translate("booksManage", "出版社"))
        self.lineEdit_4.setPlaceholderText("出版社")
        self.pushButton.setText(_translate("booksManage", "查询"))
        self.pushButton_3.setText(_translate("booksManage", "首页"))
        self.pushButton_4.setText(_translate("booksManage", "上一页"))
        self.pushButton_5.setText(_translate("booksManage", "下一页"))
        self.pushButton_6.setText(_translate("booksManage", "录入书目"))

    def returnToFirstPage(self):
        bookName = self.lineEdit.text()
        bookIsbn = self.lineEdit_2.text()
        bookAuthor = self.lineEdit_3.text()
        bookPublisher = self.lineEdit_4.text()
        self.tableItems(bookName, bookIsbn, bookAuthor, bookPublisher)

    def nextPage(self):
        if (self.currentPage == (self.allRows - 1) // 10):
            pass
        elif (self.currentPage < (self.allRows - 1) // 10):
            self.tableWidget.clearContents()
            resultRows = self.result
            self.currentPage = self.currentPage + 1
            # 判断该页行数是否够10
            if (self.allRows >= 10 * (self.currentPage + 1)):
                rowNum = 10
            elif (self.allRows <= 10 * (self.currentPage + 1)):
                rowNum = self.allRows - 10 * self.currentPage

            for i in range(rowNum):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['title']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['isbn']))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['author']))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['classifaction']))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['publisher']))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(str(resultRows[i + (self.currentPage) * 10]['book_num'])))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(resultRows[i + (self.currentPage) * 10]['in_shelf_time'])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['book_position']))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(str(resultRows[i + (self.currentPage) * 10]['price'])))


    def beforePage(self):
        if (self.currentPage == 0):
            pass
        else:
            self.tableWidget.clearContents()
            resultRows = self.result
            self.currentPage = self.currentPage - 1
            for i in range(10):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['title']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['isbn']))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['author']))
                self.tableWidget.setItem(i, 3,
                                         QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['classifaction']))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['publisher']))
                self.tableWidget.setItem(i, 5,
                                         QTableWidgetItem(str(resultRows[i + (self.currentPage) * 10]['book_num'])))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(
                    str(resultRows[i + (self.currentPage) * 10]['in_shelf_time'])))
                self.tableWidget.setItem(i, 7,
                                         QTableWidgetItem(resultRows[i + (self.currentPage) * 10]['book_position']))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(str(resultRows[i + (self.currentPage) * 10]['price'])))

    def bookSearch(self):
        bookName = self.lineEdit.text()
        bookIsbn = self.lineEdit_2.text()
        bookAuthor = self.lineEdit_3.text()
        bookPublisher = self.lineEdit_4.text()
        self.tableItems(bookName, bookIsbn, bookAuthor, bookPublisher)

    def insertBook(self):
        self.paraAddBooks = QtWidgets.QDialog()
        self.window = addBooks.Ui_insertBook()
        self.window.setupUi(self.paraAddBooks)
        self.paraAddBooks.setModal(True)
        self.paraAddBooks.show()

    def tableItems(self, name, isbn, author, publisher): #刷新表格
        if (name == "书名"):
            name = ""
        if (isbn == "ISBN号"):
            isbn = ""
        if (author == "作者"):
            author = ""
        if (publisher == "出版社"):
            publisher = ""
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS', use_unicode=True,
                               charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select * from books_catalogue where title like '%%%s%%' and isbn like '%%%s%%' and author like '%%%s%%' and publisher like '%%%s%%';" %(name, isbn, author, publisher)
        row = cur.execute(sql)
        if row == 0:
            self.msgBox_noStaff.show()
        elif row != 0:
            resultRows = cur.fetchall()
            self.result = resultRows
            self.allRows = row
            self.currentPage = 0
            cur.close()
            conn.close()
            self.tableWidget.clearContents()
            if row > 10:
                row = 10
            for i in range(row):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(resultRows[i]['title']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(resultRows[i]['isbn']))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(resultRows[i]['author']))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(resultRows[i]['classifaction']))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(resultRows[i]['publisher']))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(str(resultRows[i]['book_num'])))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(resultRows[i]['in_shelf_time'])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(resultRows[i]['book_position']))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(str(resultRows[i]['price'])))