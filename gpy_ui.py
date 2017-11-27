# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
import sys
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
class Bubble(QtWidgets.QLabel):
    def __init__(self,text):
        super(Bubble,self).__init__(text)
        self.setContentsMargins(5,5,5,5)

    def paintEvent(self, e):

        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing,True)
        p.drawRoundedRect(0,0,self.width()-1,self.height()-1,5,5)

        super(Bubble,self).paintEvent(e)        

class MyWidget(QtWidgets.QWidget):

    def __init__(self,text,left=True):
        super(MyWidget,self).__init__()

        hbox = QtWidgets.QHBoxLayout()

        label = Bubble(text)

        if not left:
            hbox.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred))

        hbox.addWidget(label)

        if left:
            hbox.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred))            

        hbox.setContentsMargins(0,0,0,0)

        self.setLayout(hbox)
        self.setContentsMargins(0,0,0,0)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1210, 869)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(220, 199, 170);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.infoScrollLayout = QtWidgets.QVBoxLayout()
        self.infoScrollLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.infoScrollLayout.setObjectName("infoScrollLayout")
        self.infoScrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoScrollArea.sizePolicy().hasHeightForWidth())

        self.infoScrollArea.setSizePolicy(sizePolicy)
        self.infoScrollArea.setMinimumSize(QtCore.QSize(600, 845))
        self.infoScrollArea.setAutoFillBackground(True)
        self.infoScrollArea.setStyleSheet("background-color: rgb(107, 122, 143);")
        self.infoScrollArea.setWidgetResizable(True)
        self.infoScrollArea.setObjectName("infoScrollArea")
        self.infoScrollContents = QtWidgets.QWidget()
        self.infoScrollContents.setGeometry(QtCore.QRect(0, 0, 598, 843))
        self.infoScrollContents.setObjectName("infoScrollContents")
        self.infoScrollArea.setWidget(self.infoScrollContents)
        self.infoScrollLayout.addWidget(self.infoScrollArea)

        self.gridLayout.addLayout(self.infoScrollLayout, 0, 1, 1, 1)
        self.msgScrollLayout = QtWidgets.QVBoxLayout()
        self.msgScrollLayout.setObjectName("msgScrollLayout")
        self.msgScrollArea = QtWidgets.QScrollArea(Form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgScrollArea.sizePolicy().hasHeightForWidth())

        self.msgScrollArea.setSizePolicy(sizePolicy)
        self.msgScrollArea.setMinimumSize(QtCore.QSize(600, 845))
        self.msgScrollArea.setAutoFillBackground(True)
        self.msgScrollArea.setStyleSheet("background-color: rgb(247, 136, 47);")
        self.msgScrollArea.setWidgetResizable(True)
        self.msgScrollArea.setObjectName("msgScrollArea")
        self.msgScrollContents = QtWidgets.QWidget()
        self.msgScrollContents.setGeometry(QtCore.QRect(0, 0, 598, 843))
        self.msgScrollContents.setObjectName("msgScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.msgScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.msgLayout = QtWidgets.QVBoxLayout()
        self.msgLayout.setObjectName("msgLayout")
        self.verticalLayout_2.addLayout(self.msgLayout)
        self.msgScrollArea.setWidget(self.msgScrollContents)
        self.msgScrollLayout.addWidget(self.msgScrollArea)
        self.gridLayout.addLayout(self.msgScrollLayout, 0, 0, 1, 1)

        self.msgLayout.addWidget(MyWidget("Left side"))
        self.msgLayout.addWidget(MyWidget("Right side",left=False))
        self.msgLayout.addWidget(MyWidget("Left side"))
        self.msgLayout.addWidget(MyWidget("Left side"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GatorWatch"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_()) 
