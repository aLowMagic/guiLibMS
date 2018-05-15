# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow_return.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QApplication
import datetime
import time
import pymysql

class Ui_borrow_return(object):
    def setupUi(self, borrow_return):
        borrow_return.setObjectName("borrow_return")
        borrow_return.resize(400, 400)
        self.toolBox = QtWidgets.QToolBox(borrow_return)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.toolBox.setObjectName("toolBox")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 400, 348))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.page_1.setFont(font)
        self.page_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.page_1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.page_1.setToolTipDuration(-1)
        self.page_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.page_1.setObjectName("page_1")
        self.isbn_2 = QtWidgets.QLineEdit(self.page_1)
        self.isbn_2.setGeometry(QtCore.QRect(190, 40, 140, 30))
        self.isbn_2.setObjectName("isbn_2")
        self.isbn_3 = QtWidgets.QLineEdit(self.page_1)
        self.isbn_3.setGeometry(QtCore.QRect(190, 90, 140, 30))
        self.isbn_3.setObjectName("isbn_3")
        self.pushButton = QtWidgets.QPushButton(self.page_1)
        self.pushButton.setGeometry(QtCore.QRect(155, 300, 90, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.page_1)
        self.comboBox.setGeometry(QtCore.QRect(190, 140, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.page_1)
        self.dateEdit.setGeometry(QtCore.QRect(190, 190, 140, 30))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.year = datetime.datetime.now().year
        self.month = datetime.datetime.now().month
        self.day = datetime.datetime.now().day
        self.dateEdit.setDate(QtCore.QDate(self.year, self.month, self.day))
        self.dateEdit.setObjectName("dateEdit")
        self.spinBox = QtWidgets.QSpinBox(self.page_1)
        self.spinBox.setGeometry(QtCore.QRect(190, 240, 50, 30))
        self.spinBox.setObjectName("spinBox")
        self.textEdit = QtWidgets.QTextEdit(self.page_1)
        self.textEdit.setGeometry(QtCore.QRect(60, 40, 110, 30))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_1)
        self.textBrowser.setGeometry(QtCore.QRect(60, 90, 110, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_1)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 140, 110, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_1)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 190, 110, 30))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_1)
        self.textBrowser_5.setGeometry(QtCore.QRect(60, 240, 110, 30))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.toolBox.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 400, 348))
        self.page_2.setObjectName("page_2")
        self.isbn_7 = QtWidgets.QLineEdit(self.page_2)
        self.isbn_7.setGeometry(QtCore.QRect(190, 60, 140, 30))
        self.isbn_7.setObjectName("isbn_7")
        self.isbn_8 = QtWidgets.QLineEdit(self.page_2)
        self.isbn_8.setGeometry(QtCore.QRect(190, 130, 140, 30))
        self.isbn_8.setObjectName("isbn_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(155, 230, 90, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_6.setGeometry(QtCore.QRect(60, 60, 110, 30))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 130, 110, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.toolBox.addItem(self.page_2, "")

        self.retranslateUi(borrow_return)
        self.toolBox.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.borrowButton)
        self.pushButton_3.clicked.connect(self.returnButton)
        self.msgBox0 = QMessageBox(QMessageBox.Information, "请输入图书isbn编号及用户证件号码", "请输入图书isbn编号及用户证件号码", QMessageBox.Ok)
        self.msgBox1 = QMessageBox(QMessageBox.Information, "插入失败", "未知错误", QMessageBox.Ok)
        self.msgBox2 = QMessageBox(QMessageBox.Information, "非法操作", "请输入书目ISBN码，用户证件号码，保证借出数目大于0", QMessageBox.Ok)
        self.msgBox_noUser = QMessageBox(QMessageBox.Information, "无该用户信息", "无该用户信息，请先创建用户，谢谢！", QMessageBox.Ok)
        self.msgBox_noBooks = QMessageBox(QMessageBox.Information, "无法借出", "库存为零，无法借出，谢谢！", QMessageBox.Ok)
        self.msgBox_borrowSucceed = QMessageBox(QMessageBox.Information, "借书成功", "借书成功！", QMessageBox.Ok)
        self.msgBox_noBorrowEvent = QMessageBox(QMessageBox.Information, "无该借书事件", "无该借书事件，无法还书！", QMessageBox.Ok)
        self.msgBox_returnSucceed = QMessageBox(QMessageBox.Information, "还书成功", "还书成功", QMessageBox.Ok)
        self.msgBox_debt = QMessageBox(QMessageBox.Information,"该用户欠款", "该用户欠款，需要支付违约金", QMessageBox.Ok)
        QtCore.QMetaObject.connectSlotsByName(borrow_return)

    def retranslateUi(self, borrow_return):
        _translate = QtCore.QCoreApplication.translate
        borrow_return.setWindowTitle(_translate("borrow_return", "借/还书管理"))
        self.textEdit.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">图书ISBN代码：</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">用户证件号码：</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">借书时长：</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">借出时间：</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">借出数目：</span></p></body></html>"))
        self.pushButton.setText(_translate("borrow_return", "确定"))
        self.comboBox.setItemText(0, _translate("borrow_return", "一个月"))
        self.comboBox.setItemText(1, _translate("borrow_return", "三个月"))
        self.comboBox.setItemText(2, _translate("borrow_return", "六个月"))
        self.comboBox.setItemText(3, _translate("borrow_return", "一年"))
        self.dateEdit.setDisplayFormat(_translate("borrow_return", "yyyy/M/d"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("borrow_return", "借出图书"))
        self.textBrowser_6.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">图书ISBN代码：</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("borrow_return", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">读者证件号码：</span></p></body></html>"))
        self.pushButton_3.setText(_translate("borrow_return", "确定"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("borrow_return", "归还图书"))

    def borrowButton(self):
        isbnCode = self.isbn_2.text()
        userId = self.isbn_3.text()
        borrowLength = self.borrowLenthChange(0, self.comboBox.currentText())
        borrowDate = self.dateEdit.date().toString(Qt.ISODate)
        borrowNum = self.spinBox.value()
        if (isbnCode==None or isbnCode=="" or userId==None or borrowNum==0):
            self.msgBox2.show()
        else:
            if (self.is_no_debt(userId)):
                try:
                    conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS', use_unicode=True, charset='utf8')
                    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                    sqlSelect = "select book_num from books_catalogue where isbn='%s';"%(isbnCode)
                    row = cur.execute(sqlSelect)
                    book_num_result = cur.fetchall()
                    book_num = book_num_result[0]['book_num']
                    if ((row == 1) & (book_num >0)):
                        sqlUpdate = "update books_catalogue set book_num=%d where isbn='%s';"%(book_num-borrowNum, isbnCode)
                        sqlInsert = "insert into borrowed(isbn, user_id, lease, bor_time, bor_num) values('%s', '%s', '%s', '%s', '%s');"%(isbnCode, userId, borrowLength, borrowDate, borrowNum)
                        cur.execute(sqlUpdate)
                        conn.commit()
                        cur.execute(sqlInsert)
                        conn.commit()
                        self.msgBox_borrowSucceed.show()
                        self.isbn_2.clear()
                        self.isbn_3.clear()
                        self.spinBox.setValue(0)
                    elif (row == 0 | book_num == 0):
                        self.msgBox_noBooks.show()
                    cur.close()
                    conn.close()
                except:
                    self.msgBox1.show()
                    self.isbn_2.clear()
                    self.isbn_3.clear()
                    self.spinBox.setValue(0)


    def returnButton(self):
        isbnCode = self.isbn_7.text()
        userId = self.isbn_8.text()
        if (isbnCode!=None or isbnCode!="" or userId!=None or userId!=""):
            try:
                conn = pymysql.connect(host='localhost', port=3306, user='libBooksManage', password='libBooksManage', \
                                       db='libMS', use_unicode=True, charset='utf8')
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                sqlSelect = "select * from borrowed where isbn='%s' and user_id='%s';"%(isbnCode, userId)
                searchResult = cur.execute(sqlSelect)
                if(searchResult != 0):
                    if(self.is_no_debt(userId) == False):
                        self.msgBox_debt.show()
                    try:
                        sqlSelectBooks = "select book_num from books_catalogue where isbn='%s';"%(isbnCode)
                        cur.execute(sqlSelectBooks)
                        bookNumResult = cur.fetchall()
                        bookNum = bookNumResult[0]['book_num']

                        sqlSelectBorrowedNum = "select bor_num from borrowed where isbn='%s' and user_id='%s'"%(isbnCode, userId)
                        cur.execute(sqlSelectBorrowedNum)
                        borrowedBookNumResult = cur.fetchall()
                        borrowedBookNum = borrowedBookNumResult[0]['bor_num']

                        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                        sqlUpdateBorrow = "update borrowed set return_time='%s' where user_id='%s' and isbn='%s';"%(today, userId, isbnCode)
                        cur.execute(sqlUpdateBorrow)
                        conn.commit()

                        sqlUpdateBook = "update books_catalogue set book_num='%s' where isbn='%s';"%((bookNum+borrowedBookNum), isbnCode)
                        cur.execute(sqlUpdateBook)
                        conn.commit()

                        self.msgBox_returnSucceed.show()
                        self.isbn_7.clear()
                        self.isbn_8.clear()
                    except:
                        self.msgBox1.show()

                else:
                    self.msgBox_noBorrowEvent.show()
            except:
                self.msgBox1.show()
        else:
            self.msgBox0.show()


    def borrowLenthChange(self, inform, length):
        dic_0 = {'一个月': '1', '三个月': '2', '六个月': '3', '一年': '4'}
        dic_1 = {'1': '一个月', '2': '三个月', '3': '六个月', '4': '一年'}
        if(inform == 0):
            return dic_0[length]
        if(inform == 1):
            return dic_1[length]
        else:
            self.msgBox1.show()

    def is_no_debt(self, userId):   #未欠款返回True
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='admin', db='libMS', use_unicode=True, charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sqlSelect = "select * from user_manage where user_id='%s';"%(userId)
        selec = cur.execute(sqlSelect)
        if(selec == 1):
            sqlBorrowSelect = "select * from borrowed where user_id='%s';"%(userId)
            rows = cur.execute(sqlBorrowSelect)
            if(rows==0):
                return True
            else:
                result = cur.fetchall()
                for i in range(rows):
                    lease = result[i]['lease']
                    borrow_time = result[i]['bor_time']
                    if(self.is_out_date(lease, borrow_time) == False):
                        return False
                return True
        else:
            self.msgBox_noUser.show()
            cur.close()
            conn.close()
            return False

    def is_out_date(self, lease, date): #超时返回False
        leaseList = {1:31, 2:93, 3:183, 4:366}
        now = datetime.date.today()
        leaseLength = (now-date).days
        if(leaseLength <= leaseList[int(lease)]):
            return True
        else:
            return False

