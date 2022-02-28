# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Index(object):
    def setupUi(self, Index):
        if not Index.objectName():
            Index.setObjectName(u"Index")
        Index.resize(720, 533)
        icon = QIcon()
        icon.addFile(u"./assets/favicon.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"./assets/favicon.png", QSize(), QIcon.Normal, QIcon.On)
        Index.setWindowIcon(icon)
        Index.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Index)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(Index)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.contentWidget = QWidget(self.backgroundFrame)
        self.contentWidget.setObjectName(u"contentWidget")
        self.contentWidget.setGeometry(QRect(250, 50, 231, 231))
        self.contentWidget.setStyleSheet(u"\n"
"image: url(./assets/logo.png);")
        self.Information = QPushButton(self.backgroundFrame)
        self.Information.setObjectName(u"Information")
        self.Information.setGeometry(QRect(250, 300, 231, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Information.setFont(font)
        self.Information.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(75, 132, 255);\n"
"color:white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(89, 178, 220);\n"
"}")
        self.newFile = QPushButton(self.backgroundFrame)
        self.newFile.setObjectName(u"newFile")
        self.newFile.setGeometry(QRect(250, 360, 231, 31))
        self.newFile.setFont(font)
        self.newFile.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(75, 132, 255);\n"
"color:white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(89, 178, 220);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/filenew.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newFile.setIcon(icon1)
        self.openFile = QPushButton(self.backgroundFrame)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(250, 420, 231, 31))
        self.openFile.setFont(font)
        self.openFile.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(75, 132, 255);\n"
"color:white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(89, 178, 220);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/fileopen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFile.setIcon(icon2)

        self.verticalLayout.addWidget(self.backgroundFrame)


        self.retranslateUi(Index)

        QMetaObject.connectSlotsByName(Index)
    # setupUi

    def retranslateUi(self, Index):
        Index.setWindowTitle(QCoreApplication.translate("Index", u"Index", None))
#if QT_CONFIG(whatsthis)
        self.contentWidget.setWhatsThis(QCoreApplication.translate("Index", u"<html><head/><body><p><img src=\":/assets/logo.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Information.setText(QCoreApplication.translate("Index", u"Information...", None))
        self.newFile.setText(QCoreApplication.translate("Index", u"New File", None))
        self.openFile.setText(QCoreApplication.translate("Index", u"Open File", None))
    # retranslateUi

