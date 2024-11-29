# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_cliente_and_chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQPushButton import QCustomQPushButton
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 818)
        MainWindow.setMinimumSize(QSize(0, 784))
        MainWindow.setMaximumSize(QSize(16777215, 818))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stackedWidget_2 = QCustomQStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 800))
        self.stackedWidget_2.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.stackedWidget_2.setFrameShape(QFrame.NoFrame)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_3 = QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(self.page_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: white;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.html_chat = QTextEdit(self.frame_4)
        self.html_chat.setObjectName(u"html_chat")
        self.html_chat.setMinimumSize(QSize(0, 547))
        self.html_chat.setMaximumSize(QSize(16777215, 16777215))
        self.html_chat.setStyleSheet(u"            QTextEdit {\n"
"          \n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"                font-family: Arial;\n"
"                font-size: 14px;\n"
"            }")

        self.gridLayout_4.addWidget(self.html_chat, 1, 4, 3, 6)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.close_window_button = QPushButton(self.frame_4)
        self.close_window_button.setObjectName(u"close_window_button")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon)

        self.gridLayout_14.addWidget(self.close_window_button, 0, 0, 1, 1)

        self.minimize_window_button = QPushButton(self.frame_4)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.gridLayout_14.addWidget(self.minimize_window_button, 0, 1, 1, 1)

        self.restore_window_button = QPushButton(self.frame_4)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(16, 16))

        self.gridLayout_14.addWidget(self.restore_window_button, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_14, 0, 9, 1, 1)

        self.pushButton_16 = QCustomQPushButton(self.frame_4)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_4.addWidget(self.pushButton_16, 0, 2, 1, 1)

        self.atach_file = QCustomQPushButton(self.frame_4)
        self.atach_file.setObjectName(u"atach_file")
        self.atach_file.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 13px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/file-arrow-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atach_file.setIcon(icon3)
        self.atach_file.setIconSize(QSize(22, 26))

        self.gridLayout_4.addWidget(self.atach_file, 5, 5, 1, 1)

        self.widget = QCustomSlideMenu(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 711))
        self.widget.setMaximumSize(QSize(16777215, 546))
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.view_threads = QCustomQPushButton(self.widget)
        self.view_threads.setObjectName(u"view_threads")
        self.view_threads.setMaximumSize(QSize(90, 30))
        self.view_threads.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_threads.setIcon(icon4)
        self.view_threads.setIconSize(QSize(24, 24))

        self.gridLayout_11.addWidget(self.view_threads, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.settings_agent = QCustomQPushButton(self.widget)
        self.settings_agent.setObjectName(u"settings_agent")
        self.settings_agent.setMinimumSize(QSize(90, 0))
        self.settings_agent.setMaximumSize(QSize(90, 30))
        self.settings_agent.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_agent.setIcon(icon5)
        self.settings_agent.setIconSize(QSize(24, 24))

        self.gridLayout_11.addWidget(self.settings_agent, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_11, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 1, 2, 1, 1)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 2, 1, 1, 2)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 5, 2)

        self.line_6 = QFrame(self.frame_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 0))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_6, 1, 3, 5, 1)

        self.send_mensage = QCustomQPushButton(self.frame_4)
        self.send_mensage.setObjectName(u"send_mensage")
        self.send_mensage.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_mensage.setIcon(icon6)
        self.send_mensage.setIconSize(QSize(27, 27))

        self.gridLayout_4.addWidget(self.send_mensage, 5, 8, 1, 1)

        self.pushButton_6 = QCustomQPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/mic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QSize(27, 27))

        self.gridLayout_4.addWidget(self.pushButton_6, 5, 9, 1, 1)

        self.mensage_input = QTextEdit(self.frame_4)
        self.mensage_input.setObjectName(u"mensage_input")
        self.mensage_input.setMinimumSize(QSize(0, 50))
        self.mensage_input.setMaximumSize(QSize(16777215, 16777215))
        self.mensage_input.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_4.addWidget(self.mensage_input, 5, 6, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 6, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 6, 6, 1, 1)

        self.html_chat.raise_()
        self.line_6.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.send_mensage.raise_()
        self.pushButton_6.raise_()
        self.widget.raise_()
        self.pushButton_16.raise_()
        self.atach_file.raise_()
        self.mensage_input.raise_()

        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout = QGridLayout(self.page_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.page_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: white;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_16.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.frame_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setFrameShape(QFrame.VLine)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 749, 745))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_295 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_295, 7, 0, 1, 1)

        self.vectorstore_in_agent = QTextEdit(self.scrollAreaWidgetContents_2)
        self.vectorstore_in_agent.setObjectName(u"vectorstore_in_agent")
        self.vectorstore_in_agent.setMinimumSize(QSize(0, 37))
        self.vectorstore_in_agent.setMaximumSize(QSize(16777215, 80))
        self.vectorstore_in_agent.setBaseSize(QSize(0, 0))
        self.vectorstore_in_agent.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.vectorstore_in_agent, 6, 2, 1, 1)

        self.label_289 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_289, 3, 0, 1, 1)

        self.instruct_agent = QTextEdit(self.scrollAreaWidgetContents_2)
        self.instruct_agent.setObjectName(u"instruct_agent")
        self.instruct_agent.setMinimumSize(QSize(0, 0))
        self.instruct_agent.setMaximumSize(QSize(16777215, 80))
        self.instruct_agent.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.instruct_agent, 0, 2, 1, 1)

        self.label_290 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_290, 5, 0, 1, 1)

        self.label_293 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_293.setObjectName(u"label_293")
        sizePolicy.setHeightForWidth(self.label_293.sizePolicy().hasHeightForWidth())
        self.label_293.setSizePolicy(sizePolicy)
        self.label_293.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_293, 4, 0, 1, 1)

        self.label_291 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_291, 1, 0, 1, 1)

        self.label_292 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_292, 2, 0, 1, 1)

        self.vectorstore_in_thread = QTextEdit(self.scrollAreaWidgetContents_2)
        self.vectorstore_in_thread.setObjectName(u"vectorstore_in_thread")
        self.vectorstore_in_thread.setMinimumSize(QSize(0, 37))
        self.vectorstore_in_thread.setMaximumSize(QSize(16777215, 80))
        self.vectorstore_in_thread.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.vectorstore_in_thread, 7, 2, 1, 1)

        self.label_294 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_294, 6, 0, 1, 1)

        self.label_296 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_296, 0, 0, 1, 1)

        self.tools_agent = QTextEdit(self.scrollAreaWidgetContents_2)
        self.tools_agent.setObjectName(u"tools_agent")
        self.tools_agent.setMinimumSize(QSize(0, 37))
        self.tools_agent.setMaximumSize(QSize(16777215, 80))
        self.tools_agent.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.tools_agent, 5, 2, 1, 1)

        self.name_agent = QLineEdit(self.scrollAreaWidgetContents_2)
        self.name_agent.setObjectName(u"name_agent")
        self.name_agent.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.name_agent, 2, 2, 1, 1)

        self.key_firebase_agent = QLineEdit(self.scrollAreaWidgetContents_2)
        self.key_firebase_agent.setObjectName(u"key_firebase_agent")
        self.key_firebase_agent.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.key_firebase_agent, 1, 2, 1, 1)

        self.model_agent = QLineEdit(self.scrollAreaWidgetContents_2)
        self.model_agent.setObjectName(u"model_agent")
        self.model_agent.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.model_agent, 3, 2, 1, 1)

        self.Upload_1file_in_message = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Upload_1file_in_message.setObjectName(u"Upload_1file_in_message")
        self.Upload_1file_in_message.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 4px;\n"
