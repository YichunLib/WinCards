# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Cygreenie\Desktop\WinCards\Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("JBRYXW Mono")
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("JBRYXW Mono")
        font.setBold(True)
        font.setWeight(75)
        self.btn_next.setFont(font)
        self.btn_next.setObjectName("btn_next")
        self.verticalLayout_2.addWidget(self.btn_next)
        self.txt_next = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.txt_next.setObjectName("txt_next")
        self.verticalLayout_2.addWidget(self.txt_next)
        self.btn_answer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("JBRYXW Mono")
        font.setBold(True)
        font.setWeight(75)
        self.btn_answer.setFont(font)
        self.btn_answer.setObjectName("btn_answer")
        self.verticalLayout_2.addWidget(self.btn_answer)
        self.txt_answer = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_answer.setObjectName("txt_answer")
        self.verticalLayout_2.addWidget(self.txt_answer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WinCards"))
        self.btn_next.setText(_translate("Form", "Next"))
        self.btn_answer.setText(_translate("Form", "Answer"))
