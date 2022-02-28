# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *


class TextEdit(object):
    def setupUi(self, TextEdit):
        """
        This function makes de graphical structure of the interface of our application
        
        Inputs:
            :TextEdit: QMainWindow
        

        
        """
        if not TextEdit.objectName():
            TextEdit.setObjectName(u"TextEdit")
        TextEdit.resize(675, 553)
        
        self.centralwidget = QWidget(TextEdit)
        self.centralwidget.setObjectName(u"centralwidget")
       # self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        #self.plainTextEdit.setObjectName(u"plainTextEdit")
        #self.plainTextEdit.setGeometry(QRect(0, 0, 675, 491))
        #self.plainTextEdit.setFocusPolicy(Qt.TabFocus)
        #TextEdit.setCentralWidget(self.centralwidget)
        #self.centralwidget = QWidget(TextEdit)
        #self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self._text_edit = QTextEdit(self.splitter)
        self._text_edit.setObjectName(u"_text_edit")
        self.splitter.addWidget(self._text_edit)
        self.preview = QWebEngineView(self.splitter)
        self.preview.setObjectName(u"preview")
        self.splitter.addWidget(self.preview)
        self.actionNew = QAction(TextEdit)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u"./assets/filenew.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(TextEdit)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u"./assets/fileopen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(TextEdit)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u"./assets/filesave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave_As = QAction(TextEdit)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon3 = QIcon()
        icon3.addFile(u"./assets/filesaveas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_As.setIcon(icon3)
        self.actionQuit =QAction(TextEdit)
        self.actionQuit.setObjectName("actionQuit")
        icon4 = QIcon()
        icon4.addFile(u"./assets/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionUndo = QAction(TextEdit)
        self.actionUndo.setObjectName(u"actionUndo")
        icon5 = QIcon()
        icon5.addFile(u"./assets/editundo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon5)
        self.actionRedo = QAction(TextEdit)
        self.actionRedo.setObjectName(u"actionRedo")
        icon6 = QIcon()
        icon6.addFile(u"./assets/editredo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon6)
        self.actionCut = QAction(TextEdit)
        self.actionCut.setObjectName(u"actionCut")
        icon7 = QIcon()
        icon7.addFile(u"./assets/editcut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCopy = QAction(TextEdit)
        self.actionCopy.setObjectName(u"actionCopy")
        icon8 = QIcon()
        icon8.addFile(u"./assets/editcopy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon8)
        self.actionPaste = QAction(TextEdit)
        self.actionPaste.setObjectName(u"actionPaste")
        icon9 = QIcon()
        icon9.addFile(u"./assets/editpaste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon9)
        self.actionAbout = QAction(TextEdit)
        self.actionAbout.setObjectName(u"actionAbout")
        
        
        self.undo = self._text_edit.undo

        self.horizontalLayout.addWidget(self.splitter)

        TextEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TextEdit)
        self.statusbar.setObjectName(u"statusbar")
        TextEdit.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(TextEdit)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 675, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        TextEdit.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(TextEdit)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setFocusPolicy(Qt.TabFocus)
        TextEdit.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)

        self.retranslateUi(TextEdit)

        QMetaObject.connectSlotsByName(TextEdit)
    # setupUi

    def retranslateUi(self, TextEdit):
        """
        This function gives the graphic names to the actions and the title of our interface and implements the internalizacion on them
                
        Inputs:
            :TextEdit: QMainWindow
        

        
        """    
        TextEdit.setWindowTitle(QApplication.translate("TextEdit", u"TextEdit", None))
        self.actionNew.setText(QApplication.translate("TextEdit", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QApplication.translate("TextEdit", u"Ctrl+N", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QApplication.translate("TextEdit", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QApplication.translate("TextEdit", u"Ctrl+O", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QApplication.translate("TextEdit", u"Save", None, -1))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QApplication.translate("TextEdit", u"Ctrl+S", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QApplication.translate("TextEdit", u"Save As...", None, -1))
        self.actionQuit.setText(QApplication.translate("TextEdit", u"Quit", None, -1))
        self.actionQuit.setShortcut(QApplication.translate("TextEdit", u"Ctrl+Q", None, -1))
        self.actionUndo.setText(QApplication.translate("TextEdit", u"Undo", None, -1))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QApplication.translate("TextEdit", u"Ctrl+Z", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QApplication.translate("TextEdit", u"Redo", None, -1))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QApplication.translate("TextEdit", u"Ctrl+Y", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QApplication.translate("TextEdit", u"Cut", None, -1))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QApplication.translate("TextEdit", u"Ctrl+X", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QApplication.translate("TextEdit", u"Copy", None, -1))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QApplication.translate("TextEdit", u"Ctrl+C", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QApplication.translate("TextEdit", u"Paste", None, -1))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QApplication.translate("TextEdit", u"Ctrl+V", None, -1))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QApplication.translate("TextEdit", u"About", None, -1))
        self.menuFile.setTitle(QApplication.translate("TextEdit", u"File", None, -1))
        self.menuEdit.setTitle(QApplication.translate("TextEdit", u"Edit", None, -1))
        self.menuHelp.setTitle(QApplication.translate("TextEdit", u"Help", None, -1))
        self.toolBar.setWindowTitle(QApplication.translate("TextEdit", u"toolBar", None, -1))
    # retranslateUi