"                border-radius: 4px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.Upload_1file_in_message, 9, 2, 1, 1)

        self.addition_instruct = QLineEdit(self.scrollAreaWidgetContents_2)
        self.addition_instruct.setObjectName(u"addition_instruct")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addition_instruct.sizePolicy().hasHeightForWidth())
        self.addition_instruct.setSizePolicy(sizePolicy1)
        self.addition_instruct.setMinimumSize(QSize(0, 117))
        self.addition_instruct.setMaximumSize(QSize(16777215, 16777215))
        self.addition_instruct.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.addition_instruct, 4, 2, 1, 1)

        self.Upload_1file_in_thread = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Upload_1file_in_thread.setObjectName(u"Upload_1file_in_thread")
        self.Upload_1file_in_thread.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 4px;\n"
"                border-radius: 4px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.Upload_1file_in_thread, 8, 2, 1, 1)

        self.Upload_1image_for_vision_in_thread = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Upload_1image_for_vision_in_thread.setObjectName(u"Upload_1image_for_vision_in_thread")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Upload_1image_for_vision_in_thread.sizePolicy().hasHeightForWidth())
        self.Upload_1image_for_vision_in_thread.setSizePolicy(sizePolicy2)
        self.Upload_1image_for_vision_in_thread.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 4px;\n"
