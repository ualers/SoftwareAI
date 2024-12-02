# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
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
        MainWindow.resize(781, 607)
        MainWindow.setMinimumSize(QSize(781, 502))
        MainWindow.setStyleSheet(u"background:white")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.open_close_side_bar_btn = QCustomQPushButton(self.centralwidget)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_close_side_bar_btn.sizePolicy().hasHeightForWidth())
        self.open_close_side_bar_btn.setSizePolicy(sizePolicy)
        self.open_close_side_bar_btn.setMinimumSize(QSize(35, 0))
        self.open_close_side_bar_btn.setMaximumSize(QSize(35, 16777215))
        self.open_close_side_bar_btn.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/arrow_back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(29, 29))

        self.gridLayout.addWidget(self.open_close_side_bar_btn, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(580, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.close_window_button = QPushButton(self.centralwidget)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon1)
        self.close_window_button.setIconSize(QSize(21, 24))

        self.gridLayout_2.addWidget(self.close_window_button, 0, 3, 1, 1)

        self.restore_window_button = QPushButton(self.centralwidget)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(21, 24))

        self.gridLayout_2.addWidget(self.restore_window_button, 0, 2, 1, 1)

        self.minimize_window_button = QPushButton(self.centralwidget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon3)
        self.minimize_window_button.setIconSize(QSize(21, 24))

        self.gridLayout_2.addWidget(self.minimize_window_button, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)

        self.menu_widget = QCustomSlideMenu(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_widget.sizePolicy().hasHeightForWidth())
        self.menu_widget.setSizePolicy(sizePolicy1)
        self.menu_widget.setMinimumSize(QSize(39, 0))
        self.menu_widget.setMaximumSize(QSize(39, 16777215))
        self.verticalLayout = QVBoxLayout(self.menu_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CreateAgents_menu = QPushButton(self.menu_widget)
        self.CreateAgents_menu.setObjectName(u"CreateAgents_menu")
        self.CreateAgents_menu.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/people_alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CreateAgents_menu.setIcon(icon4)
        self.CreateAgents_menu.setIconSize(QSize(24, 26))

        self.verticalLayout.addWidget(self.CreateAgents_menu)

        self.Editor_instructions = QPushButton(self.menu_widget)
        self.Editor_instructions.setObjectName(u"Editor_instructions")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Editor_instructions.sizePolicy().hasHeightForWidth())
        self.Editor_instructions.setSizePolicy(sizePolicy2)
        self.Editor_instructions.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/integration_instructions.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Editor_instructions.setIcon(icon5)
        self.Editor_instructions.setIconSize(QSize(24, 27))

        self.verticalLayout.addWidget(self.Editor_instructions)

        self.Editor_functions = QPushButton(self.menu_widget)
        self.Editor_functions.setObjectName(u"Editor_functions")
        sizePolicy2.setHeightForWidth(self.Editor_functions.sizePolicy().hasHeightForWidth())
        self.Editor_functions.setSizePolicy(sizePolicy2)
        self.Editor_functions.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/settings_suggest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Editor_functions.setIcon(icon6)
        self.Editor_functions.setIconSize(QSize(24, 27))

        self.verticalLayout.addWidget(self.Editor_functions)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.menu_widget, 2, 0, 1, 1)

        self.myStackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.myStackedWidget.setObjectName(u"myStackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.myStackedWidget.sizePolicy().hasHeightForWidth())
        self.myStackedWidget.setSizePolicy(sizePolicy3)
        self.myStackedWidget.setMinimumSize(QSize(650, 400))
        self.myStackedWidget.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: white;\n"
"}\n"
"")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.html_chat_3 = QTextEdit(self.page_2)
        self.html_chat_3.setObjectName(u"html_chat_3")
        self.html_chat_3.setMinimumSize(QSize(0, 246))
        self.html_chat_3.setMaximumSize(QSize(16777215, 16777215))
        self.html_chat_3.setStyleSheet(u"            QTextEdit {\n"
"          \n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"                font-family: Arial;\n"
"                font-size: 14px;\n"
"            }")

        self.gridLayout_4.addWidget(self.html_chat_3, 3, 0, 2, 2)

        self.comboBox = QComboBox(self.page_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.comboBox, 2, 1, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(6)
        self.gridLayout_22.setContentsMargins(-1, -1, 11, -1)
        self.mensage_input_2 = QTextEdit(self.page_2)
        self.mensage_input_2.setObjectName(u"mensage_input_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mensage_input_2.sizePolicy().hasHeightForWidth())
        self.mensage_input_2.setSizePolicy(sizePolicy4)
        self.mensage_input_2.setMinimumSize(QSize(694, 52))
        self.mensage_input_2.setMaximumSize(QSize(685, 16777215))
        self.mensage_input_2.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_22.addWidget(self.mensage_input_2, 0, 1, 1, 1)

        self.send_mensage_2 = QCustomQPushButton(self.page_2)
        self.send_mensage_2.setObjectName(u"send_mensage_2")
        sizePolicy.setHeightForWidth(self.send_mensage_2.sizePolicy().hasHeightForWidth())
        self.send_mensage_2.setSizePolicy(sizePolicy)
        self.send_mensage_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_mensage_2.setIcon(icon7)
        self.send_mensage_2.setIconSize(QSize(40, 41))

        self.gridLayout_22.addWidget(self.send_mensage_2, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_22, 6, 0, 1, 2)

        self.myStackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget_instruction = QCustomQStackedWidget(self.page)
        self.stackedWidget_instruction.setObjectName(u"stackedWidget_instruction")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_list_instruction_edit = QComboBox(self.page_3)
        self.comboBox_list_instruction_edit.setObjectName(u"comboBox_list_instruction_edit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_list_instruction_edit.sizePolicy().hasHeightForWidth())
        self.comboBox_list_instruction_edit.setSizePolicy(sizePolicy5)
        self.comboBox_list_instruction_edit.setMinimumSize(QSize(571, 0))
        self.comboBox_list_instruction_edit.setMaximumSize(QSize(571, 16777215))
        self.comboBox_list_instruction_edit.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.comboBox_list_instruction_edit, 0, 2, 1, 1)

        self.Current_instuction_html_edit = QTextEdit(self.page_3)
        self.Current_instuction_html_edit.setObjectName(u"Current_instuction_html_edit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Current_instuction_html_edit.sizePolicy().hasHeightForWidth())
        self.Current_instuction_html_edit.setSizePolicy(sizePolicy6)
        self.Current_instuction_html_edit.setMinimumSize(QSize(0, 0))
        self.Current_instuction_html_edit.setMaximumSize(QSize(16777215, 16777215))
        self.Current_instuction_html_edit.setStyleSheet(u"            QTextEdit {\n"
"          \n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"                font-family: Arial;\n"
"                font-size: 14px;\n"
"            }")

        self.gridLayout_3.addWidget(self.Current_instuction_html_edit, 1, 0, 1, 4)

        self.Add_new_instructions_button_edit = QCustomQPushButton(self.page_3)
        self.Add_new_instructions_button_edit.setObjectName(u"Add_new_instructions_button_edit")
        sizePolicy3.setHeightForWidth(self.Add_new_instructions_button_edit.sizePolicy().hasHeightForWidth())
        self.Add_new_instructions_button_edit.setSizePolicy(sizePolicy3)
        self.Add_new_instructions_button_edit.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Add_new_instructions_button_edit.setIcon(icon8)
        self.Add_new_instructions_button_edit.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.Add_new_instructions_button_edit, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setIndent(10)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setVerticalSpacing(9)
        self.gridLayout_8.setContentsMargins(-1, 9, 9, 1)
        self.instruction_input_edit = QTextEdit(self.page_3)
        self.instruction_input_edit.setObjectName(u"instruction_input_edit")
        sizePolicy4.setHeightForWidth(self.instruction_input_edit.sizePolicy().hasHeightForWidth())
        self.instruction_input_edit.setSizePolicy(sizePolicy4)
        self.instruction_input_edit.setMinimumSize(QSize(676, 52))
        self.instruction_input_edit.setMaximumSize(QSize(676, 52))
        self.instruction_input_edit.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_8.addWidget(self.instruction_input_edit, 1, 2, 1, 1)

        self.change_instruction_button_edit = QCustomQPushButton(self.page_3)
        self.change_instruction_button_edit.setObjectName(u"change_instruction_button_edit")
        sizePolicy.setHeightForWidth(self.change_instruction_button_edit.sizePolicy().hasHeightForWidth())
        self.change_instruction_button_edit.setSizePolicy(sizePolicy)
        self.change_instruction_button_edit.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/edit_note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change_instruction_button_edit.setIcon(icon9)
        self.change_instruction_button_edit.setIconSize(QSize(40, 47))

        self.gridLayout_8.addWidget(self.change_instruction_button_edit, 1, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_8, 3, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.stackedWidget_instruction.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_9 = QGridLayout(self.page_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(2)
        self.label_3 = QLabel(self.page_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_list_agent_for_create_instruction_create = QComboBox(self.page_4)
        self.comboBox_list_agent_for_create_instruction_create.setObjectName(u"comboBox_list_agent_for_create_instruction_create")
        sizePolicy.setHeightForWidth(self.comboBox_list_agent_for_create_instruction_create.sizePolicy().hasHeightForWidth())
        self.comboBox_list_agent_for_create_instruction_create.setSizePolicy(sizePolicy)
        self.comboBox_list_agent_for_create_instruction_create.setMinimumSize(QSize(172, 0))
        self.comboBox_list_agent_for_create_instruction_create.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.comboBox_list_agent_for_create_instruction_create, 1, 3, 1, 1)

        self.NameForInstruction_create = QLineEdit(self.page_4)
        self.NameForInstruction_create.setObjectName(u"NameForInstruction_create")
        sizePolicy.setHeightForWidth(self.NameForInstruction_create.sizePolicy().hasHeightForWidth())
        self.NameForInstruction_create.setSizePolicy(sizePolicy)
        self.NameForInstruction_create.setMinimumSize(QSize(172, 0))
        self.NameForInstruction_create.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.NameForInstruction_create, 1, 0, 1, 1)

        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setIndent(34)

        self.gridLayout_6.addWidget(self.label_4, 0, 3, 1, 1)

        self.comboBox_category_instruction_create = QComboBox(self.page_4)
        self.comboBox_category_instruction_create.setObjectName(u"comboBox_category_instruction_create")
        self.comboBox_category_instruction_create.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.comboBox_category_instruction_create, 1, 1, 1, 2)

        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setIndent(113)

        self.gridLayout_6.addWidget(self.label_5, 0, 1, 1, 2)


        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 271, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 1, 0, 1, 2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(6)
        self.BacktoEditinstruction_create = QCustomQPushButton(self.page_4)
        self.BacktoEditinstruction_create.setObjectName(u"BacktoEditinstruction_create")
        sizePolicy3.setHeightForWidth(self.BacktoEditinstruction_create.sizePolicy().hasHeightForWidth())
        self.BacktoEditinstruction_create.setSizePolicy(sizePolicy3)
        self.BacktoEditinstruction_create.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/material_design/icons/material_design/keyboard_backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BacktoEditinstruction_create.setIcon(icon10)
        self.BacktoEditinstruction_create.setIconSize(QSize(27, 27))

        self.gridLayout_7.addWidget(self.BacktoEditinstruction_create, 0, 0, 1, 1)

        self.New_instruction_html_create = QTextEdit(self.page_4)
        self.New_instruction_html_create.setObjectName(u"New_instruction_html_create")
        sizePolicy4.setHeightForWidth(self.New_instruction_html_create.sizePolicy().hasHeightForWidth())
        self.New_instruction_html_create.setSizePolicy(sizePolicy4)
        self.New_instruction_html_create.setMinimumSize(QSize(641, 45))
        self.New_instruction_html_create.setMaximumSize(QSize(641, 45))
        self.New_instruction_html_create.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_7.addWidget(self.New_instruction_html_create, 0, 2, 1, 1)

        self.CreateInstructionbutton_create = QCustomQPushButton(self.page_4)
        self.CreateInstructionbutton_create.setObjectName(u"CreateInstructionbutton_create")
        sizePolicy.setHeightForWidth(self.CreateInstructionbutton_create.sizePolicy().hasHeightForWidth())
        self.CreateInstructionbutton_create.setSizePolicy(sizePolicy)
        self.CreateInstructionbutton_create.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/material_design/icons/material_design/create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CreateInstructionbutton_create.setIcon(icon11)
        self.CreateInstructionbutton_create.setIconSize(QSize(37, 41))

        self.gridLayout_7.addWidget(self.CreateInstructionbutton_create, 0, 3, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_7, 2, 0, 1, 2)

        self.stackedWidget_instruction.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget_instruction, 0, 0, 1, 1)

        self.myStackedWidget.addWidget(self.page)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.gridLayout_17 = QGridLayout(self.page_settings)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.stackedWidget_SettingsCreate = QCustomQStackedWidget(self.page_settings)
        self.stackedWidget_SettingsCreate.setObjectName(u"stackedWidget_SettingsCreate")
        sizePolicy3.setHeightForWidth(self.stackedWidget_SettingsCreate.sizePolicy().hasHeightForWidth())
        self.stackedWidget_SettingsCreate.setSizePolicy(sizePolicy3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_10 = QGridLayout(self.page_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_3 = QGroupBox(self.page_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.gridLayout_16 = QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(33)
        self.gridLayout_15.setVerticalSpacing(15)
        self.gridLayout_15.setContentsMargins(6, 1, 8, 5)
        self.InstructionSettings = QPushButton(self.groupBox_3)
        self.InstructionSettings.setObjectName(u"InstructionSettings")
        self.InstructionSettings.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/material_design/icons/material_design/person_pin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.InstructionSettings.setIcon(icon12)
        self.InstructionSettings.setIconSize(QSize(18, 18))

        self.gridLayout_15.addWidget(self.InstructionSettings, 5, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_15.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1, 1)

        self.PromptSettings = QPushButton(self.groupBox_3)
        self.PromptSettings.setObjectName(u"PromptSettings")
        font = QFont()
        self.PromptSettings.setFont(font)
        self.PromptSettings.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/material_design/icons/material_design/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PromptSettings.setIcon(icon13)
        self.PromptSettings.setIconSize(QSize(15, 18))

        self.gridLayout_15.addWidget(self.PromptSettings, 4, 0, 1, 2)

        self.AgentCategory = QComboBox(self.groupBox_3)
        self.AgentCategory.setObjectName(u"AgentCategory")
        sizePolicy.setHeightForWidth(self.AgentCategory.sizePolicy().hasHeightForWidth())
        self.AgentCategory.setSizePolicy(sizePolicy)
        self.AgentCategory.setMinimumSize(QSize(190, 23))
        self.AgentCategory.setMaximumSize(QSize(190, 23))
        self.AgentCategory.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 5px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 12px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.AgentCategory, 3, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_15.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_15.addWidget(self.label_7, 1, 0, 1, 1)

        self.NameAgent = QTextEdit(self.groupBox_3)
        self.NameAgent.setObjectName(u"NameAgent")
        sizePolicy.setHeightForWidth(self.NameAgent.sizePolicy().hasHeightForWidth())
        self.NameAgent.setSizePolicy(sizePolicy)
        self.NameAgent.setMinimumSize(QSize(190, 29))
        self.NameAgent.setMaximumSize(QSize(190, 29))
        self.NameAgent.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 2px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_15.addWidget(self.NameAgent, 1, 1, 1, 1)

        self.KeyInFirebase = QTextEdit(self.groupBox_3)
        self.KeyInFirebase.setObjectName(u"KeyInFirebase")
        sizePolicy.setHeightForWidth(self.KeyInFirebase.sizePolicy().hasHeightForWidth())
        self.KeyInFirebase.setSizePolicy(sizePolicy)
        self.KeyInFirebase.setMinimumSize(QSize(190, 29))
        self.KeyInFirebase.setMaximumSize(QSize(190, 29))
        self.KeyInFirebase.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 2px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_15.addWidget(self.KeyInFirebase, 0, 1, 1, 1)

        self.ModelSelect = QTextEdit(self.groupBox_3)
        self.ModelSelect.setObjectName(u"ModelSelect")
        sizePolicy.setHeightForWidth(self.ModelSelect.sizePolicy().hasHeightForWidth())
        self.ModelSelect.setSizePolicy(sizePolicy)
        self.ModelSelect.setMinimumSize(QSize(190, 29))
        self.ModelSelect.setMaximumSize(QSize(190, 29))
        self.ModelSelect.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 2px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_15.addWidget(self.ModelSelect, 2, 1, 1, 1)

        self.FunctionsSettings = QPushButton(self.groupBox_3)
        self.FunctionsSettings.setObjectName(u"FunctionsSettings")
        self.FunctionsSettings.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/material_design/icons/material_design/settings_input_component.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FunctionsSettings.setIcon(icon14)
        self.FunctionsSettings.setIconSize(QSize(18, 18))

        self.gridLayout_15.addWidget(self.FunctionsSettings, 6, 0, 1, 2)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.page_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_12 = QGridLayout(self.groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(15)
        self.gridLayout_11.setVerticalSpacing(23)
        self.gridLayout_11.setContentsMargins(-1, -1, 18, -1)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.gridLayout_11.addWidget(self.label_9, 1, 0, 1, 1)

        self.VectorstoreinThread = QTextEdit(self.groupBox)
        self.VectorstoreinThread.setObjectName(u"VectorstoreinThread")
        sizePolicy.setHeightForWidth(self.VectorstoreinThread.sizePolicy().hasHeightForWidth())
        self.VectorstoreinThread.setSizePolicy(sizePolicy)
        self.VectorstoreinThread.setMinimumSize(QSize(177, 40))
        self.VectorstoreinThread.setMaximumSize(QSize(177, 40))
        self.VectorstoreinThread.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_11.addWidget(self.VectorstoreinThread, 2, 1, 1, 1)

        self.VectorstoreinThreadByUser = QPushButton(self.groupBox)
        self.VectorstoreinThreadByUser.setObjectName(u"VectorstoreinThreadByUser")
        sizePolicy.setHeightForWidth(self.VectorstoreinThreadByUser.sizePolicy().hasHeightForWidth())
        self.VectorstoreinThreadByUser.setSizePolicy(sizePolicy)
        self.VectorstoreinThreadByUser.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/material_design/icons/material_design/library_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VectorstoreinThreadByUser.setIcon(icon15)
        self.VectorstoreinThreadByUser.setIconSize(QSize(23, 27))

        self.gridLayout_11.addWidget(self.VectorstoreinThreadByUser, 2, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_11.addWidget(self.label_10, 2, 0, 1, 1)

        self.Vectorstoreinassistant = QTextEdit(self.groupBox)
        self.Vectorstoreinassistant.setObjectName(u"Vectorstoreinassistant")
        sizePolicy.setHeightForWidth(self.Vectorstoreinassistant.sizePolicy().hasHeightForWidth())
        self.Vectorstoreinassistant.setSizePolicy(sizePolicy)
        self.Vectorstoreinassistant.setMinimumSize(QSize(177, 40))
        self.Vectorstoreinassistant.setMaximumSize(QSize(177, 40))
        self.Vectorstoreinassistant.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_11.addWidget(self.Vectorstoreinassistant, 1, 1, 1, 1)

        self.UseVectorstoreToGenerateFiles = QCustomCheckBox(self.groupBox)
        self.UseVectorstoreToGenerateFiles.setObjectName(u"UseVectorstoreToGenerateFiles")

        self.gridLayout_11.addWidget(self.UseVectorstoreToGenerateFiles, 0, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(26, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.VectorstoreinassistantByUser = QPushButton(self.groupBox)
        self.VectorstoreinassistantByUser.setObjectName(u"VectorstoreinassistantByUser")
        sizePolicy.setHeightForWidth(self.VectorstoreinassistantByUser.sizePolicy().hasHeightForWidth())
        self.VectorstoreinassistantByUser.setSizePolicy(sizePolicy)
        self.VectorstoreinassistantByUser.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        self.VectorstoreinassistantByUser.setIcon(icon15)
        self.VectorstoreinassistantByUser.setIconSize(QSize(23, 27))

        self.gridLayout_11.addWidget(self.VectorstoreinassistantByUser, 1, 2, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_14 = QGridLayout(self.groupBox_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(59)
        self.gridLayout_13.setVerticalSpacing(8)
        self.gridLayout_13.setContentsMargins(1, 4, 8, 5)
        self.Uploadlistfileforcodeinterpreterinthread = QTextEdit(self.groupBox_2)
        self.Uploadlistfileforcodeinterpreterinthread.setObjectName(u"Uploadlistfileforcodeinterpreterinthread")
        sizePolicy.setHeightForWidth(self.Uploadlistfileforcodeinterpreterinthread.sizePolicy().hasHeightForWidth())
        self.Uploadlistfileforcodeinterpreterinthread.setSizePolicy(sizePolicy)
        self.Uploadlistfileforcodeinterpreterinthread.setMinimumSize(QSize(388, 40))
        self.Uploadlistfileforcodeinterpreterinthread.setMaximumSize(QSize(388, 40))
        self.Uploadlistfileforcodeinterpreterinthread.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_13.addWidget(self.Uploadlistfileforcodeinterpreterinthread, 3, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)

        self.gridLayout_13.addWidget(self.label_12, 1, 0, 1, 1)

        self.Upload1imageforvisioninThread = QTextEdit(self.groupBox_2)
        self.Upload1imageforvisioninThread.setObjectName(u"Upload1imageforvisioninThread")
        sizePolicy.setHeightForWidth(self.Upload1imageforvisioninThread.sizePolicy().hasHeightForWidth())
        self.Upload1imageforvisioninThread.setSizePolicy(sizePolicy)
        self.Upload1imageforvisioninThread.setMinimumSize(QSize(388, 40))
        self.Upload1imageforvisioninThread.setMaximumSize(QSize(388, 40))
        self.Upload1imageforvisioninThread.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_13.addWidget(self.Upload1imageforvisioninThread, 2, 1, 1, 1)

        self.UploadlistfileforcodeinterpreterinthreadByUser = QPushButton(self.groupBox_2)
        self.UploadlistfileforcodeinterpreterinthreadByUser.setObjectName(u"UploadlistfileforcodeinterpreterinthreadByUser")
        sizePolicy.setHeightForWidth(self.UploadlistfileforcodeinterpreterinthreadByUser.sizePolicy().hasHeightForWidth())
        self.UploadlistfileforcodeinterpreterinthreadByUser.setSizePolicy(sizePolicy)
        self.UploadlistfileforcodeinterpreterinthreadByUser.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/material_design/icons/material_design/upload_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UploadlistfileforcodeinterpreterinthreadByUser.setIcon(icon16)
        self.UploadlistfileforcodeinterpreterinthreadByUser.setIconSize(QSize(24, 27))

        self.gridLayout_13.addWidget(self.UploadlistfileforcodeinterpreterinthreadByUser, 3, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)

        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy7)

        self.gridLayout_13.addWidget(self.label_14, 2, 0, 1, 1)

        self.Upload1fileinmessage = QTextEdit(self.groupBox_2)
        self.Upload1fileinmessage.setObjectName(u"Upload1fileinmessage")
        sizePolicy.setHeightForWidth(self.Upload1fileinmessage.sizePolicy().hasHeightForWidth())
        self.Upload1fileinmessage.setSizePolicy(sizePolicy)
        self.Upload1fileinmessage.setMinimumSize(QSize(388, 40))
        self.Upload1fileinmessage.setMaximumSize(QSize(388, 40))
        self.Upload1fileinmessage.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_13.addWidget(self.Upload1fileinmessage, 1, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy7.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy7)

        self.gridLayout_13.addWidget(self.label_13, 3, 0, 1, 1)

        self.Upload1fileinThread = QTextEdit(self.groupBox_2)
        self.Upload1fileinThread.setObjectName(u"Upload1fileinThread")
        sizePolicy.setHeightForWidth(self.Upload1fileinThread.sizePolicy().hasHeightForWidth())
        self.Upload1fileinThread.setSizePolicy(sizePolicy)
        self.Upload1fileinThread.setMinimumSize(QSize(388, 40))
        self.Upload1fileinThread.setMaximumSize(QSize(388, 40))
        self.Upload1fileinThread.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_13.addWidget(self.Upload1fileinThread, 0, 1, 1, 1)

        self.Upload1imageforvisioninThreadByUser = QPushButton(self.groupBox_2)
        self.Upload1imageforvisioninThreadByUser.setObjectName(u"Upload1imageforvisioninThreadByUser")
        sizePolicy.setHeightForWidth(self.Upload1imageforvisioninThreadByUser.sizePolicy().hasHeightForWidth())
        self.Upload1imageforvisioninThreadByUser.setSizePolicy(sizePolicy)
        self.Upload1imageforvisioninThreadByUser.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/material_design/icons/material_design/image_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Upload1imageforvisioninThreadByUser.setIcon(icon17)
        self.Upload1imageforvisioninThreadByUser.setIconSize(QSize(24, 27))

        self.gridLayout_13.addWidget(self.Upload1imageforvisioninThreadByUser, 2, 2, 1, 1)

        self.Upload1fileinmessageByUser = QPushButton(self.groupBox_2)
        self.Upload1fileinmessageByUser.setObjectName(u"Upload1fileinmessageByUser")
        sizePolicy.setHeightForWidth(self.Upload1fileinmessageByUser.sizePolicy().hasHeightForWidth())
        self.Upload1fileinmessageByUser.setSizePolicy(sizePolicy)
        self.Upload1fileinmessageByUser.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/material_design/icons/material_design/attach_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Upload1fileinmessageByUser.setIcon(icon18)
        self.Upload1fileinmessageByUser.setIconSize(QSize(24, 27))

        self.gridLayout_13.addWidget(self.Upload1fileinmessageByUser, 1, 2, 1, 1)

        self.Upload1fileinThreadByUser = QPushButton(self.groupBox_2)
        self.Upload1fileinThreadByUser.setObjectName(u"Upload1fileinThreadByUser")
        sizePolicy.setHeightForWidth(self.Upload1fileinThreadByUser.sizePolicy().hasHeightForWidth())
        self.Upload1fileinThreadByUser.setSizePolicy(sizePolicy)
        self.Upload1fileinThreadByUser.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        self.Upload1fileinThreadByUser.setIcon(icon18)
        self.Upload1fileinThreadByUser.setIconSize(QSize(24, 27))

        self.gridLayout_13.addWidget(self.Upload1fileinThreadByUser, 0, 2, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.CreateAgent = QPushButton(self.page_6)
        self.CreateAgent.setObjectName(u"CreateAgent")
        self.CreateAgent.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"")
        icon19 = QIcon()
        icon19.addFile(u":/material_design/icons/material_design/person_add_alt_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CreateAgent.setIcon(icon19)

        self.gridLayout_10.addWidget(self.CreateAgent, 2, 0, 1, 2)

        self.stackedWidget_SettingsCreate.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_26 = QGridLayout(self.page_7)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.groupBox_5 = QGroupBox(self.page_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_19 = QGridLayout(self.groupBox_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Promptmain = QTextEdit(self.groupBox_5)
        self.Promptmain.setObjectName(u"Promptmain")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.Promptmain.sizePolicy().hasHeightForWidth())
        self.Promptmain.setSizePolicy(sizePolicy8)
        self.Promptmain.setMinimumSize(QSize(0, 0))
        self.Promptmain.setMaximumSize(QSize(16777215, 16777215))
        self.Promptmain.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_19.addWidget(self.Promptmain, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_21 = QGridLayout(self.groupBox_7)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.PromptRules = QTextEdit(self.groupBox_7)
        self.PromptRules.setObjectName(u"PromptRules")
        sizePolicy8.setHeightForWidth(self.PromptRules.sizePolicy().hasHeightForWidth())
        self.PromptRules.setSizePolicy(sizePolicy8)
        self.PromptRules.setMinimumSize(QSize(0, 0))
        self.PromptRules.setMaximumSize(QSize(16777215, 16777215))
        self.PromptRules.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_21.addWidget(self.PromptRules, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_20 = QGridLayout(self.groupBox_6)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.PromptExample = QTextEdit(self.groupBox_6)
        self.PromptExample.setObjectName(u"PromptExample")
        sizePolicy8.setHeightForWidth(self.PromptExample.sizePolicy().hasHeightForWidth())
        self.PromptExample.setSizePolicy(sizePolicy8)
        self.PromptExample.setMinimumSize(QSize(0, 0))
        self.PromptExample.setMaximumSize(QSize(16777215, 16777215))
        self.PromptExample.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_20.addWidget(self.PromptExample, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_6, 0, 2, 1, 1)

        self.BackToSettings = QPushButton(self.page_7)
        self.BackToSettings.setObjectName(u"BackToSettings")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        self.BackToSettings.setFont(font1)
        self.BackToSettings.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.BackToSettings.setIcon(icon)
        self.BackToSettings.setIconSize(QSize(39, 29))

        self.gridLayout_26.addWidget(self.BackToSettings, 1, 0, 1, 3)

        self.stackedWidget_SettingsCreate.addWidget(self.page_7)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_28 = QGridLayout(self.page_5)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.groupBox_8 = QGroupBox(self.page_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_24 = QGridLayout(self.groupBox_8)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.InstructionAgentCreate = QTextEdit(self.groupBox_8)
        self.InstructionAgentCreate.setObjectName(u"InstructionAgentCreate")
        sizePolicy8.setHeightForWidth(self.InstructionAgentCreate.sizePolicy().hasHeightForWidth())
        self.InstructionAgentCreate.setSizePolicy(sizePolicy8)
        self.InstructionAgentCreate.setMinimumSize(QSize(322, 0))
        self.InstructionAgentCreate.setMaximumSize(QSize(322, 16777215))
        self.InstructionAgentCreate.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_24.addWidget(self.InstructionAgentCreate, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_25 = QGridLayout(self.groupBox_4)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.AditionalInstructionsAgentCreate = QTextEdit(self.groupBox_4)
        self.AditionalInstructionsAgentCreate.setObjectName(u"AditionalInstructionsAgentCreate")
        sizePolicy8.setHeightForWidth(self.AditionalInstructionsAgentCreate.sizePolicy().hasHeightForWidth())
        self.AditionalInstructionsAgentCreate.setSizePolicy(sizePolicy8)
        self.AditionalInstructionsAgentCreate.setMinimumSize(QSize(322, 0))
        self.AditionalInstructionsAgentCreate.setMaximumSize(QSize(322, 16777215))
        self.AditionalInstructionsAgentCreate.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_25.addWidget(self.AditionalInstructionsAgentCreate, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.page_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(36, 36))

        self.gridLayout_28.addWidget(self.pushButton, 1, 0, 1, 2)

        self.stackedWidget_SettingsCreate.addWidget(self.page_5)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_31 = QGridLayout(self.page_8)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_10 = QGroupBox(self.page_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_27 = QGridLayout(self.groupBox_10)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.AgentTools = QTextEdit(self.groupBox_10)
        self.AgentTools.setObjectName(u"AgentTools")
        sizePolicy8.setHeightForWidth(self.AgentTools.sizePolicy().hasHeightForWidth())
        self.AgentTools.setSizePolicy(sizePolicy8)
        self.AgentTools.setMinimumSize(QSize(0, 0))
        self.AgentTools.setMaximumSize(QSize(16777215, 16777215))
        self.AgentTools.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_27.addWidget(self.AgentTools, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_10, 0, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.page_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_29 = QGridLayout(self.groupBox_11)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.namefunction_agentcreate = QTextEdit(self.groupBox_11)
        self.namefunction_agentcreate.setObjectName(u"namefunction_agentcreate")
        self.namefunction_agentcreate.setMaximumSize(QSize(16777215, 22))
        self.namefunction_agentcreate.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 3px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_29.addWidget(self.namefunction_agentcreate, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_11)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_29.addWidget(self.label_16, 0, 0, 1, 1)

        self.FunctionPython = QTextEdit(self.groupBox_11)
        self.FunctionPython.setObjectName(u"FunctionPython")
        sizePolicy8.setHeightForWidth(self.FunctionPython.sizePolicy().hasHeightForWidth())
        self.FunctionPython.setSizePolicy(sizePolicy8)
        self.FunctionPython.setMinimumSize(QSize(0, 0))
        self.FunctionPython.setMaximumSize(QSize(16777215, 16777215))
        self.FunctionPython.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_29.addWidget(self.FunctionPython, 1, 0, 1, 2)


        self.gridLayout_31.addWidget(self.groupBox_11, 0, 1, 1, 1)

        self.groupBox_12 = QGroupBox(self.page_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_30 = QGridLayout(self.groupBox_12)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.FunctionPythonOutput = QTextEdit(self.groupBox_12)
        self.FunctionPythonOutput.setObjectName(u"FunctionPythonOutput")
        sizePolicy8.setHeightForWidth(self.FunctionPythonOutput.sizePolicy().hasHeightForWidth())
        self.FunctionPythonOutput.setSizePolicy(sizePolicy8)
        self.FunctionPythonOutput.setMinimumSize(QSize(0, 0))
        self.FunctionPythonOutput.setMaximumSize(QSize(16777215, 16777215))
        self.FunctionPythonOutput.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 5px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_30.addWidget(self.FunctionPythonOutput, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_12, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.page_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(35, 33))

        self.gridLayout_31.addWidget(self.pushButton_2, 1, 0, 1, 3)

        self.stackedWidget_SettingsCreate.addWidget(self.page_8)

        self.gridLayout_17.addWidget(self.stackedWidget_SettingsCreate, 0, 0, 1, 1)

        self.myStackedWidget.addWidget(self.page_settings)

        self.gridLayout.addWidget(self.myStackedWidget, 1, 1, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.myStackedWidget.setCurrentIndex(2)
        self.stackedWidget_instruction.setCurrentIndex(0)
        self.stackedWidget_SettingsCreate.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText("")
        self.close_window_button.setText("")
        self.restore_window_button.setText("")
        self.minimize_window_button.setText("")
        self.CreateAgents_menu.setText("")
        self.Editor_instructions.setText("")
        self.Editor_functions.setText("")
        self.html_chat_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Current Function...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.mensage_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Function...", None))
        self.send_mensage_2.setText("")
        self.Current_instuction_html_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Current Instruction", None))
        self.Add_new_instructions_button_edit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Instruction", None))
        self.instruction_input_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Instruction...", None))
        self.change_instruction_button_edit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name For instruction", None))
        self.NameForInstruction_create.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bob", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Instruction For Agent", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Instruction Category", None))
        self.BacktoEditinstruction_create.setText("")
        self.New_instruction_html_create.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Instruction...", None))
        self.CreateInstructionbutton_create.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Initial Settings", None))
        self.InstructionSettings.setText(QCoreApplication.translate("MainWindow", u"Instruction Settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Model Select", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Key In Firebase", None))
        self.PromptSettings.setText(QCoreApplication.translate("MainWindow", u"Prompt Settings", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Agent Category", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name Agent", None))
        self.NameAgent.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dallas2</p></body></html>", None))
        self.NameAgent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dallas", None))
        self.KeyInFirebase.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AgentForPlanningDallas</p></body></html>", None))
        self.KeyInFirebase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AgentForPlanningDallas", None))
        self.ModelSelect.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gpt-4o-mini-2024-07-18</p></body></html>", None))
        self.ModelSelect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gpt-4o-mini-2024-07-18", None))
        self.FunctionsSettings.setText(QCoreApplication.translate("MainWindow", u"Functions Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VectorStore", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Vectorstore in assistant", None))
        self.VectorstoreinThread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"vs_USBolYuyy7cVX....", None))
        self.VectorstoreinThreadByUser.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Vectorstore in Thread", None))
        self.Vectorstoreinassistant.setPlaceholderText(QCoreApplication.translate("MainWindow", u"vs_USBolYuyy7cVX....", None))
        self.UseVectorstoreToGenerateFiles.setText(QCoreApplication.translate("MainWindow", u"Use Vectorstore To Generate Files", None))
        self.VectorstoreinassistantByUser.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.Uploadlistfileforcodeinterpreterinthread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path/test.py,path/test2.txt", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Upload 1 file in message", None))
        self.Upload1imageforvisioninThread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path/test.png", None))
        self.UploadlistfileforcodeinterpreterinthreadByUser.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Upload 1 file in Thread", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Upload 1 image for vision in Thread", None))
        self.Upload1fileinmessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path/test.py", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Upload list file for code interpreter in thread", None))
        self.Upload1fileinThread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path/test.py", None))
        self.Upload1imageforvisioninThreadByUser.setText("")
        self.Upload1fileinmessageByUser.setText("")
        self.Upload1fileinThreadByUser.setText("")
        self.CreateAgent.setText(QCoreApplication.translate("MainWindow", u"Create Agent", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Prompt main", None))
        self.Promptmain.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">decida oque o usuario esta solicitando com base na mensagem recebida</p></body></html>", None))
        self.Promptmain.setPlaceholderText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Prompt Rules", None))
        self.PromptRules.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">regras de teste</p></body></html>", None))
        self.PromptRules.setPlaceholderText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Sample response provided to the agent", None))
        self.PromptExample.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Caso seja solicitado algum script ou software Responda no formato JSON Exemplo:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">{'solicitadoalgumcodigo': 'solicitacao...'} </span></p></body></html>", None))
        self.PromptExample.setPlaceholderText("")
        self.BackToSettings.setText(QCoreApplication.translate("MainWindow", u"Back To Settings", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.InstructionAgentCreate.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Seu Nome \u00e9 Dallas, Voce Faz parte da Equipe de Solucoes da empresa Urobotsoftware, seu objetivo \u00e9 Planejar um Roadmap do Projeto com base no Cronograma,Planilha e Documento Pre Projeto </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Responda o Roadmap do Projeto no formato JSON</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Exemplo:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">{&quot;Roadmap&quot;: &quot;Roadmap do Projeto ...&quot;}</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">{&quot;nome_do_Roadmap&quot;: &quot;nome_do_Roadmap_do_projeto ...&quot;}</span></p></body></html>", None))
        self.InstructionAgentCreate.setPlaceholderText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Aditional Instructions", None))
        self.AditionalInstructionsAgentCreate.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.AditionalInstructionsAgentCreate.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back To Settings", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Agent Tools", None))
        self.AgentTools.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1f1f1f;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;type&quot;</span><span style=\" font-family:"
                        "'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;function&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;function&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0"
                        " \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;name&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;</span><span style=\" font-size:8pt;\">pegar_hora</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;description&quot;</span><span style=\""
                        " font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;Retorna a data e hora atual no formato YYYY-MM-DD HH:MM:SS.&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;parameters&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,C"
                        "ourier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;type&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;object&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;properties&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;"
                        "\">: {},</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;required&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: []</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0"
                        " \u00a0 }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 } </span></p></body></html>", None))
        self.AgentTools.setPlaceholderText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Function Python", None))
        self.namefunction_agentcreate.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">pegar_hora</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.FunctionPython.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">def pegar_hora():</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     import datetime</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     current_datetime = datetime.datetime.now()</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     return f&quot;{formatted_datetime}&quot;</span></p></body></html>", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Function Python Output", None))
        self.FunctionPythonOutput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1f1f1f;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#569cd6;\">def</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#dcdcaa;\">submit_output_</span><span style=\" font-size:8pt;\">pegar_hora</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">(</span><span style=\" font-family:'Consolas,Courier New"
                        ",monospace'; font-size:8pt; color:#9cdcfe;\">function_name</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">function_arguments</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0"
                        " \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_call</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">threead_id</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0"
                        " \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">client</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">run</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 ):"
                        "</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#569cd6;\">global</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_outputs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">if</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span st"
                        "yle=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">function_name</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4;\">==</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">'</span><span style=\" font-size:8pt;\">pegar_hora</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">'</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span "
                        "style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">resultado</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4;\">=</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#dcdcaa;\">get_current_datetime</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_outputs</span><span style=\" font-family:"
                        "'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">.</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#dcdcaa;\">append</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">({</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;tool_call_id&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_call</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">.id,</span></p>\n"
"<p style=\" margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;output&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">: </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">resultado</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 })</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0"
                        " \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#6a9955;\"># Submit all tool outputs at once after collecting them in a list</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">if</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_outputs</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Cour"
                        "ier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">try</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">run</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4;\">=</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospa"
                        "ce'; font-size:8pt; color:#9cdcfe;\">client</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">.beta.threads.runs.submit_tool_outputs_and_poll(</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">thread_id</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4;\">=</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">threead_id</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">run_id</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4;\">=</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">run</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">.id,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_outputs</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4"
                        ";\">=</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_outputs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 )</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#dcdcaa;\">print</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">(</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;Tool outputs submitted successfully.&quot;</span><s"
                        "pan style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">tool_outputs</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#d4d4d4;\">=</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> []</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 "
                        "\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">return</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#569cd6;\">True</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">except</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#4ec9b0;\">Exception</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><spa"
                        "n style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">as</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\"> </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">e</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#dcdcaa;\">print</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">(</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;Failed to submit tool outputs:&quot;</span><spa"
                        "n style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">, </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#9cdcfe;\">e</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 </span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#c586c0;\">else</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">\u00a0 \u00a0 \u00a0 \u00a0 </span><span style=\" fon"
                        "t-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#dcdcaa;\">print</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">(</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#ce9178;\">&quot;No tool outputs to submit.&quot;</span><span style=\" font-family:'Consolas,Courier New,monospace'; font-size:8pt; color:#cccccc;\">)</span></p></body></html>", None))
        self.FunctionPythonOutput.setPlaceholderText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Back To Settings", None))
    # retranslateUi

