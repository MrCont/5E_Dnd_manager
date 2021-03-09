# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screenJpzxof.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DnD_manager(object):
    def setupUi(self, DnD_manager):
        if not DnD_manager.objectName():
            DnD_manager.setObjectName(u"DnD_manager")
        DnD_manager.resize(1170, 700)
        DnD_manager.setMinimumSize(QSize(900, 700))
        self.centralwidget = QWidget(DnD_manager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 700))
        self.centralwidget.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFocusPolicy(Qt.NoFocus)
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_all_menu = QFrame(self.frame_bottom)
        self.frame_all_menu.setObjectName(u"frame_all_menu")
        self.frame_all_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_all_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_all_menu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_left_bar = QFrame(self.frame_all_menu)
        self.frame_left_bar.setObjectName(u"frame_left_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_bar.sizePolicy().hasHeightForWidth())
        self.frame_left_bar.setSizePolicy(sizePolicy)
        self.frame_left_bar.setMinimumSize(QSize(120, 0))
        self.frame_left_bar.setMaximumSize(QSize(120, 16777215))
        self.frame_left_bar.setStyleSheet(u"background-color: rgb(63, 63, 63);\n"
"border-radius:10px;")
        self.frame_left_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_left_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_left_bar_new_game = QPushButton(self.frame_left_bar)
        self.pushButton_left_bar_new_game.setObjectName(u"pushButton_left_bar_new_game")
        self.pushButton_left_bar_new_game.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Copperplate Gothic Light")
        font.setPointSize(10)
        self.pushButton_left_bar_new_game.setFont(font)
        self.pushButton_left_bar_new_game.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_left_bar_new_game)

        self.pushButton_left_bar_load_game = QPushButton(self.frame_left_bar)
        self.pushButton_left_bar_load_game.setObjectName(u"pushButton_left_bar_load_game")
        self.pushButton_left_bar_load_game.setMinimumSize(QSize(0, 50))
        self.pushButton_left_bar_load_game.setFont(font)
        self.pushButton_left_bar_load_game.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_left_bar_load_game)

        self.pushButton_left_bar_save_game = QPushButton(self.frame_left_bar)
        self.pushButton_left_bar_save_game.setObjectName(u"pushButton_left_bar_save_game")
        self.pushButton_left_bar_save_game.setMinimumSize(QSize(0, 50))
        self.pushButton_left_bar_save_game.setFont(font)
        self.pushButton_left_bar_save_game.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_left_bar_save_game)

        self.pushButton_delete_game = QPushButton(self.frame_left_bar)
        self.pushButton_delete_game.setObjectName(u"pushButton_delete_game")
        self.pushButton_delete_game.setMinimumSize(QSize(0, 50))
        self.pushButton_delete_game.setFont(font)
        self.pushButton_delete_game.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_delete_game)

        self.pushButton_left_bar_add_player = QPushButton(self.frame_left_bar)
        self.pushButton_left_bar_add_player.setObjectName(u"pushButton_left_bar_add_player")
        self.pushButton_left_bar_add_player.setMinimumSize(QSize(0, 50))
        self.pushButton_left_bar_add_player.setFont(font)
        self.pushButton_left_bar_add_player.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_left_bar_add_player)

        self.pushButton_delete_player = QPushButton(self.frame_left_bar)
        self.pushButton_delete_player.setObjectName(u"pushButton_delete_player")
        self.pushButton_delete_player.setMinimumSize(QSize(0, 50))
        self.pushButton_delete_player.setFont(font)
        self.pushButton_delete_player.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_delete_player)

        self.pushButton_left_bar_export_pdf = QPushButton(self.frame_left_bar)
        self.pushButton_left_bar_export_pdf.setObjectName(u"pushButton_left_bar_export_pdf")
        self.pushButton_left_bar_export_pdf.setMinimumSize(QSize(0, 50))
        self.pushButton_left_bar_export_pdf.setFont(font)
        self.pushButton_left_bar_export_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_left_bar_export_pdf)

        self.pushButton_left_bar_current_game = QPushButton(self.frame_left_bar)
        self.pushButton_left_bar_current_game.setObjectName(u"pushButton_left_bar_current_game")
        self.pushButton_left_bar_current_game.setMinimumSize(QSize(0, 50))
        self.pushButton_left_bar_current_game.setFont(font)
        self.pushButton_left_bar_current_game.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_left_bar_current_game)

        self.label_left_bar_image = QLabel(self.frame_left_bar)
        self.label_left_bar_image.setObjectName(u"label_left_bar_image")
        self.label_left_bar_image.setMinimumSize(QSize(90, 90))
        self.label_left_bar_image.setMaximumSize(QSize(90, 90))
        self.label_left_bar_image.setStyleSheet(u"background-color: rgb(156, 156, 156);")
        self.label_left_bar_image.setPixmap(QPixmap(u"DnD_logo.png"))
        self.label_left_bar_image.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_left_bar_image, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_bar)

        self.frame_stack_and_label = QFrame(self.frame_all_menu)
        self.frame_stack_and_label.setObjectName(u"frame_stack_and_label")
        self.frame_stack_and_label.setFrameShape(QFrame.StyledPanel)
        self.frame_stack_and_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_stack_and_label)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_menus = QStackedWidget(self.frame_stack_and_label)
        self.stackedWidget_menus.setObjectName(u"stackedWidget_menus")
        self.stackedWidget_menus.setStyleSheet(u"border-radius:20px;")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.label_main_page_image = QLabel(self.page_main)
        self.label_main_page_image.setObjectName(u"label_main_page_image")
        self.label_main_page_image.setGeometry(QRect(70, 30, 501, 561))
        self.label_main_page_image.setPixmap(QPixmap(u"DnD_logo.png"))
        self.stackedWidget_menus.addWidget(self.page_main)
        self.page_new_adventure = QWidget()
        self.page_new_adventure.setObjectName(u"page_new_adventure")
        self.label_new_adventure = QLabel(self.page_new_adventure)
        self.label_new_adventure.setObjectName(u"label_new_adventure")
        self.label_new_adventure.setGeometry(QRect(30, 20, 291, 31))
        font1 = QFont()
        font1.setFamily(u"Copperplate Gothic Bold")
        font1.setPointSize(16)
        self.label_new_adventure.setFont(font1)
        self.label_new_adventure.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.gridLayoutWidget = QWidget(self.page_new_adventure)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 160, 511, 61))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.label_player_number = QLabel(self.gridLayoutWidget)
        self.label_player_number.setObjectName(u"label_player_number")
        font2 = QFont()
        font2.setFamily(u"Copperplate Gothic Light")
        font2.setPointSize(12)
        self.label_player_number.setFont(font2)
        self.label_player_number.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout.addWidget(self.label_player_number, 1, 0, 1, 1)

        self.label_adventure_name = QLabel(self.gridLayoutWidget)
        self.label_adventure_name.setObjectName(u"label_adventure_name")
        self.label_adventure_name.setFont(font2)
        self.label_adventure_name.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout.addWidget(self.label_adventure_name, 0, 0, 1, 1)

        self.lineEdit_adventure_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_adventure_name.setObjectName(u"lineEdit_adventure_name")
        self.lineEdit_adventure_name.setStyleSheet(u"\n"
"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout.addWidget(self.lineEdit_adventure_name, 0, 1, 1, 1)

        self.lineEdit_player_number = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_player_number.setObjectName(u"lineEdit_player_number")
        self.lineEdit_player_number.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout.addWidget(self.lineEdit_player_number, 1, 1, 1, 1)

        self.pushButton_create_adventure = QPushButton(self.page_new_adventure)
        self.pushButton_create_adventure.setObjectName(u"pushButton_create_adventure")
        self.pushButton_create_adventure.setGeometry(QRect(180, 540, 281, 50))
        self.pushButton_create_adventure.setMinimumSize(QSize(0, 50))
        self.pushButton_create_adventure.setFont(font)
        self.pushButton_create_adventure.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.stackedWidget_menus.addWidget(self.page_new_adventure)
        self.page_load_adventure = QWidget()
        self.page_load_adventure.setObjectName(u"page_load_adventure")
        self.label_load_adventure = QLabel(self.page_load_adventure)
        self.label_load_adventure.setObjectName(u"label_load_adventure")
        self.label_load_adventure.setGeometry(QRect(30, 20, 291, 31))
        self.label_load_adventure.setFont(font1)
        self.label_load_adventure.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.pushButton_load_adventure = QPushButton(self.page_load_adventure)
        self.pushButton_load_adventure.setObjectName(u"pushButton_load_adventure")
        self.pushButton_load_adventure.setGeometry(QRect(180, 540, 281, 50))
        self.pushButton_load_adventure.setMinimumSize(QSize(0, 50))
        self.pushButton_load_adventure.setFont(font)
        self.pushButton_load_adventure.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.gridLayoutWidget_2 = QWidget(self.page_load_adventure)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(60, 160, 511, 61))
        self.gridLayout_load_adventure = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_load_adventure.setObjectName(u"gridLayout_load_adventure")
        self.gridLayout_load_adventure.setHorizontalSpacing(30)
        self.gridLayout_load_adventure.setContentsMargins(3, 3, 3, 3)
        self.label_adventure_name_load = QLabel(self.gridLayoutWidget_2)
        self.label_adventure_name_load.setObjectName(u"label_adventure_name_load")
        self.label_adventure_name_load.setMaximumSize(QSize(142, 17))
        self.label_adventure_name_load.setFont(font2)
        self.label_adventure_name_load.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_load_adventure.addWidget(self.label_adventure_name_load, 1, 0, 1, 1)

        self.comboBox_adventure_name = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_adventure_name.setObjectName(u"comboBox_adventure_name")
        self.comboBox_adventure_name.setStyleSheet(u"background-color: rgb(63, 63, 63);")

        self.gridLayout_load_adventure.addWidget(self.comboBox_adventure_name, 1, 1, 1, 1)

        self.stackedWidget_menus.addWidget(self.page_load_adventure)
        self.page_delete_adventure = QWidget()
        self.page_delete_adventure.setObjectName(u"page_delete_adventure")
        self.label_delete_adventure = QLabel(self.page_delete_adventure)
        self.label_delete_adventure.setObjectName(u"label_delete_adventure")
        self.label_delete_adventure.setGeometry(QRect(30, 20, 291, 31))
        self.label_delete_adventure.setFont(font1)
        self.label_delete_adventure.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.label_warning_1 = QLabel(self.page_delete_adventure)
        self.label_warning_1.setObjectName(u"label_warning_1")
        self.label_warning_1.setGeometry(QRect(70, 180, 501, 31))
        self.label_warning_1.setFont(font2)
        self.label_warning_1.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.label_warning_2 = QLabel(self.page_delete_adventure)
        self.label_warning_2.setObjectName(u"label_warning_2")
        self.label_warning_2.setGeometry(QRect(200, 220, 221, 16))
        self.label_warning_2.setFont(font2)
        self.label_warning_2.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.pushButton_No = QPushButton(self.page_delete_adventure)
        self.pushButton_No.setObjectName(u"pushButton_No")
        self.pushButton_No.setGeometry(QRect(180, 540, 281, 50))
        self.pushButton_No.setMinimumSize(QSize(0, 50))
        self.pushButton_No.setFont(font)
        self.pushButton_No.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.pushButton_yes = QPushButton(self.page_delete_adventure)
        self.pushButton_yes.setObjectName(u"pushButton_yes")
        self.pushButton_yes.setGeometry(QRect(180, 480, 281, 50))
        self.pushButton_yes.setMinimumSize(QSize(0, 50))
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.stackedWidget_menus.addWidget(self.page_delete_adventure)
        self.page_add_player = QWidget()
        self.page_add_player.setObjectName(u"page_add_player")
        self.label_add_player = QLabel(self.page_add_player)
        self.label_add_player.setObjectName(u"label_add_player")
        self.label_add_player.setGeometry(QRect(30, 20, 291, 31))
        self.label_add_player.setFont(font1)
        self.label_add_player.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.gridLayoutWidget_3 = QWidget(self.page_add_player)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(60, 150, 511, 253))
        self.gridLayout_add_player = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_add_player.setObjectName(u"gridLayout_add_player")
        self.gridLayout_add_player.setHorizontalSpacing(30)
        self.gridLayout_add_player.setContentsMargins(3, 3, 3, 3)
        self.label_player_name = QLabel(self.gridLayoutWidget_3)
        self.label_player_name.setObjectName(u"label_player_name")
        self.label_player_name.setFont(font2)
        self.label_player_name.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_player_name, 0, 0, 1, 1)

        self.lineEdit_character_name = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_character_name.setObjectName(u"lineEdit_character_name")
        self.lineEdit_character_name.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_character_name, 1, 1, 1, 1)

        self.label_class = QLabel(self.gridLayoutWidget_3)
        self.label_class.setObjectName(u"label_class")
        self.label_class.setFont(font2)
        self.label_class.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_class, 3, 0, 1, 1)

        self.comboBox_class = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_class.setObjectName(u"comboBox_class")
        self.comboBox_class.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.comboBox_class, 3, 1, 1, 1)

        self.comboBox_alignment = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_alignment.setObjectName(u"comboBox_alignment")
        self.comboBox_alignment.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.comboBox_alignment, 4, 1, 1, 1)

        self.label_race = QLabel(self.gridLayoutWidget_3)
        self.label_race.setObjectName(u"label_race")
        self.label_race.setFont(font2)
        self.label_race.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_race, 2, 0, 1, 1)

        self.lineEdit_player_name = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_player_name.setObjectName(u"lineEdit_player_name")
        self.lineEdit_player_name.setStyleSheet(u"\n"
"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_player_name, 0, 1, 1, 1)

        self.label_character_name = QLabel(self.gridLayoutWidget_3)
        self.label_character_name.setObjectName(u"label_character_name")
        self.label_character_name.setFont(font2)
        self.label_character_name.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_character_name, 1, 0, 1, 1)

        self.lineEdit_dexterity = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_dexterity.setObjectName(u"lineEdit_dexterity")
        self.lineEdit_dexterity.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_dexterity, 6, 1, 1, 1)

        self.lineEdit_strength = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_strength.setObjectName(u"lineEdit_strength")
        self.lineEdit_strength.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_strength, 5, 1, 1, 1)

        self.label_alignment = QLabel(self.gridLayoutWidget_3)
        self.label_alignment.setObjectName(u"label_alignment")
        self.label_alignment.setFont(font2)
        self.label_alignment.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_alignment, 4, 0, 1, 1)

        self.label_charisma = QLabel(self.gridLayoutWidget_3)
        self.label_charisma.setObjectName(u"label_charisma")
        self.label_charisma.setFont(font2)
        self.label_charisma.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_charisma, 10, 0, 1, 1)

        self.comboBox_race = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_race.setObjectName(u"comboBox_race")
        self.comboBox_race.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.comboBox_race, 2, 1, 1, 1)

        self.label_strength = QLabel(self.gridLayoutWidget_3)
        self.label_strength.setObjectName(u"label_strength")
        self.label_strength.setFont(font2)
        self.label_strength.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_strength, 5, 0, 1, 1)

        self.label_wisdom = QLabel(self.gridLayoutWidget_3)
        self.label_wisdom.setObjectName(u"label_wisdom")
        self.label_wisdom.setFont(font2)
        self.label_wisdom.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_wisdom, 9, 0, 1, 1)

        self.label_dexterity = QLabel(self.gridLayoutWidget_3)
        self.label_dexterity.setObjectName(u"label_dexterity")
        self.label_dexterity.setFont(font2)
        self.label_dexterity.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_dexterity, 6, 0, 1, 1)

        self.label_constitution = QLabel(self.gridLayoutWidget_3)
        self.label_constitution.setObjectName(u"label_constitution")
        self.label_constitution.setFont(font2)
        self.label_constitution.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_constitution, 7, 0, 1, 1)

        self.label_intelligence = QLabel(self.gridLayoutWidget_3)
        self.label_intelligence.setObjectName(u"label_intelligence")
        self.label_intelligence.setFont(font2)
        self.label_intelligence.setStyleSheet(u"color: rgb(156, 156, 156);")

        self.gridLayout_add_player.addWidget(self.label_intelligence, 8, 0, 1, 1)

        self.lineEdit_constitution = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_constitution.setObjectName(u"lineEdit_constitution")
        self.lineEdit_constitution.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_constitution, 7, 1, 1, 1)

        self.lineEdit_intelligence = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_intelligence.setObjectName(u"lineEdit_intelligence")
        self.lineEdit_intelligence.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_intelligence, 8, 1, 1, 1)

        self.lineEdit_wisdom = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_wisdom.setObjectName(u"lineEdit_wisdom")
        self.lineEdit_wisdom.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_wisdom, 9, 1, 1, 1)

        self.lineEdit_charisma = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_charisma.setObjectName(u"lineEdit_charisma")
        self.lineEdit_charisma.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"background-color: rgb(63, 63, 63);")

        self.gridLayout_add_player.addWidget(self.lineEdit_charisma, 10, 1, 1, 1)

        self.pushButton_add_player = QPushButton(self.page_add_player)
        self.pushButton_add_player.setObjectName(u"pushButton_add_player")
        self.pushButton_add_player.setGeometry(QRect(170, 520, 281, 50))
        self.pushButton_add_player.setMinimumSize(QSize(0, 50))
        self.pushButton_add_player.setFont(font)
        self.pushButton_add_player.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.pushButton_alternative_add = QPushButton(self.page_add_player)
        self.pushButton_alternative_add.setObjectName(u"pushButton_alternative_add")
        self.pushButton_alternative_add.setGeometry(QRect(140, 580, 341, 50))
        self.pushButton_alternative_add.setMinimumSize(QSize(0, 50))
        self.pushButton_alternative_add.setFont(font)
        self.pushButton_alternative_add.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.stackedWidget_menus.addWidget(self.page_add_player)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_23 = QLabel(self.page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(70, 30, 501, 561))
        self.label_23.setPixmap(QPixmap(u"DnD_logo.png"))
        self.stackedWidget_menus.addWidget(self.page)

        self.horizontalLayout_3.addWidget(self.stackedWidget_menus)

        self.label_display = QLabel(self.frame_stack_and_label)
        self.label_display.setObjectName(u"label_display")
        self.label_display.setMinimumSize(QSize(350, 0))
        self.label_display.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Copperplate Gothic Bold")
        font3.setPointSize(10)
        self.label_display.setFont(font3)
        self.label_display.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_display.setStyleSheet(u"background-color: rgb(156, 156, 156);\n"
"color: rgb(38, 38, 38);\n"
"border-radius:10px;")
        self.label_display.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_display.setTextFormat(Qt.AutoText)
        self.label_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_display.setMargin(10)
        self.label_display.setOpenExternalLinks(False)
        self.label_display.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_display)


        self.horizontalLayout_2.addWidget(self.frame_stack_and_label)

        self.frame_stack_and_label.raise_()
        self.frame_left_bar.raise_()

        self.horizontalLayout.addWidget(self.frame_all_menu)


        self.verticalLayout.addWidget(self.frame_bottom)

        DnD_manager.setCentralWidget(self.centralwidget)

        self.retranslateUi(DnD_manager)

        self.stackedWidget_menus.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(DnD_manager)
    # setupUi

    def retranslateUi(self, DnD_manager):
        DnD_manager.setWindowTitle(QCoreApplication.translate("DnD_manager", u"5E DnD Manager", None))
        self.pushButton_left_bar_new_game.setText(QCoreApplication.translate("DnD_manager", u"New Game", None))
        self.pushButton_left_bar_load_game.setText(QCoreApplication.translate("DnD_manager", u"Load Game", None))
        self.pushButton_left_bar_save_game.setText(QCoreApplication.translate("DnD_manager", u"Save Game", None))
        self.pushButton_delete_game.setText(QCoreApplication.translate("DnD_manager", u"Delete Game", None))
        self.pushButton_left_bar_add_player.setText(QCoreApplication.translate("DnD_manager", u"Add Player", None))
        self.pushButton_delete_player.setText(QCoreApplication.translate("DnD_manager", u"Delete Player", None))
        self.pushButton_left_bar_export_pdf.setText(QCoreApplication.translate("DnD_manager", u"Export PDF", None))
        self.pushButton_left_bar_current_game.setText(QCoreApplication.translate("DnD_manager", u"Current Game", None))
        self.label_left_bar_image.setText("")
        self.label_main_page_image.setText("")
        self.label_new_adventure.setText(QCoreApplication.translate("DnD_manager", u"New Adventure", None))
        self.label_player_number.setText(QCoreApplication.translate("DnD_manager", u"Player Number", None))
        self.label_adventure_name.setText(QCoreApplication.translate("DnD_manager", u"Adventure Name", None))
        self.pushButton_create_adventure.setText(QCoreApplication.translate("DnD_manager", u"Create Adventure", None))
        self.label_load_adventure.setText(QCoreApplication.translate("DnD_manager", u"Load Adventure", None))
        self.pushButton_load_adventure.setText(QCoreApplication.translate("DnD_manager", u"Load Adventure", None))
        self.label_adventure_name_load.setText(QCoreApplication.translate("DnD_manager", u"Adventure Name", None))
        self.label_delete_adventure.setText(QCoreApplication.translate("DnD_manager", u"Delete Adventure", None))
        self.label_warning_1.setText(QCoreApplication.translate("DnD_manager", u"current game and progress will be deleted irreversibly", None))
        self.label_warning_2.setText(QCoreApplication.translate("DnD_manager", u"still u want to proceed?", None))
        self.pushButton_No.setText(QCoreApplication.translate("DnD_manager", u"No", None))
        self.pushButton_yes.setText(QCoreApplication.translate("DnD_manager", u"Yes", None))
        self.label_add_player.setText(QCoreApplication.translate("DnD_manager", u"Add Player", None))
        self.label_player_name.setText(QCoreApplication.translate("DnD_manager", u"Player Name", None))
        self.label_class.setText(QCoreApplication.translate("DnD_manager", u"Class", None))
        self.label_race.setText(QCoreApplication.translate("DnD_manager", u" Race", None))
        self.label_character_name.setText(QCoreApplication.translate("DnD_manager", u"Character Name", None))
        self.label_alignment.setText(QCoreApplication.translate("DnD_manager", u"Alignment", None))
        self.label_charisma.setText(QCoreApplication.translate("DnD_manager", u"Charisma", None))
        self.label_strength.setText(QCoreApplication.translate("DnD_manager", u"Strength", None))
        self.label_wisdom.setText(QCoreApplication.translate("DnD_manager", u"Wisdom", None))
        self.label_dexterity.setText(QCoreApplication.translate("DnD_manager", u"Dexterity", None))
        self.label_constitution.setText(QCoreApplication.translate("DnD_manager", u"Constitution", None))
        self.label_intelligence.setText(QCoreApplication.translate("DnD_manager", u"Intelligence", None))
        self.pushButton_add_player.setText(QCoreApplication.translate("DnD_manager", u"Add Player", None))
        self.pushButton_alternative_add.setText(QCoreApplication.translate("DnD_manager", u"Add Player and go back to Adventure menu", None))
        self.label_23.setText("")
        self.label_display.setText(QCoreApplication.translate("DnD_manager", u"TEST TEXT", None))
    # retranslateUi