"                border-radius: 4px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.Upload_1image_for_vision_in_thread, 10, 2, 1, 1)

        self.label_297 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_297, 8, 0, 1, 1)

        self.label_299 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_299, 10, 0, 1, 1)

        self.label_298 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_298.setObjectName(u"label_298")
        self.label_298.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_8.addWidget(self.label_298, 9, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(0)
        self.checkBox_6 = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_15.addWidget(self.checkBox_6, 0, 6, 1, 1)

        self.checkBox_2 = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy3)
        self.checkBox_2.setMinimumSize(QSize(170, 0))
        self.checkBox_2.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_15.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.checkBox_4 = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_15.addWidget(self.checkBox_4, 0, 4, 1, 1)

        self.checkBox = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_15.addWidget(self.checkBox, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(11, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.checkBox_3 = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy2.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy2)

        self.gridLayout_15.addWidget(self.checkBox_3, 0, 2, 1, 1)

        self.checkBox_7 = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_15.addWidget(self.checkBox_7, 0, 7, 1, 1)

        self.checkBox_5 = QCustomCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_15.addWidget(self.checkBox_5, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(11, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 0, 8, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_15, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_16.addWidget(self.scrollArea_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_12 = QGridLayout(self.page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: white;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_15 = QPushButton(self.frame_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(0, 0, 721, 41))
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 340, 233, 163))
        self.frame_2.setMinimumSize(QSize(233, 0))
        self.frame_2.setStyleSheet(u"QWidget {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(11)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 5)
        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 10px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_11.setIconSize(QSize(19, 39))

        self.gridLayout_6.addWidget(self.pushButton_11, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_12.setIconSize(QSize(19, 39))

        self.gridLayout_6.addWidget(self.pushButton_12, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 10px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_13.setIconSize(QSize(19, 39))

        self.gridLayout_6.addWidget(self.pushButton_13, 3, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 10px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_14.setIconSize(QSize(19, 39))

        self.gridLayout_6.addWidget(self.pushButton_14, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 300, 233, 13))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #D8DEE9;\n"
"\n"
"    color: #111111;\n"
"\n"
"}")
        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 120, 233, 163))
        self.frame.setMinimumSize(QSize(226, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"QWidget {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(11)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 5)
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 10px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_8.setIconSize(QSize(19, 39))

        self.gridLayout_5.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_7.setIconSize(QSize(19, 39))

        self.gridLayout_5.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 10px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_10.setIconSize(QSize(19, 39))

        self.gridLayout_5.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"            QPushButton {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 10px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 10px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_9.setIconSize(QSize(19, 39))

        self.gridLayout_5.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 233, 13))
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setStyleSheet(u"QPushButton {\n"
"    background-color: #D8DEE9;\n"
"\n"
"    color: #111111;\n"
"\n"
"}")
        self.line_5 = QFrame(self.frame_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 320, 233, 3))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 233, 13))
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #D8DEE9;\n"
"\n"
"    color: #111111;\n"
"\n"
"}")
        self.layoutWidget = QWidget(self.frame_6)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(300, 60, 442, 71))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_279 = QLabel(self.layoutWidget)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setMinimumSize(QSize(217, 0))
        self.label_279.setMaximumSize(QSize(217, 16777215))
        self.label_279.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_2.addWidget(self.label_279, 3, 0, 1, 1)

        self.label_280 = QLabel(self.layoutWidget)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setMinimumSize(QSize(217, 0))
        self.label_280.setMaximumSize(QSize(217, 16777215))
        self.label_280.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_2.addWidget(self.label_280, 2, 0, 1, 1)

        self.label_282 = QLabel(self.layoutWidget)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setMinimumSize(QSize(217, 0))
        self.label_282.setMaximumSize(QSize(217, 16777215))
        self.label_282.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_2.addWidget(self.label_282, 7, 0, 1, 1)

        self.label_283 = QLabel(self.layoutWidget)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setMinimumSize(QSize(217, 0))
        self.label_283.setMaximumSize(QSize(217, 16777215))
        self.label_283.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_2.addWidget(self.label_283, 2, 1, 1, 1)

        self.label_281 = QLabel(self.layoutWidget)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setMinimumSize(QSize(217, 0))
        self.label_281.setMaximumSize(QSize(217, 16777215))
        self.label_281.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_2.addWidget(self.label_281, 3, 1, 1, 1)

        self.label_278 = QLabel(self.layoutWidget)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setMinimumSize(QSize(217, 0))
        self.label_278.setMaximumSize(QSize(217, 16777215))
        self.label_278.setStyleSheet(u"            QLabel {\n"
"                background-color: #F7F7F7;\n"
"                border: 1px solid #E0E0E0;\n"
"                border-radius: 9px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }")

        self.gridLayout_2.addWidget(self.label_278, 7, 1, 1, 1)

        self.line_7 = QFrame(self.frame_6)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(300, 220, 79, 3))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.frame_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(300, 229, 79, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(300, 238, 79, 3))
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_12.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page)

        self.gridLayout_9.addWidget(self.stackedWidget_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_window_button.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.atach_file.setText("")
        self.view_threads.setText("")
        self.settings_agent.setText("")
        self.send_mensage.setText("")
        self.pushButton_6.setText("")
        self.mensage_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mensagem...", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Back to home", None))
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"Vectorstore in Thread:", None))
        self.vectorstore_in_agent.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">None</span></p></body></html>", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"Model select:", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"tools:", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"Aditional instructions:", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"Nameassistant:", None))
        self.vectorstore_in_thread.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">None</span></p></body></html>", None))
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"Vectorstore in assistant:", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"Instruction:", None))
        self.tools_agent.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">None</span></p></body></html>", None))
        self.name_agent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AI ByteManager Donos da Empresa Urobotsoftware", None))
        self.key_firebase_agent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AI_ByteManager_Company_Owners", None))
        self.model_agent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gpt-4o-mini-2024-07-18", None))
        self.Upload_1file_in_message.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Upload_1file_in_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Local Path", None))
        self.addition_instruct.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.addition_instruct.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Upload_1file_in_thread.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Upload_1file_in_thread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Local Path", None))
        self.Upload_1image_for_vision_in_thread.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Upload_1image_for_vision_in_thread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Local Path", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"Upload 1 file in thread:", None))
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"Upload 1 image for vision in thread:", None))
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"Upload 1 file  in message:", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Voice onyx", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Voice Engine PC Voice", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Voice echo", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Voice Engine tts-1", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Voice alloy", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Voice nova", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Voice fable", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Back to home", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ontem:", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Thread: ...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hoje:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Threads:", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"Assistant Name: ", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Tools: ", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"File search:", None))
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"Code interpreter:", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"Vector storage:", None))
    # retranslateUi

