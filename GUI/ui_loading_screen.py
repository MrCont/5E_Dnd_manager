# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading_screenRmXurd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Loading_screen(object):
    def setupUi(self, Loading_screen):
        if not Loading_screen.objectName():
            Loading_screen.setObjectName(u"Loading_screen")
        Loading_screen.setEnabled(False)
        Loading_screen.resize(800, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Loading_screen.sizePolicy().hasHeightForWidth())
        Loading_screen.setSizePolicy(sizePolicy)
        Loading_screen.setMinimumSize(QSize(800, 550))
        Loading_screen.setMaximumSize(QSize(800, 591))
        Loading_screen.setBaseSize(QSize(800, 550))
        font = QFont()
        font.setUnderline(False)
        Loading_screen.setFont(font)
        Loading_screen.setFocusPolicy(Qt.NoFocus)
        Loading_screen.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"")
        self.centralwidget = QWidget(Loading_screen)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 550))
        self.centralwidget.setMaximumSize(QSize(800, 550))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 550))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(38, 38, 38);\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(400, 230, 381, 101))
        font1 = QFont()
        font1.setFamily(u"Copperplate Gothic Light")
        font1.setPointSize(40)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(210, 490, 391, 23))
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"	border-style:none;\n"
"	border-radius: 10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-color: rgb(38, 38, 38);\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.54, stop:0 rgba(38, 38, 38, 255), stop:1 rgba(156, 156, 156, 255));\n"
"\n"
"}")
        self.progressBar.setValue(24)
        self.label_credits = QLabel(self.frame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(570, 10, 191, 21))
        font2 = QFont()
        font2.setFamily(u"Copperplate Gothic Light")
        font2.setPointSize(10)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"\n"
"color: rgb(156, 156, 156);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_loading = QLabel(self.frame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(320, 520, 171, 16))
        self.label_loading.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 441, 431))
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u"DnD_logo.png"))
        self.label.setScaledContents(True)
        self.progressBar.raise_()
        self.label_credits.raise_()
        self.label_loading.raise_()
        self.label.raise_()
        self.label_title.raise_()
        Loading_screen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Loading_screen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        Loading_screen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Loading_screen)
        self.statusbar.setObjectName(u"statusbar")
        Loading_screen.setStatusBar(self.statusbar)

        self.retranslateUi(Loading_screen)

        QMetaObject.connectSlotsByName(Loading_screen)
    # setupUi

    def retranslateUi(self, Loading_screen):
        Loading_screen.setWindowTitle("")
        self.label_title.setText(QCoreApplication.translate("Loading_screen", u"5E manager", None))
        self.label_credits.setText(QCoreApplication.translate("Loading_screen", u"<strong>Created by</strong>: Aron Contini", None))
        self.label_loading.setText(QCoreApplication.translate("Loading_screen", u"loading...", None))
        self.label.setText("")
    # retranslateUi

