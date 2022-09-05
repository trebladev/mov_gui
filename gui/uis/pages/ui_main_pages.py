# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagespUMWOT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.verticalLayout_2 = QVBoxLayout(MainPages)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.page1_right = QFrame(self.frame)
        self.page1_right.setObjectName(u"page1_right")
        self.page1_right.setGeometry(QRect(584, 0, 250, 574))
        self.page1_right.setMaximumSize(QSize(16777215, 16777215))
        self.page1_right.setFrameShape(QFrame.StyledPanel)
        self.page1_right.setFrameShadow(QFrame.Raised)
        self.page1_right_layout = QVBoxLayout(self.page1_right)
        self.page1_right_layout.setObjectName(u"page1_right_layout")
        self.scene_select_frame = QFrame(self.page1_right)
        self.scene_select_frame.setObjectName(u"scene_select_frame")
        self.scene_select_frame.setMaximumSize(QSize(16777215, 120))
        self.scene_select_frame.setFrameShape(QFrame.StyledPanel)
        self.scene_select_frame.setFrameShadow(QFrame.Raised)
        self.radio_btn_layout = QVBoxLayout(self.scene_select_frame)
        self.radio_btn_layout.setObjectName(u"radio_btn_layout")
        self.big_scene = QRadioButton(self.scene_select_frame)
        self.big_scene.setObjectName(u"big_scene")
        self.big_scene.setAutoFillBackground(False)
        self.big_scene.setCheckable(True)
        self.big_scene.setChecked(False)

        self.radio_btn_layout.addWidget(self.big_scene)

        self.small_scene = QRadioButton(self.scene_select_frame)
        self.small_scene.setObjectName(u"small_scene")

        self.radio_btn_layout.addWidget(self.small_scene)


        self.page1_right_layout.addWidget(self.scene_select_frame)

        self.scan_list = QListView(self.page1_right)
        self.scan_list.setObjectName(u"scan_list")
        self.scan_list.setMaximumSize(QSize(16777215, 250))

        self.page1_right_layout.addWidget(self.scan_list)

        self.start_btn_frame = QFrame(self.page1_right)
        self.start_btn_frame.setObjectName(u"start_btn_frame")
        self.start_btn_frame.setMaximumSize(QSize(16777215, 100))
        self.start_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.start_btn_frame.setFrameShadow(QFrame.Raised)
        self.start_btn_layout = QVBoxLayout(self.start_btn_frame)
        self.start_btn_layout.setObjectName(u"start_btn_layout")

        self.page1_right_layout.addWidget(self.start_btn_frame)

        self.page1_left = QFrame(self.frame)
        self.page1_left.setObjectName(u"page1_left")
        self.page1_left.setGeometry(QRect(0, 0, 584, 574))
        self.page1_left.setFrameShape(QFrame.StyledPanel)
        self.page1_left.setFrameShadow(QFrame.Raised)
        self.page1_label = QLabel(self.page1_left)
        self.page1_label.setObjectName(u"page1_label")
        self.page1_label.setGeometry(QRect(250, 210, 63, 20))

        self.page_1_layout.addWidget(self.frame)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.page2_right = QFrame(self.frame_2)
        self.page2_right.setObjectName(u"page2_right")
        self.page2_right.setGeometry(QRect(584, 0, 250, 574))
        self.page2_right.setFrameShape(QFrame.StyledPanel)
        self.page2_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.page2_right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.page2_list_frame = QFrame(self.page2_right)
        self.page2_list_frame.setObjectName(u"page2_list_frame")
        self.page2_list_frame.setMaximumSize(QSize(16777215, 400))
        self.page2_list_frame.setFrameShape(QFrame.StyledPanel)
        self.page2_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.page2_list_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.page2_list = QListView(self.page2_list_frame)
        self.page2_list.setObjectName(u"page2_list")

        self.verticalLayout.addWidget(self.page2_list)


        self.verticalLayout_4.addWidget(self.page2_list_frame)

        self.page2_button = QFrame(self.page2_right)
        self.page2_button.setObjectName(u"page2_button")
        self.page2_button.setMaximumSize(QSize(16777215, 150))
        self.page2_button.setFrameShape(QFrame.StyledPanel)
        self.page2_button.setFrameShadow(QFrame.Raised)
        self.page2_btn_layout = QVBoxLayout(self.page2_button)
        self.page2_btn_layout.setObjectName(u"page2_btn_layout")

        self.verticalLayout_4.addWidget(self.page2_button)

        self.page2_left = QFrame(self.frame_2)
        self.page2_left.setObjectName(u"page2_left")
        self.page2_left.setGeometry(QRect(0, 0, 584, 574))
        self.page2_left.setFrameShape(QFrame.StyledPanel)
        self.page2_left.setFrameShadow(QFrame.Raised)
        self.page2_label = QLabel(self.page2_left)
        self.page2_label.setObjectName(u"page2_label")
        self.page2_label.setGeometry(QRect(270, 260, 63, 20))

        self.page_2_layout.addWidget(self.frame_2)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.pages.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.big_scene.setText(QCoreApplication.translate("MainPages", u"\u5927\u573a\u666f", None))
        self.small_scene.setText(QCoreApplication.translate("MainPages", u"\u5c0f\u573a\u666f", None))
        self.page1_label.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.page2_label.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
    # retranslateUi

