# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1101, 598)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/1/搜狗截图20221112194218.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 80, 111, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 80, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 111, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 130, 421, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 280, 101, 21))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(210, 280, 421, 211))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 510, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 430, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 510, 171, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 251, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 430, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 111, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 180, 421, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(710, 30, 361, 301))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 40, 461, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 230, 111, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 230, 421, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(720, 360, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(950, 360, 111, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 410, 111, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(650, 180, 37, 31))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 330, 111, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(270, 560, 631, 41))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.buttonsend)
        self.label_6.linkActivated['QString'].connect(self.label_6.setText)
        self.pushButton_5.clicked.connect(Form.savepass)
        self.pushButton_6.clicked.connect(Form.loadpass)
        self.pushButton_2.clicked.connect(Form.savedraft)
        self.pushButton_4.clicked.connect(Form.loaddraft)
        self.pushButton_3.clicked.connect(Form.clear)
        self.pushButton_8.clicked.connect(Form.sent)
        self.toolButton.clicked.connect(Form.contacts)
        self.pushButton_7.clicked.connect(Form.addcontacts)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton_3)
        Form.setTabOrder(self.pushButton_3, self.lineEdit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SMTP纵横天下"))
        self.label.setText(_translate("Form", "邮箱用户："))
        self.label_3.setText(_translate("Form", "你的密码："))
        self.label_4.setText(_translate("Form", "邮件内容："))
        self.pushButton.setText(_translate("Form", "发送"))
        self.pushButton_2.setText(_translate("Form", "保存草稿"))
        self.pushButton_3.setText(_translate("Form", "撤销"))
        self.label_2.setText(_translate("Form", "SMTP纵横天下"))
        self.pushButton_4.setText(_translate("Form", "载入草稿"))
        self.label_5.setText(_translate("Form", "发送地址："))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "邮件主题："))
        self.pushButton_5.setText(_translate("Form", "保存密码"))
        self.pushButton_6.setText(_translate("Form", "自动登录"))
        self.pushButton_8.setText(_translate("Form", "查看已发送"))
        self.toolButton.setText(_translate("Form", "+"))
        self.pushButton_7.setText(_translate("Form", "保存联系人"))
        self.label_8.setText(_translate("Form", "SMTP工作中······"))
import test_rc
