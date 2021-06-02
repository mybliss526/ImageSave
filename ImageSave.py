# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageSave.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from moviepy.editor import *

import sys
import cv2
import os
import numpy as np
import threading
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(66, 66, 66, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(99, 99, 99, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(82, 82, 82, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(33, 33, 33, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(44, 44, 44, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 9, 791, 531))
        self.Page01 = QWidget()
        self.Page01.setObjectName(u"Page01")
        self.Page01_Livelabel1 = QLabel(self.Page01)
        self.Page01_Livelabel1.setObjectName(u"Page01_Livelabel1")
        self.Page01_Livelabel1.setGeometry(QRect(0, 10, 56, 12))
        self.Page01_Livelabel2 = QLabel(self.Page01)
        self.Page01_Livelabel2.setObjectName(u"Page01_Livelabel2")
        self.Page01_Livelabel2.setGeometry(QRect(400, 10, 56, 12))
        self.Page01_Livelabel3 = QLabel(self.Page01)
        self.Page01_Livelabel3.setObjectName(u"Page01_Livelabel3")
        self.Page01_Livelabel3.setGeometry(QRect(0, 270, 56, 12))
        self.Page01_Livelabel4 = QLabel(self.Page01)
        self.Page01_Livelabel4.setObjectName(u"Page01_Livelabel4")
        self.Page01_Livelabel4.setGeometry(QRect(400, 270, 56, 12))
        self.horizontalLayoutWidget_5 = QWidget(self.Page01)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 20, 391, 241))
        self.Page01_CameraImage1 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.Page01_CameraImage1.setObjectName(u"Page01_CameraImage1")
        self.Page01_CameraImage1.setContentsMargins(0, 0, 0, 0)
        self.Page01_LiveImagelabel1 = QLabel(self.horizontalLayoutWidget_5)
        self.Page01_LiveImagelabel1.setObjectName(u"Page01_LiveImagelabel1")

        self.Page01_CameraImage1.addWidget(self.Page01_LiveImagelabel1)

        self.horizontalLayoutWidget_6 = QWidget(self.Page01)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 280, 391, 241))
        self.Page01_CameraImage3 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.Page01_CameraImage3.setObjectName(u"Page01_CameraImage3")
        self.Page01_CameraImage3.setContentsMargins(0, 0, 0, 0)
        self.Page01_LiveImagelabel3 = QLabel(self.horizontalLayoutWidget_6)
        self.Page01_LiveImagelabel3.setObjectName(u"Page01_LiveImagelabel3")

        self.Page01_CameraImage3.addWidget(self.Page01_LiveImagelabel3)

        self.horizontalLayoutWidget_10 = QWidget(self.Page01)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(400, 20, 391, 241))
        self.Page01_CameraImage2 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.Page01_CameraImage2.setObjectName(u"Page01_CameraImage2")
        self.Page01_CameraImage2.setContentsMargins(0, 0, 0, 0)
        self.Page01_LiveImagelabel2 = QLabel(self.horizontalLayoutWidget_10)
        self.Page01_LiveImagelabel2.setObjectName(u"Page01_LiveImagelabel2")

        self.Page01_CameraImage2.addWidget(self.Page01_LiveImagelabel2)

        self.horizontalLayoutWidget_11 = QWidget(self.Page01)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(400, 280, 391, 241))
        self.Page01_CameraImage4 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.Page01_CameraImage4.setObjectName(u"Page01_CameraImage4")
        self.Page01_CameraImage4.setContentsMargins(0, 0, 0, 0)
        self.Page01_LiveImagelabel4 = QLabel(self.horizontalLayoutWidget_11)
        self.Page01_LiveImagelabel4.setObjectName(u"Page01_LiveImagelabel4")

        self.Page01_CameraImage4.addWidget(self.Page01_LiveImagelabel4)

        self.stackedWidget.addWidget(self.Page01)
        self.Page02 = QWidget()
        self.Page02.setObjectName(u"Page02")
        self.CameratabWidget = QTabWidget(self.Page02)
        self.CameratabWidget.setObjectName(u"CameratabWidget")
        self.CameratabWidget.setGeometry(QRect(0, 0, 791, 531))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush9 = QBrush(QColor(139, 139, 139, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush9)
        brush10 = QBrush(QColor(208, 208, 208, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush10)
        brush11 = QBrush(QColor(173, 173, 173, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        brush12 = QBrush(QColor(69, 69, 69, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush12)
        brush13 = QBrush(QColor(93, 93, 93, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush14 = QBrush(QColor(197, 197, 197, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush15 = QBrush(QColor(0, 0, 0, 128))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.CameratabWidget.setPalette(palette1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.Page02_CameraImage1.setObjectName(u"Page02_CameraImage1")
        self.Page02_CameraImage1.setContentsMargins(0, 0, 0, 0)
        self.Page02_ImageLabel1 = QLabel(self.horizontalLayoutWidget)
        self.Page02_ImageLabel1.setObjectName(u"Page02_ImageLabel1")

        self.Page02_CameraImage1.addWidget(self.Page02_ImageLabel1)

        self.horizontalLayoutWidget_3 = QWidget(self.tab)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(570, 470, 201, 31))
        self.Page02_CaptureLayout1 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.Page02_CaptureLayout1.setObjectName(u"Page02_CaptureLayout1")
        self.Page02_CaptureLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page02_CaptureLabel1 = QLabel(self.horizontalLayoutWidget_3)
        self.Page02_CaptureLabel1.setObjectName(u"Page02_CaptureLabel1")

        self.Page02_CaptureLayout1.addWidget(self.Page02_CaptureLabel1)

        self.Page02_CaptureSetButton1 = QPushButton(self.horizontalLayoutWidget_3)
        self.Page02_CaptureSetButton1.setObjectName(u"Page02_CaptureSetButton1")

        self.Page02_CaptureLayout1.addWidget(self.Page02_CaptureSetButton1)

        self.Page02_CaptureReleaseButton1 = QPushButton(self.horizontalLayoutWidget_3)
        self.Page02_CaptureReleaseButton1.setObjectName(u"Page02_CaptureReleaseButton1")

        self.Page02_CaptureLayout1.addWidget(self.Page02_CaptureReleaseButton1)

        self.horizontalLayoutWidget_33 = QWidget(self.tab)
        self.horizontalLayoutWidget_33.setObjectName(u"horizontalLayoutWidget_33")
        self.horizontalLayoutWidget_33.setGeometry(QRect(570, 440, 201, 31))
        self.Page02_VideoLayout1 = QHBoxLayout(self.horizontalLayoutWidget_33)
        self.Page02_VideoLayout1.setObjectName(u"Page02_VideoLayout1")
        self.Page02_VideoLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page02_Videolabel1 = QLabel(self.horizontalLayoutWidget_33)
        self.Page02_Videolabel1.setObjectName(u"Page02_Videolabel1")

        self.Page02_VideoLayout1.addWidget(self.Page02_Videolabel1)

        self.Page02_VideoStopButton1 = QPushButton(self.horizontalLayoutWidget_33)
        self.Page02_VideoStopButton1.setObjectName(u"Page02_VideoStopButton1")

        self.Page02_VideoLayout1.addWidget(self.Page02_VideoStopButton1)

        self.Page02_VideoPlayButton1 = QPushButton(self.horizontalLayoutWidget_33)
        self.Page02_VideoPlayButton1.setObjectName(u"Page02_VideoPlayButton1")

        self.Page02_VideoLayout1.addWidget(self.Page02_VideoPlayButton1)

        self.Page02_scrollArea1 = QScrollArea(self.tab)
        self.Page02_scrollArea1.setObjectName(u"Page02_scrollArea1")
        self.Page02_scrollArea1.setGeometry(QRect(0, 430, 531, 71))
        self.Page02_scrollArea1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 512, 167))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Page02_setOKImageLayout1 = QHBoxLayout()
        self.Page02_setOKImageLayout1.setObjectName(u"Page02_setOKImageLayout1")
        self.Page02_setOKImageLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.Page02_setOKImageLabel1.setObjectName(u"Page02_setOKImageLabel1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_setOKImageLabel1)

        self.Page02_setOKImagelineEdit1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Page02_setOKImagelineEdit1.setObjectName(u"Page02_setOKImagelineEdit1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_setOKImagelineEdit1)

        self.Page02_setOKImagebutton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_setOKImagebutton1.setObjectName(u"Page02_setOKImagebutton1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_setOKImagebutton1)

        self.Page02_OKImageSaveButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_OKImageSaveButton1.setObjectName(u"Page02_OKImageSaveButton1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_OKImageSaveButton1)


        self.verticalLayout_2.addLayout(self.Page02_setOKImageLayout1)

        self.Page02_setNGImageLayout1 = QHBoxLayout()
        self.Page02_setNGImageLayout1.setObjectName(u"Page02_setNGImageLayout1")
        self.Page02_setNGImageLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.Page02_setNGImageLabel1.setObjectName(u"Page02_setNGImageLabel1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_setNGImageLabel1)

        self.Page02_setNGImagelineEdit1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Page02_setNGImagelineEdit1.setObjectName(u"Page02_setNGImagelineEdit1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_setNGImagelineEdit1)

        self.Page02_setNGImagebutton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_setNGImagebutton1.setObjectName(u"Page02_setNGImagebutton1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_setNGImagebutton1)

        self.Page02_NGImageSaveButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_NGImageSaveButton1.setObjectName(u"Page02_NGImageSaveButton1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_NGImageSaveButton1)


        self.verticalLayout_2.addLayout(self.Page02_setNGImageLayout1)

        self.Page02_setAImageLayout1 = QHBoxLayout()
        self.Page02_setAImageLayout1.setObjectName(u"Page02_setAImageLayout1")
        self.Page02_setAImageLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.Page02_setAImageLabel1.setObjectName(u"Page02_setAImageLabel1")

        self.Page02_setAImageLayout1.addWidget(self.Page02_setAImageLabel1)

        self.Page02_setAImagelineEdit1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Page02_setAImagelineEdit1.setObjectName(u"Page02_setAImagelineEdit1")

        self.Page02_setAImageLayout1.addWidget(self.Page02_setAImagelineEdit1)

        self.Page02_setAImagebutton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_setAImagebutton1.setObjectName(u"Page02_setAImagebutton1")

        self.Page02_setAImageLayout1.addWidget(self.Page02_setAImagebutton1)

        self.Page02_AImageSaveButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_AImageSaveButton1.setObjectName(u"Page02_AImageSaveButton1")

        self.Page02_setAImageLayout1.addWidget(self.Page02_AImageSaveButton1)


        self.verticalLayout_2.addLayout(self.Page02_setAImageLayout1)

        self.Page02_setBImageLayout1 = QHBoxLayout()
        self.Page02_setBImageLayout1.setObjectName(u"Page02_setBImageLayout1")
        self.Page02_setBImageLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.Page02_setBImageLabel1.setObjectName(u"Page02_setBImageLabel1")

        self.Page02_setBImageLayout1.addWidget(self.Page02_setBImageLabel1)

        self.Page02_setBImagelineEdit1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Page02_setBImagelineEdit1.setObjectName(u"Page02_setBImagelineEdit1")

        self.Page02_setBImageLayout1.addWidget(self.Page02_setBImagelineEdit1)

        self.Page02_setBImagebutton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_setBImagebutton1.setObjectName(u"Page02_setBImagebutton1")

        self.Page02_setBImageLayout1.addWidget(self.Page02_setBImagebutton1)

        self.Page02_BImageSaveButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_BImageSaveButton1.setObjectName(u"Page02_BImageSaveButton1")

        self.Page02_setBImageLayout1.addWidget(self.Page02_BImageSaveButton1)


        self.verticalLayout_2.addLayout(self.Page02_setBImageLayout1)

        self.Page02_setCImageLayout1 = QHBoxLayout()
        self.Page02_setCImageLayout1.setObjectName(u"Page02_setCImageLayout1")
        self.Page02_setCImageLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.Page02_setCImageLabel1.setObjectName(u"Page02_setCImageLabel1")

        self.Page02_setCImageLayout1.addWidget(self.Page02_setCImageLabel1)

        self.Page02_setCImagelineEdit1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Page02_setCImagelineEdit1.setObjectName(u"Page02_setCImagelineEdit1")

        self.Page02_setCImageLayout1.addWidget(self.Page02_setCImagelineEdit1)

        self.Page02_setCImagebutton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_setCImagebutton1.setObjectName(u"Page02_setCImagebutton1")

        self.Page02_setCImageLayout1.addWidget(self.Page02_setCImagebutton1)

        self.Page02_CImageSaveButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Page02_CImageSaveButton1.setObjectName(u"Page02_CImageSaveButton1")

        self.Page02_setCImageLayout1.addWidget(self.Page02_CImageSaveButton1)


        self.verticalLayout_2.addLayout(self.Page02_setCImageLayout1)

        self.Page02_scrollArea1.setWidget(self.scrollAreaWidgetContents_2)
        self.CameratabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Page02_CameraImage2.setObjectName(u"Page02_CameraImage2")
        self.Page02_CameraImage2.setContentsMargins(0, 0, 0, 0)
        self.Page02_ImageLabel2 = QLabel(self.horizontalLayoutWidget_2)
        self.Page02_ImageLabel2.setObjectName(u"Page02_ImageLabel2")

        self.Page02_CameraImage2.addWidget(self.Page02_ImageLabel2)

        self.horizontalLayoutWidget_4 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(570, 470, 201, 31))
        self.Page02_CaptureLayout2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.Page02_CaptureLayout2.setObjectName(u"Page02_CaptureLayout2")
        self.Page02_CaptureLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page02_CaptureLabel2 = QLabel(self.horizontalLayoutWidget_4)
        self.Page02_CaptureLabel2.setObjectName(u"Page02_CaptureLabel2")

        self.Page02_CaptureLayout2.addWidget(self.Page02_CaptureLabel2)

        self.Page02_CaptureSetButton2 = QPushButton(self.horizontalLayoutWidget_4)
        self.Page02_CaptureSetButton2.setObjectName(u"Page02_CaptureSetButton2")

        self.Page02_CaptureLayout2.addWidget(self.Page02_CaptureSetButton2)

        self.Page02_CaptureReleaseButton2 = QPushButton(self.horizontalLayoutWidget_4)
        self.Page02_CaptureReleaseButton2.setObjectName(u"Page02_CaptureReleaseButton2")

        self.Page02_CaptureLayout2.addWidget(self.Page02_CaptureReleaseButton2)

        self.horizontalLayoutWidget_32 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_32.setObjectName(u"horizontalLayoutWidget_32")
        self.horizontalLayoutWidget_32.setGeometry(QRect(570, 440, 201, 31))
        self.Page02_VideoLayout2 = QHBoxLayout(self.horizontalLayoutWidget_32)
        self.Page02_VideoLayout2.setObjectName(u"Page02_VideoLayout2")
        self.Page02_VideoLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page02_Videolabel2 = QLabel(self.horizontalLayoutWidget_32)
        self.Page02_Videolabel2.setObjectName(u"Page02_Videolabel2")

        self.Page02_VideoLayout2.addWidget(self.Page02_Videolabel2)

        self.Page02_VideoStopButton2 = QPushButton(self.horizontalLayoutWidget_32)
        self.Page02_VideoStopButton2.setObjectName(u"Page02_VideoStopButton2")

        self.Page02_VideoLayout2.addWidget(self.Page02_VideoStopButton2)

        self.Page02_VideoPlayButton2 = QPushButton(self.horizontalLayoutWidget_32)
        self.Page02_VideoPlayButton2.setObjectName(u"Page02_VideoPlayButton2")

        self.Page02_VideoLayout2.addWidget(self.Page02_VideoPlayButton2)

        self.Page02_scrollArea2 = QScrollArea(self.tab_2)
        self.Page02_scrollArea2.setObjectName(u"Page02_scrollArea2")
        self.Page02_scrollArea2.setGeometry(QRect(0, 430, 531, 71))
        self.Page02_scrollArea2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 512, 167))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Page02_setOKImageLayout2 = QHBoxLayout()
        self.Page02_setOKImageLayout2.setObjectName(u"Page02_setOKImageLayout2")
        self.Page02_setOKImageLabel2 = QLabel(self.scrollAreaWidgetContents_4)
        self.Page02_setOKImageLabel2.setObjectName(u"Page02_setOKImageLabel2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_setOKImageLabel2)

        self.Page02_setOKImagelineEdit2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.Page02_setOKImagelineEdit2.setObjectName(u"Page02_setOKImagelineEdit2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_setOKImagelineEdit2)

        self.Page02_setOKImagebutton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_setOKImagebutton2.setObjectName(u"Page02_setOKImagebutton2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_setOKImagebutton2)

        self.Page02_OKImageSaveButton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_OKImageSaveButton2.setObjectName(u"Page02_OKImageSaveButton2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_OKImageSaveButton2)


        self.verticalLayout_4.addLayout(self.Page02_setOKImageLayout2)

        self.Page02_setNGImageLayout2 = QHBoxLayout()
        self.Page02_setNGImageLayout2.setObjectName(u"Page02_setNGImageLayout2")
        self.Page02_setNGImageLabel2 = QLabel(self.scrollAreaWidgetContents_4)
        self.Page02_setNGImageLabel2.setObjectName(u"Page02_setNGImageLabel2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_setNGImageLabel2)

        self.Page02_setNGImagelineEdit2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.Page02_setNGImagelineEdit2.setObjectName(u"Page02_setNGImagelineEdit2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_setNGImagelineEdit2)

        self.Page02_setNGImagebutton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_setNGImagebutton2.setObjectName(u"Page02_setNGImagebutton2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_setNGImagebutton2)

        self.Page02_NGImageSaveButton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_NGImageSaveButton2.setObjectName(u"Page02_NGImageSaveButton2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_NGImageSaveButton2)


        self.verticalLayout_4.addLayout(self.Page02_setNGImageLayout2)

        self.Page02_setAImageLayout2 = QHBoxLayout()
        self.Page02_setAImageLayout2.setObjectName(u"Page02_setAImageLayout2")
        self.Page02_setAImageLabel2 = QLabel(self.scrollAreaWidgetContents_4)
        self.Page02_setAImageLabel2.setObjectName(u"Page02_setAImageLabel2")

        self.Page02_setAImageLayout2.addWidget(self.Page02_setAImageLabel2)

        self.Page02_setAImagelineEdit2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.Page02_setAImagelineEdit2.setObjectName(u"Page02_setAImagelineEdit2")

        self.Page02_setAImageLayout2.addWidget(self.Page02_setAImagelineEdit2)

        self.Page02_setAImagebutton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_setAImagebutton2.setObjectName(u"Page02_setAImagebutton2")

        self.Page02_setAImageLayout2.addWidget(self.Page02_setAImagebutton2)

        self.Page02_AImageSaveButton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_AImageSaveButton2.setObjectName(u"Page02_AImageSaveButton2")

        self.Page02_setAImageLayout2.addWidget(self.Page02_AImageSaveButton2)


        self.verticalLayout_4.addLayout(self.Page02_setAImageLayout2)

        self.Page02_setBImageLayout2 = QHBoxLayout()
        self.Page02_setBImageLayout2.setObjectName(u"Page02_setBImageLayout2")
        self.Page02_setBImageLabel2 = QLabel(self.scrollAreaWidgetContents_4)
        self.Page02_setBImageLabel2.setObjectName(u"Page02_setBImageLabel2")

        self.Page02_setBImageLayout2.addWidget(self.Page02_setBImageLabel2)

        self.Page02_setBImagelineEdit2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.Page02_setBImagelineEdit2.setObjectName(u"Page02_setBImagelineEdit2")

        self.Page02_setBImageLayout2.addWidget(self.Page02_setBImagelineEdit2)

        self.Page02_setBImagebutton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_setBImagebutton2.setObjectName(u"Page02_setBImagebutton2")

        self.Page02_setBImageLayout2.addWidget(self.Page02_setBImagebutton2)

        self.Page02_BImageSaveButton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_BImageSaveButton2.setObjectName(u"Page02_BImageSaveButton2")

        self.Page02_setBImageLayout2.addWidget(self.Page02_BImageSaveButton2)


        self.verticalLayout_4.addLayout(self.Page02_setBImageLayout2)

        self.Page02_setCImageLayout2 = QHBoxLayout()
        self.Page02_setCImageLayout2.setObjectName(u"Page02_setCImageLayout2")
        self.Page02_setCImageLabel2 = QLabel(self.scrollAreaWidgetContents_4)
        self.Page02_setCImageLabel2.setObjectName(u"Page02_setCImageLabel2")

        self.Page02_setCImageLayout2.addWidget(self.Page02_setCImageLabel2)

        self.Page02_setCImagelineEdit2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.Page02_setCImagelineEdit2.setObjectName(u"Page02_setCImagelineEdit2")

        self.Page02_setCImageLayout2.addWidget(self.Page02_setCImagelineEdit2)

        self.Page02_setCImagebutton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_setCImagebutton2.setObjectName(u"Page02_setCImagebutton2")

        self.Page02_setCImageLayout2.addWidget(self.Page02_setCImagebutton2)

        self.Page02_CImageSaveButton2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Page02_CImageSaveButton2.setObjectName(u"Page02_CImageSaveButton2")

        self.Page02_setCImageLayout2.addWidget(self.Page02_CImageSaveButton2)


        self.verticalLayout_4.addLayout(self.Page02_setCImageLayout2)

        self.Page02_scrollArea2.setWidget(self.scrollAreaWidgetContents_4)
        self.CameratabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayoutWidget_15 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(570, 470, 201, 31))
        self.Page02_CaptureLayout3 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.Page02_CaptureLayout3.setObjectName(u"Page02_CaptureLayout3")
        self.Page02_CaptureLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page02_CaptureLabel3 = QLabel(self.horizontalLayoutWidget_15)
        self.Page02_CaptureLabel3.setObjectName(u"Page02_CaptureLabel3")

        self.Page02_CaptureLayout3.addWidget(self.Page02_CaptureLabel3)

        self.Page02_CaptureSetButton3 = QPushButton(self.horizontalLayoutWidget_15)
        self.Page02_CaptureSetButton3.setObjectName(u"Page02_CaptureSetButton3")

        self.Page02_CaptureLayout3.addWidget(self.Page02_CaptureSetButton3)

        self.Page02_CaptureReleaseButton3 = QPushButton(self.horizontalLayoutWidget_15)
        self.Page02_CaptureReleaseButton3.setObjectName(u"Page02_CaptureReleaseButton3")

        self.Page02_CaptureLayout3.addWidget(self.Page02_CaptureReleaseButton3)

        self.horizontalLayoutWidget_16 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage3 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.Page02_CameraImage3.setObjectName(u"Page02_CameraImage3")
        self.Page02_CameraImage3.setContentsMargins(0, 0, 0, 0)
        self.Page02_ImageLabel3 = QLabel(self.horizontalLayoutWidget_16)
        self.Page02_ImageLabel3.setObjectName(u"Page02_ImageLabel3")

        self.Page02_CameraImage3.addWidget(self.Page02_ImageLabel3)

        self.horizontalLayoutWidget_31 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_31.setObjectName(u"horizontalLayoutWidget_31")
        self.horizontalLayoutWidget_31.setGeometry(QRect(570, 440, 201, 31))
        self.Page02_VideoLayout3 = QHBoxLayout(self.horizontalLayoutWidget_31)
        self.Page02_VideoLayout3.setObjectName(u"Page02_VideoLayout3")
        self.Page02_VideoLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page02_Videolabel3 = QLabel(self.horizontalLayoutWidget_31)
        self.Page02_Videolabel3.setObjectName(u"Page02_Videolabel3")

        self.Page02_VideoLayout3.addWidget(self.Page02_Videolabel3)

        self.Page02_VideoStopButton3 = QPushButton(self.horizontalLayoutWidget_31)
        self.Page02_VideoStopButton3.setObjectName(u"Page02_VideoStopButton3")

        self.Page02_VideoLayout3.addWidget(self.Page02_VideoStopButton3)

        self.Page02_VideoPlayButton3 = QPushButton(self.horizontalLayoutWidget_31)
        self.Page02_VideoPlayButton3.setObjectName(u"Page02_VideoPlayButton3")

        self.Page02_VideoLayout3.addWidget(self.Page02_VideoPlayButton3)

        self.Page02_scrollArea3 = QScrollArea(self.tab_3)
        self.Page02_scrollArea3.setObjectName(u"Page02_scrollArea3")
        self.Page02_scrollArea3.setGeometry(QRect(0, 430, 531, 71))
        self.Page02_scrollArea3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 512, 167))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Page02_setOKImageLayout3 = QHBoxLayout()
        self.Page02_setOKImageLayout3.setObjectName(u"Page02_setOKImageLayout3")
        self.Page02_setOKImageLabel3 = QLabel(self.scrollAreaWidgetContents_5)
        self.Page02_setOKImageLabel3.setObjectName(u"Page02_setOKImageLabel3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_setOKImageLabel3)

        self.Page02_setOKImagelineEdit3 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.Page02_setOKImagelineEdit3.setObjectName(u"Page02_setOKImagelineEdit3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_setOKImagelineEdit3)

        self.Page02_setOKImagebutton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_setOKImagebutton3.setObjectName(u"Page02_setOKImagebutton3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_setOKImagebutton3)

        self.Page02_OKImageSaveButton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_OKImageSaveButton3.setObjectName(u"Page02_OKImageSaveButton3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_OKImageSaveButton3)


        self.verticalLayout_5.addLayout(self.Page02_setOKImageLayout3)

        self.Page02_setNGImageLayout3 = QHBoxLayout()
        self.Page02_setNGImageLayout3.setObjectName(u"Page02_setNGImageLayout3")
        self.Page02_setNGImageLabel3 = QLabel(self.scrollAreaWidgetContents_5)
        self.Page02_setNGImageLabel3.setObjectName(u"Page02_setNGImageLabel3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_setNGImageLabel3)

        self.Page02_setNGImagelineEdit3 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.Page02_setNGImagelineEdit3.setObjectName(u"Page02_setNGImagelineEdit3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_setNGImagelineEdit3)

        self.Page02_setNGImagebutton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_setNGImagebutton3.setObjectName(u"Page02_setNGImagebutton3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_setNGImagebutton3)

        self.Page02_NGImageSaveButton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_NGImageSaveButton3.setObjectName(u"Page02_NGImageSaveButton3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_NGImageSaveButton3)


        self.verticalLayout_5.addLayout(self.Page02_setNGImageLayout3)

        self.Page02_setAImageLayout3 = QHBoxLayout()
        self.Page02_setAImageLayout3.setObjectName(u"Page02_setAImageLayout3")
        self.Page02_setAImageLabel3 = QLabel(self.scrollAreaWidgetContents_5)
        self.Page02_setAImageLabel3.setObjectName(u"Page02_setAImageLabel3")

        self.Page02_setAImageLayout3.addWidget(self.Page02_setAImageLabel3)

        self.Page02_setAImagelineEdit3 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.Page02_setAImagelineEdit3.setObjectName(u"Page02_setAImagelineEdit3")

        self.Page02_setAImageLayout3.addWidget(self.Page02_setAImagelineEdit3)

        self.Page02_setAImagebutton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_setAImagebutton3.setObjectName(u"Page02_setAImagebutton3")

        self.Page02_setAImageLayout3.addWidget(self.Page02_setAImagebutton3)

        self.Page02_AImageSaveButton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_AImageSaveButton3.setObjectName(u"Page02_AImageSaveButton3")

        self.Page02_setAImageLayout3.addWidget(self.Page02_AImageSaveButton3)


        self.verticalLayout_5.addLayout(self.Page02_setAImageLayout3)

        self.Page02_setBImageLayout3 = QHBoxLayout()
        self.Page02_setBImageLayout3.setObjectName(u"Page02_setBImageLayout3")
        self.Page02_setBImageLabel3 = QLabel(self.scrollAreaWidgetContents_5)
        self.Page02_setBImageLabel3.setObjectName(u"Page02_setBImageLabel3")

        self.Page02_setBImageLayout3.addWidget(self.Page02_setBImageLabel3)

        self.Page02_setBImagelineEdit3 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.Page02_setBImagelineEdit3.setObjectName(u"Page02_setBImagelineEdit3")

        self.Page02_setBImageLayout3.addWidget(self.Page02_setBImagelineEdit3)

        self.Page02_setBImagebutton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_setBImagebutton3.setObjectName(u"Page02_setBImagebutton3")

        self.Page02_setBImageLayout3.addWidget(self.Page02_setBImagebutton3)

        self.Page02_BImageSaveButton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_BImageSaveButton3.setObjectName(u"Page02_BImageSaveButton3")

        self.Page02_setBImageLayout3.addWidget(self.Page02_BImageSaveButton3)


        self.verticalLayout_5.addLayout(self.Page02_setBImageLayout3)

        self.Page02_setCImageLayout3 = QHBoxLayout()
        self.Page02_setCImageLayout3.setObjectName(u"Page02_setCImageLayout3")
        self.Page02_setCImageLabel3 = QLabel(self.scrollAreaWidgetContents_5)
        self.Page02_setCImageLabel3.setObjectName(u"Page02_setCImageLabel3")

        self.Page02_setCImageLayout3.addWidget(self.Page02_setCImageLabel3)

        self.Page02_setCImagelineEdit3 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.Page02_setCImagelineEdit3.setObjectName(u"Page02_setCImagelineEdit3")

        self.Page02_setCImageLayout3.addWidget(self.Page02_setCImagelineEdit3)

        self.Page02_setCImagebutton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_setCImagebutton3.setObjectName(u"Page02_setCImagebutton3")

        self.Page02_setCImageLayout3.addWidget(self.Page02_setCImagebutton3)

        self.Page02_CImageSaveButton3 = QPushButton(self.scrollAreaWidgetContents_5)
        self.Page02_CImageSaveButton3.setObjectName(u"Page02_CImageSaveButton3")

        self.Page02_setCImageLayout3.addWidget(self.Page02_CImageSaveButton3)


        self.verticalLayout_5.addLayout(self.Page02_setCImageLayout3)

        self.Page02_scrollArea3.setWidget(self.scrollAreaWidgetContents_5)
        self.CameratabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayoutWidget_19 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(570, 470, 201, 31))
        self.Page02_CaptureLayout4 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.Page02_CaptureLayout4.setObjectName(u"Page02_CaptureLayout4")
        self.Page02_CaptureLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page02_CaptureLabel4 = QLabel(self.horizontalLayoutWidget_19)
        self.Page02_CaptureLabel4.setObjectName(u"Page02_CaptureLabel4")

        self.Page02_CaptureLayout4.addWidget(self.Page02_CaptureLabel4)

        self.Page02_CaptureSetButton4 = QPushButton(self.horizontalLayoutWidget_19)
        self.Page02_CaptureSetButton4.setObjectName(u"Page02_CaptureSetButton4")

        self.Page02_CaptureLayout4.addWidget(self.Page02_CaptureSetButton4)

        self.Page02_CaptureReleaseButton4 = QPushButton(self.horizontalLayoutWidget_19)
        self.Page02_CaptureReleaseButton4.setObjectName(u"Page02_CaptureReleaseButton4")

        self.Page02_CaptureLayout4.addWidget(self.Page02_CaptureReleaseButton4)

        self.horizontalLayoutWidget_20 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage4 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.Page02_CameraImage4.setObjectName(u"Page02_CameraImage4")
        self.Page02_CameraImage4.setContentsMargins(0, 0, 0, 0)
        self.Page02_ImageLabel4 = QLabel(self.horizontalLayoutWidget_20)
        self.Page02_ImageLabel4.setObjectName(u"Page02_ImageLabel4")

        self.Page02_CameraImage4.addWidget(self.Page02_ImageLabel4)

        self.horizontalLayoutWidget_30 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_30.setObjectName(u"horizontalLayoutWidget_30")
        self.horizontalLayoutWidget_30.setGeometry(QRect(570, 440, 201, 31))
        self.Page02_VideoLayout4 = QHBoxLayout(self.horizontalLayoutWidget_30)
        self.Page02_VideoLayout4.setObjectName(u"Page02_VideoLayout4")
        self.Page02_VideoLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page02_Videolabel4 = QLabel(self.horizontalLayoutWidget_30)
        self.Page02_Videolabel4.setObjectName(u"Page02_Videolabel4")

        self.Page02_VideoLayout4.addWidget(self.Page02_Videolabel4)

        self.Page02_VideoStopButton4 = QPushButton(self.horizontalLayoutWidget_30)
        self.Page02_VideoStopButton4.setObjectName(u"Page02_VideoStopButton4")

        self.Page02_VideoLayout4.addWidget(self.Page02_VideoStopButton4)

        self.Page02_VideoPlayButton4 = QPushButton(self.horizontalLayoutWidget_30)
        self.Page02_VideoPlayButton4.setObjectName(u"Page02_VideoPlayButton4")

        self.Page02_VideoLayout4.addWidget(self.Page02_VideoPlayButton4)

        self.Page02_scrollArea4 = QScrollArea(self.tab_4)
        self.Page02_scrollArea4.setObjectName(u"Page02_scrollArea4")
        self.Page02_scrollArea4.setGeometry(QRect(0, 430, 531, 71))
        self.Page02_scrollArea4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 512, 167))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Page02_setOKImageLayout4 = QHBoxLayout()
        self.Page02_setOKImageLayout4.setObjectName(u"Page02_setOKImageLayout4")
        self.Page02_setOKImageLabel4 = QLabel(self.scrollAreaWidgetContents_6)
        self.Page02_setOKImageLabel4.setObjectName(u"Page02_setOKImageLabel4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_setOKImageLabel4)

        self.Page02_setOKImagelineEdit4 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.Page02_setOKImagelineEdit4.setObjectName(u"Page02_setOKImagelineEdit4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_setOKImagelineEdit4)

        self.Page02_setOKImagebutton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_setOKImagebutton4.setObjectName(u"Page02_setOKImagebutton4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_setOKImagebutton4)

        self.Page02_OKImageSaveButton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_OKImageSaveButton4.setObjectName(u"Page02_OKImageSaveButton4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_OKImageSaveButton4)


        self.verticalLayout_6.addLayout(self.Page02_setOKImageLayout4)

        self.Page02_setNGImageLayout4 = QHBoxLayout()
        self.Page02_setNGImageLayout4.setObjectName(u"Page02_setNGImageLayout4")
        self.Page02_setNGImageLabel4 = QLabel(self.scrollAreaWidgetContents_6)
        self.Page02_setNGImageLabel4.setObjectName(u"Page02_setNGImageLabel4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_setNGImageLabel4)

        self.Page02_setNGImagelineEdit4 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.Page02_setNGImagelineEdit4.setObjectName(u"Page02_setNGImagelineEdit4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_setNGImagelineEdit4)

        self.Page02_setNGImagebutton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_setNGImagebutton4.setObjectName(u"Page02_setNGImagebutton4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_setNGImagebutton4)

        self.Page02_NGImageSaveButton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_NGImageSaveButton4.setObjectName(u"Page02_NGImageSaveButton4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_NGImageSaveButton4)


        self.verticalLayout_6.addLayout(self.Page02_setNGImageLayout4)

        self.Page02_setAImageLayout4 = QHBoxLayout()
        self.Page02_setAImageLayout4.setObjectName(u"Page02_setAImageLayout4")
        self.Page02_setAImageLabel4 = QLabel(self.scrollAreaWidgetContents_6)
        self.Page02_setAImageLabel4.setObjectName(u"Page02_setAImageLabel4")

        self.Page02_setAImageLayout4.addWidget(self.Page02_setAImageLabel4)

        self.Page02_setAImagelineEdit4 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.Page02_setAImagelineEdit4.setObjectName(u"Page02_setAImagelineEdit4")

        self.Page02_setAImageLayout4.addWidget(self.Page02_setAImagelineEdit4)

        self.Page02_setAImagebutton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_setAImagebutton4.setObjectName(u"Page02_setAImagebutton4")

        self.Page02_setAImageLayout4.addWidget(self.Page02_setAImagebutton4)

        self.Page02_AImageSaveButton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_AImageSaveButton4.setObjectName(u"Page02_AImageSaveButton4")

        self.Page02_setAImageLayout4.addWidget(self.Page02_AImageSaveButton4)


        self.verticalLayout_6.addLayout(self.Page02_setAImageLayout4)

        self.Page02_setBImageLayout4 = QHBoxLayout()
        self.Page02_setBImageLayout4.setObjectName(u"Page02_setBImageLayout4")
        self.Page02_setBImageLabel4 = QLabel(self.scrollAreaWidgetContents_6)
        self.Page02_setBImageLabel4.setObjectName(u"Page02_setBImageLabel4")

        self.Page02_setBImageLayout4.addWidget(self.Page02_setBImageLabel4)

        self.Page02_setBImagelineEdit4 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.Page02_setBImagelineEdit4.setObjectName(u"Page02_setBImagelineEdit4")

        self.Page02_setBImageLayout4.addWidget(self.Page02_setBImagelineEdit4)

        self.Page02_setBImagebutton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_setBImagebutton4.setObjectName(u"Page02_setBImagebutton4")

        self.Page02_setBImageLayout4.addWidget(self.Page02_setBImagebutton4)

        self.Page02_BImageSaveButton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_BImageSaveButton4.setObjectName(u"Page02_BImageSaveButton4")

        self.Page02_setBImageLayout4.addWidget(self.Page02_BImageSaveButton4)


        self.verticalLayout_6.addLayout(self.Page02_setBImageLayout4)

        self.Page02_setCImageLayout4 = QHBoxLayout()
        self.Page02_setCImageLayout4.setObjectName(u"Page02_setCImageLayout4")
        self.Page02_setCImageLabel4 = QLabel(self.scrollAreaWidgetContents_6)
        self.Page02_setCImageLabel4.setObjectName(u"Page02_setCImageLabel4")

        self.Page02_setCImageLayout4.addWidget(self.Page02_setCImageLabel4)

        self.Page02_setCImagelineEdit4 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.Page02_setCImagelineEdit4.setObjectName(u"Page02_setCImagelineEdit4")

        self.Page02_setCImageLayout4.addWidget(self.Page02_setCImagelineEdit4)

        self.Page02_setCImagebutton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_setCImagebutton4.setObjectName(u"Page02_setCImagebutton4")

        self.Page02_setCImageLayout4.addWidget(self.Page02_setCImagebutton4)

        self.Page02_CImageSaveButton4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.Page02_CImageSaveButton4.setObjectName(u"Page02_CImageSaveButton4")

        self.Page02_setCImageLayout4.addWidget(self.Page02_CImageSaveButton4)


        self.verticalLayout_6.addLayout(self.Page02_setCImageLayout4)

        self.Page02_scrollArea4.setWidget(self.scrollAreaWidgetContents_6)
        self.CameratabWidget.addTab(self.tab_4, "")
        self.stackedWidget.addWidget(self.Page02)
        self.Page03 = QWidget()
        self.Page03.setObjectName(u"Page03")
        self.Page03_groupBox1 = QGroupBox(self.Page03)
        self.Page03_groupBox1.setObjectName(u"Page03_groupBox1")
        self.Page03_groupBox1.setGeometry(QRect(0, 10, 791, 61))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush16 = QBrush(QColor(89, 89, 89, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush16)
        brush17 = QBrush(QColor(133, 133, 133, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush17)
        brush18 = QBrush(QColor(111, 111, 111, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush18)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush5)
        brush19 = QBrush(QColor(59, 59, 59, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush19)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush18)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush17)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush18)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush19)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.Page03_groupBox1.setPalette(palette2)
        self.horizontalLayoutWidget_22 = QWidget(self.Page03_groupBox1)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(390, 10, 391, 31))
        self.Page03_RecordLayout1 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.Page03_RecordLayout1.setObjectName(u"Page03_RecordLayout1")
        self.Page03_RecordLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel1 = QLabel(self.horizontalLayoutWidget_22)
        self.Page03_RecordCapLabel1.setObjectName(u"Page03_RecordCapLabel1")
        self.Page03_RecordCapLabel1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordCapLabel1)

        self.Page03_RecordCapSpinBox1 = QSpinBox(self.horizontalLayoutWidget_22)
        self.Page03_RecordCapSpinBox1.setObjectName(u"Page03_RecordCapSpinBox1")
        self.Page03_RecordCapSpinBox1.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Page03_RecordCapSpinBox1.setValue(20)
        self.Page03_RecordCapSpinBox1.setRange(5, 99 * 1024) # max: 99GB

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordCapSpinBox1)

        self.Page03_RecordStartButton1 = QPushButton(self.horizontalLayoutWidget_22)
        self.Page03_RecordStartButton1.setObjectName(u"Page03_RecordStartButton1")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordStartButton1.setPalette(palette3)

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordStartButton1)

        self.Page03_RecordEndButton1 = QPushButton(self.horizontalLayoutWidget_22)
        self.Page03_RecordEndButton1.setObjectName(u"Page03_RecordEndButton1")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordEndButton1.setPalette(palette4)

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordEndButton1)

        self.horizontalLayoutWidget_21 = QWidget(self.Page03_groupBox1)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(650, 40, 131, 21))
        self.Page03_RecordStatusLayout1 = QHBoxLayout(self.horizontalLayoutWidget_21)
        self.Page03_RecordStatusLayout1.setObjectName(u"Page03_RecordStatusLayout1")
        self.Page03_RecordStatusLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordStatusTitle1 = QLabel(self.horizontalLayoutWidget_21)
        self.Page03_RecordStatusTitle1.setObjectName(u"Page03_RecordStatusTitle1")
        self.Page03_RecordStatusTitle1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout1.addWidget(self.Page03_RecordStatusTitle1)

        self.Page03_RecordStatuslabel1 = QLabel(self.horizontalLayoutWidget_21)
        self.Page03_RecordStatuslabel1.setObjectName(u"Page03_RecordStatuslabel1")
        self.Page03_RecordStatuslabel1.setTextFormat(Qt.AutoText)
        self.Page03_RecordStatuslabel1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout1.addWidget(self.Page03_RecordStatuslabel1)

        self.horizontalLayoutWidget_23 = QWidget(self.Page03_groupBox1)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(10, 10, 371, 31))
        self.Page03_setVideoDirLayout1 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirLayout1.setObjectName(u"Page03_setVideoDirLayout1")
        self.Page03_setVideoDirLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel1 = QLabel(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirLabel1.setObjectName(u"Page03_setVideoDirLabel1")

        self.Page03_setVideoDirLayout1.addWidget(self.Page03_setVideoDirLabel1)

        self.Page03_setVideoDirlineEdit1 = QLineEdit(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirlineEdit1.setObjectName(u"Page03_setVideoDirlineEdit1")
        self.Page03_setVideoDirlineEdit1.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page03_setVideoDirLayout1.addWidget(self.Page03_setVideoDirlineEdit1)

        self.Page03_setVideoDirbutton1 = QPushButton(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirbutton1.setObjectName(u"Page03_setVideoDirbutton1")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_setVideoDirbutton1.setPalette(palette5)

        self.Page03_setVideoDirLayout1.addWidget(self.Page03_setVideoDirbutton1)

        self.Page03_groupBox2 = QGroupBox(self.Page03)
        self.Page03_groupBox2.setObjectName(u"Page03_groupBox2")
        self.Page03_groupBox2.setGeometry(QRect(0, 80, 791, 61))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush19)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush19)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush19)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.Page03_groupBox2.setPalette(palette6)
        self.horizontalLayoutWidget_24 = QWidget(self.Page03_groupBox2)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(390, 10, 391, 31))
        self.Page03_RecordLayout2 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.Page03_RecordLayout2.setObjectName(u"Page03_RecordLayout2")
        self.Page03_RecordLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel2 = QLabel(self.horizontalLayoutWidget_24)
        self.Page03_RecordCapLabel2.setObjectName(u"Page03_RecordCapLabel2")
        self.Page03_RecordCapLabel2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordCapLabel2)

        self.Page03_RecordCapSpinBox2 = QSpinBox(self.horizontalLayoutWidget_24)
        self.Page03_RecordCapSpinBox2.setObjectName(u"Page03_RecordCapSpinBox2")
        self.Page03_RecordCapSpinBox2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Page03_RecordCapSpinBox2.setValue(20)
        self.Page03_RecordCapSpinBox2.setRange(5, 99 * 1024)  # max: 99GB

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordCapSpinBox2)

        self.Page03_RecordStartButton2 = QPushButton(self.horizontalLayoutWidget_24)
        self.Page03_RecordStartButton2.setObjectName(u"Page03_RecordStartButton2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordStartButton2.setPalette(palette7)

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordStartButton2)

        self.Page03_RecordEndButton2 = QPushButton(self.horizontalLayoutWidget_24)
        self.Page03_RecordEndButton2.setObjectName(u"Page03_RecordEndButton2")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordEndButton2.setPalette(palette8)

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordEndButton2)

        self.horizontalLayoutWidget_25 = QWidget(self.Page03_groupBox2)
        self.horizontalLayoutWidget_25.setObjectName(u"horizontalLayoutWidget_25")
        self.horizontalLayoutWidget_25.setGeometry(QRect(650, 40, 131, 21))
        self.Page03_RecordStatusLayout2 = QHBoxLayout(self.horizontalLayoutWidget_25)
        self.Page03_RecordStatusLayout2.setObjectName(u"Page03_RecordStatusLayout2")
        self.Page03_RecordStatusLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordStatusTitle2 = QLabel(self.horizontalLayoutWidget_25)
        self.Page03_RecordStatusTitle2.setObjectName(u"Page03_RecordStatusTitle2")
        self.Page03_RecordStatusTitle2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout2.addWidget(self.Page03_RecordStatusTitle2)

        self.Page03_RecordStatuslabel2 = QLabel(self.horizontalLayoutWidget_25)
        self.Page03_RecordStatuslabel2.setObjectName(u"Page03_RecordStatuslabel2")
        self.Page03_RecordStatuslabel2.setTextFormat(Qt.AutoText)
        self.Page03_RecordStatuslabel2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout2.addWidget(self.Page03_RecordStatuslabel2)

        self.horizontalLayoutWidget_26 = QWidget(self.Page03_groupBox2)
        self.horizontalLayoutWidget_26.setObjectName(u"horizontalLayoutWidget_26")
        self.horizontalLayoutWidget_26.setGeometry(QRect(10, 10, 371, 31))
        self.Page03_setVideoDirLayout2 = QHBoxLayout(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirLayout2.setObjectName(u"Page03_setVideoDirLayout2")
        self.Page03_setVideoDirLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel2 = QLabel(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirLabel2.setObjectName(u"Page03_setVideoDirLabel2")

        self.Page03_setVideoDirLayout2.addWidget(self.Page03_setVideoDirLabel2)

        self.Page03_setVideoDirlineEdit2 = QLineEdit(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirlineEdit2.setObjectName(u"Page03_setVideoDirlineEdit2")
        self.Page03_setVideoDirlineEdit2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page03_setVideoDirLayout2.addWidget(self.Page03_setVideoDirlineEdit2)

        self.Page03_setVideoDirbutton2 = QPushButton(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirbutton2.setObjectName(u"Page03_setVideoDirbutton2")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_setVideoDirbutton2.setPalette(palette9)

        self.Page03_setVideoDirLayout2.addWidget(self.Page03_setVideoDirbutton2)

        self.Page03_groupBox3 = QGroupBox(self.Page03)
        self.Page03_groupBox3.setObjectName(u"Page03_groupBox3")
        self.Page03_groupBox3.setGeometry(QRect(0, 150, 791, 61))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush17)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush18)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush19)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush17)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush18)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush19)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush19)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.Page03_groupBox3.setPalette(palette10)
        self.horizontalLayoutWidget_27 = QWidget(self.Page03_groupBox3)
        self.horizontalLayoutWidget_27.setObjectName(u"horizontalLayoutWidget_27")
        self.horizontalLayoutWidget_27.setGeometry(QRect(390, 10, 391, 31))
        self.Page03_RecordLayout3 = QHBoxLayout(self.horizontalLayoutWidget_27)
        self.Page03_RecordLayout3.setObjectName(u"Page03_RecordLayout3")
        self.Page03_RecordLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel3 = QLabel(self.horizontalLayoutWidget_27)
        self.Page03_RecordCapLabel3.setObjectName(u"Page03_RecordCapLabel3")
        self.Page03_RecordCapLabel3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordCapLabel3)

        self.Page03_RecordCapSpinBox3 = QSpinBox(self.horizontalLayoutWidget_27)
        self.Page03_RecordCapSpinBox3.setObjectName(u"Page03_RecordCapSpinBox3")
        self.Page03_RecordCapSpinBox3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Page03_RecordCapSpinBox3.setValue(20)
        self.Page03_RecordCapSpinBox3.setRange(5, 99 * 1024)  # max: 99GB

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordCapSpinBox3)

        self.Page03_RecordStartButton3 = QPushButton(self.horizontalLayoutWidget_27)
        self.Page03_RecordStartButton3.setObjectName(u"Page03_RecordStartButton3")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordStartButton3.setPalette(palette11)

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordStartButton3)

        self.Page03_RecordEndButton3 = QPushButton(self.horizontalLayoutWidget_27)
        self.Page03_RecordEndButton3.setObjectName(u"Page03_RecordEndButton3")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordEndButton3.setPalette(palette12)

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordEndButton3)

        self.horizontalLayoutWidget_28 = QWidget(self.Page03_groupBox3)
        self.horizontalLayoutWidget_28.setObjectName(u"horizontalLayoutWidget_28")
        self.horizontalLayoutWidget_28.setGeometry(QRect(650, 40, 131, 21))
        self.Page03_RecordStatusLayout3 = QHBoxLayout(self.horizontalLayoutWidget_28)
        self.Page03_RecordStatusLayout3.setObjectName(u"Page03_RecordStatusLayout3")
        self.Page03_RecordStatusLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordStatusTitle3 = QLabel(self.horizontalLayoutWidget_28)
        self.Page03_RecordStatusTitle3.setObjectName(u"Page03_RecordStatusTitle3")
        self.Page03_RecordStatusTitle3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout3.addWidget(self.Page03_RecordStatusTitle3)

        self.Page03_RecordStatuslabel3 = QLabel(self.horizontalLayoutWidget_28)
        self.Page03_RecordStatuslabel3.setObjectName(u"Page03_RecordStatuslabel3")
        self.Page03_RecordStatuslabel3.setTextFormat(Qt.AutoText)
        self.Page03_RecordStatuslabel3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout3.addWidget(self.Page03_RecordStatuslabel3)

        self.horizontalLayoutWidget_29 = QWidget(self.Page03_groupBox3)
        self.horizontalLayoutWidget_29.setObjectName(u"horizontalLayoutWidget_29")
        self.horizontalLayoutWidget_29.setGeometry(QRect(10, 10, 371, 31))
        self.Page03_setVideoDirLayout3 = QHBoxLayout(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirLayout3.setObjectName(u"Page03_setVideoDirLayout3")
        self.Page03_setVideoDirLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel3 = QLabel(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirLabel3.setObjectName(u"Page03_setVideoDirLabel3")

        self.Page03_setVideoDirLayout3.addWidget(self.Page03_setVideoDirLabel3)

        self.Page03_setVideoDirlineEdit3 = QLineEdit(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirlineEdit3.setObjectName(u"Page03_setVideoDirlineEdit3")
        self.Page03_setVideoDirlineEdit3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page03_setVideoDirLayout3.addWidget(self.Page03_setVideoDirlineEdit3)

        self.Page03_setVideoDirbutton3 = QPushButton(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirbutton3.setObjectName(u"Page03_setVideoDirbutton3")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_setVideoDirbutton3.setPalette(palette13)

        self.Page03_setVideoDirLayout3.addWidget(self.Page03_setVideoDirbutton3)

        self.Page03_groupBox4 = QGroupBox(self.Page03)
        self.Page03_groupBox4.setObjectName(u"Page03_groupBox4")
        self.Page03_groupBox4.setGeometry(QRect(0, 220, 791, 61))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush17)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush18)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush19)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush18)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush19)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush18)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush19)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.Page03_groupBox4.setPalette(palette14)
        self.horizontalLayoutWidget_62 = QWidget(self.Page03_groupBox4)
        self.horizontalLayoutWidget_62.setObjectName(u"horizontalLayoutWidget_62")
        self.horizontalLayoutWidget_62.setGeometry(QRect(390, 10, 391, 31))
        self.Page03_RecordLayout4 = QHBoxLayout(self.horizontalLayoutWidget_62)
        self.Page03_RecordLayout4.setObjectName(u"Page03_RecordLayout4")
        self.Page03_RecordLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel4 = QLabel(self.horizontalLayoutWidget_62)
        self.Page03_RecordCapLabel4.setObjectName(u"Page03_RecordCapLabel4")
        self.Page03_RecordCapLabel4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordCapLabel4)

        self.Page03_RecordCapSpinBox4 = QSpinBox(self.horizontalLayoutWidget_62)
        self.Page03_RecordCapSpinBox4.setObjectName(u"Page03_RecordCapSpinBox4")
        self.Page03_RecordCapSpinBox4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Page03_RecordCapSpinBox4.setValue(20)
        self.Page03_RecordCapSpinBox4.setRange(5, 99 * 1024)  # max: 99GB

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordCapSpinBox4)

        self.Page03_RecordStartButton4 = QPushButton(self.horizontalLayoutWidget_62)
        self.Page03_RecordStartButton4.setObjectName(u"Page03_RecordStartButton4")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordStartButton4.setPalette(palette15)

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordStartButton4)

        self.Page03_RecordEndButton4 = QPushButton(self.horizontalLayoutWidget_62)
        self.Page03_RecordEndButton4.setObjectName(u"Page03_RecordEndButton4")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_RecordEndButton4.setPalette(palette16)

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordEndButton4)

        self.horizontalLayoutWidget_63 = QWidget(self.Page03_groupBox4)
        self.horizontalLayoutWidget_63.setObjectName(u"horizontalLayoutWidget_63")
        self.horizontalLayoutWidget_63.setGeometry(QRect(650, 40, 131, 21))
        self.Page03_RecordStatusLayout4 = QHBoxLayout(self.horizontalLayoutWidget_63)
        self.Page03_RecordStatusLayout4.setObjectName(u"Page03_RecordStatusLayout4")
        self.Page03_RecordStatusLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordStatusTitle4 = QLabel(self.horizontalLayoutWidget_63)
        self.Page03_RecordStatusTitle4.setObjectName(u"Page03_RecordStatusTitle4")
        self.Page03_RecordStatusTitle4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout4.addWidget(self.Page03_RecordStatusTitle4)

        self.Page03_RecordStatuslabel4 = QLabel(self.horizontalLayoutWidget_63)
        self.Page03_RecordStatuslabel4.setObjectName(u"Page03_RecordStatuslabel4")
        self.Page03_RecordStatuslabel4.setTextFormat(Qt.AutoText)
        self.Page03_RecordStatuslabel4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Page03_RecordStatusLayout4.addWidget(self.Page03_RecordStatuslabel4)

        self.horizontalLayoutWidget_64 = QWidget(self.Page03_groupBox4)
        self.horizontalLayoutWidget_64.setObjectName(u"horizontalLayoutWidget_64")
        self.horizontalLayoutWidget_64.setGeometry(QRect(10, 10, 371, 31))
        self.Page03_setVideoDirLayout4 = QHBoxLayout(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirLayout4.setObjectName(u"Page03_setVideoDirLayout4")
        self.Page03_setVideoDirLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel4 = QLabel(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirLabel4.setObjectName(u"Page03_setVideoDirLabel4")

        self.Page03_setVideoDirLayout4.addWidget(self.Page03_setVideoDirLabel4)

        self.Page03_setVideoDirlineEdit4 = QLineEdit(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirlineEdit4.setObjectName(u"Page03_setVideoDirlineEdit4")
        self.Page03_setVideoDirlineEdit4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page03_setVideoDirLayout4.addWidget(self.Page03_setVideoDirlineEdit4)

        self.Page03_setVideoDirbutton4 = QPushButton(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirbutton4.setObjectName(u"Page03_setVideoDirbutton4")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Page03_setVideoDirbutton4.setPalette(palette17)

        self.Page03_setVideoDirLayout4.addWidget(self.Page03_setVideoDirbutton4)

        self.stackedWidget.addWidget(self.Page03)
        self.Page04 = QWidget()
        self.Page04.setObjectName(u"Page04")
        self.horizontalLayoutWidget_7 = QWidget(self.Page04)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 0, 751, 421))
        self.Page04_VideoImage = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.Page04_VideoImage.setObjectName(u"Page04_VideoImage")
        self.Page04_VideoImage.setContentsMargins(0, 0, 0, 0)
        self.Page04_ImageLabel = QLabel(self.horizontalLayoutWidget_7)
        self.Page04_ImageLabel.setObjectName(u"Page04_ImageLabel")
        self.Page04_ImageLabel.setStyleSheet(u"background-color: rgb(200, 200, 200);")

        self.Page04_VideoImage.addWidget(self.Page04_ImageLabel)

        self.Page04_scrollArea = QScrollArea(self.Page04)
        self.Page04_scrollArea.setObjectName(u"Page04_scrollArea")
        self.Page04_scrollArea.setGeometry(QRect(400, 460, 391, 71))
        self.Page04_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 372, 167))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Page04_setOKImageLayout = QHBoxLayout()
        self.Page04_setOKImageLayout.setObjectName(u"Page04_setOKImageLayout")
        self.Page04_setOKImageLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.Page04_setOKImageLabel.setObjectName(u"Page04_setOKImageLabel")

        self.Page04_setOKImageLayout.addWidget(self.Page04_setOKImageLabel)

        self.Page04_setOKImagelineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Page04_setOKImagelineEdit.setObjectName(u"Page04_setOKImagelineEdit")

        self.Page04_setOKImageLayout.addWidget(self.Page04_setOKImagelineEdit)

        self.Page04_setOKImagebutton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_setOKImagebutton.setObjectName(u"Page04_setOKImagebutton")
        self.Page04_setOKImagebutton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setOKImageLayout.addWidget(self.Page04_setOKImagebutton)

        self.Page04_OKImageSaveButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_OKImageSaveButton.setObjectName(u"Page04_OKImageSaveButton")
        self.Page04_OKImageSaveButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setOKImageLayout.addWidget(self.Page04_OKImageSaveButton)


        self.verticalLayout_3.addLayout(self.Page04_setOKImageLayout)

        self.Page04_setNGImageLayout = QHBoxLayout()
        self.Page04_setNGImageLayout.setObjectName(u"Page04_setNGImageLayout")
        self.Page04_setNGImageLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.Page04_setNGImageLabel.setObjectName(u"Page04_setNGImageLabel")

        self.Page04_setNGImageLayout.addWidget(self.Page04_setNGImageLabel)

        self.Page04_setNGImagelineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Page04_setNGImagelineEdit.setObjectName(u"Page04_setNGImagelineEdit")

        self.Page04_setNGImageLayout.addWidget(self.Page04_setNGImagelineEdit)

        self.Page04_setNGImagebutton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_setNGImagebutton.setObjectName(u"Page04_setNGImagebutton")
        self.Page04_setNGImagebutton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setNGImageLayout.addWidget(self.Page04_setNGImagebutton)

        self.Page04_NGImageSaveButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_NGImageSaveButton.setObjectName(u"Page04_NGImageSaveButton")
        self.Page04_NGImageSaveButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setNGImageLayout.addWidget(self.Page04_NGImageSaveButton)


        self.verticalLayout_3.addLayout(self.Page04_setNGImageLayout)

        self.Page04_setAImageLayout = QHBoxLayout()
        self.Page04_setAImageLayout.setObjectName(u"Page04_setAImageLayout")
        self.Page04_setAImageLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.Page04_setAImageLabel.setObjectName(u"Page04_setAImageLabel")

        self.Page04_setAImageLayout.addWidget(self.Page04_setAImageLabel)

        self.Page04_setAImagelineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Page04_setAImagelineEdit.setObjectName(u"Page04_setAImagelineEdit")

        self.Page04_setAImageLayout.addWidget(self.Page04_setAImagelineEdit)

        self.Page04_setAImagebutton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_setAImagebutton.setObjectName(u"Page04_setAImagebutton")
        self.Page04_setAImagebutton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setAImageLayout.addWidget(self.Page04_setAImagebutton)

        self.Page04_AImageSaveButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_AImageSaveButton.setObjectName(u"Page04_AImageSaveButton")
        self.Page04_AImageSaveButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setAImageLayout.addWidget(self.Page04_AImageSaveButton)


        self.verticalLayout_3.addLayout(self.Page04_setAImageLayout)

        self.Page04_setBImageLayout = QHBoxLayout()
        self.Page04_setBImageLayout.setObjectName(u"Page04_setBImageLayout")
        self.Page04_setBImageLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.Page04_setBImageLabel.setObjectName(u"Page04_setBImageLabel")

        self.Page04_setBImageLayout.addWidget(self.Page04_setBImageLabel)

        self.Page04_setBImagelineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Page04_setBImagelineEdit.setObjectName(u"Page04_setBImagelineEdit")

        self.Page04_setBImageLayout.addWidget(self.Page04_setBImagelineEdit)

        self.Page04_setBImagebutton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_setBImagebutton.setObjectName(u"Page04_setBImagebutton")
        self.Page04_setBImagebutton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setBImageLayout.addWidget(self.Page04_setBImagebutton)

        self.Page04_BImageSaveButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_BImageSaveButton.setObjectName(u"Page04_BImageSaveButton")
        self.Page04_BImageSaveButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setBImageLayout.addWidget(self.Page04_BImageSaveButton)


        self.verticalLayout_3.addLayout(self.Page04_setBImageLayout)

        self.Page04_setCImageLayout = QHBoxLayout()
        self.Page04_setCImageLayout.setObjectName(u"Page04_setCImageLayout")
        self.Page04_setCImageLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.Page04_setCImageLabel.setObjectName(u"Page04_setCImageLabel")

        self.Page04_setCImageLayout.addWidget(self.Page04_setCImageLabel)

        self.Page04_setCImagelineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Page04_setCImagelineEdit.setObjectName(u"Page04_setCImagelineEdit")

        self.Page04_setCImageLayout.addWidget(self.Page04_setCImagelineEdit)

        self.Page04_setCImagebutton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_setCImagebutton.setObjectName(u"Page04_setCImagebutton")
        self.Page04_setCImagebutton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setCImageLayout.addWidget(self.Page04_setCImagebutton)

        self.Page04_CImageSaveButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.Page04_CImageSaveButton.setObjectName(u"Page04_CImageSaveButton")
        self.Page04_CImageSaveButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_setCImageLayout.addWidget(self.Page04_CImageSaveButton)


        self.verticalLayout_3.addLayout(self.Page04_setCImageLayout)

        self.Page04_scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget_2 = QWidget(self.Page04)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 430, 391, 101))
        self.Page04_setClipPlayLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.Page04_setClipPlayLayout.setObjectName(u"Page04_setClipPlayLayout")
        self.Page04_setClipPlayLayout.setContentsMargins(0, 0, 0, 0)
        self.Page04_ClipPlayDirLayout = QHBoxLayout()
        self.Page04_ClipPlayDirLayout.setObjectName(u"Page04_ClipPlayDirLayout")
        self.Page04_ClipPlayDirLabel = QLabel(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayDirLabel.setObjectName(u"Page04_ClipPlayDirLabel")

        self.Page04_ClipPlayDirLayout.addWidget(self.Page04_ClipPlayDirLabel)

        self.Page04_ClipPlayDirlineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayDirlineEdit.setObjectName(u"Page04_ClipPlayDirlineEdit")
        self.Page04_ClipPlayDirlineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_ClipPlayDirLayout.addWidget(self.Page04_ClipPlayDirlineEdit)

        self.Page04_ClipPlayDirbutton = QPushButton(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayDirbutton.setObjectName(u"Page04_ClipPlayDirbutton")
        self.Page04_ClipPlayDirbutton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_ClipPlayDirLayout.addWidget(self.Page04_ClipPlayDirbutton)


        self.Page04_setClipPlayLayout.addLayout(self.Page04_ClipPlayDirLayout)

        self.Page04_ClipPlaySlideLayout = QHBoxLayout()
        self.Page04_ClipPlaySlideLayout.setObjectName(u"Page04_ClipPlaySlideLayout")
        self.Page04_ClipPlaySlider = QSlider(self.verticalLayoutWidget_2)
        self.Page04_ClipPlaySlider.setObjectName(u"Page04_ClipPlaySlider")
        self.Page04_ClipPlaySlider.setOrientation(Qt.Horizontal)

        self.Page04_ClipPlaySlideLayout.addWidget(self.Page04_ClipPlaySlider)

        self.Page04_ClipPlayFrameNumLabel = QLabel(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayFrameNumLabel.setObjectName(u"Page04_ClipPlayFrameNumLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Page04_ClipPlayFrameNumLabel.sizePolicy().hasHeightForWidth())
        self.Page04_ClipPlayFrameNumLabel.setSizePolicy(sizePolicy)
        self.Page04_ClipPlayFrameNumLabel.setMinimumSize(QSize(55, 0))
        self.Page04_ClipPlayFrameNumLabel.setBaseSize(QSize(0, 0))
        self.Page04_ClipPlayFrameNumLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page04_ClipPlaySlideLayout.addWidget(self.Page04_ClipPlayFrameNumLabel)

        self.Page04_ClipPlayFrameMaxLabel = QLabel(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayFrameMaxLabel.setObjectName(u"Page04_ClipPlayFrameMaxLabel")
        sizePolicy.setHeightForWidth(self.Page04_ClipPlayFrameMaxLabel.sizePolicy().hasHeightForWidth())
        self.Page04_ClipPlayFrameMaxLabel.setSizePolicy(sizePolicy)
        self.Page04_ClipPlayFrameMaxLabel.setMinimumSize(QSize(55, 0))

        self.Page04_ClipPlaySlideLayout.addWidget(self.Page04_ClipPlayFrameMaxLabel)


        self.Page04_setClipPlayLayout.addLayout(self.Page04_ClipPlaySlideLayout)

        self.Page04_ClipPlayButtonLayout = QHBoxLayout()
        self.Page04_ClipPlayButtonLayout.setObjectName(u"Page04_ClipPlayButtonLayout")
        self.Page04_ClipPlayButtonPlay = QPushButton(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayButtonPlay.setObjectName(u"Page04_ClipPlayButtonPlay")
        self.Page04_ClipPlayButtonPlay.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_ClipPlayButtonLayout.addWidget(self.Page04_ClipPlayButtonPlay)

        self.Page04_ClipPlayButtonPause = QPushButton(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayButtonPause.setObjectName(u"Page04_ClipPlayButtonPause")
        self.Page04_ClipPlayButtonPause.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_ClipPlayButtonLayout.addWidget(self.Page04_ClipPlayButtonPause)

        self.Page04_ClipPlayButtonBack = QPushButton(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayButtonBack.setObjectName(u"Page04_ClipPlayButtonBack")
        self.Page04_ClipPlayButtonBack.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_ClipPlayButtonLayout.addWidget(self.Page04_ClipPlayButtonBack)

        self.Page04_ClipPlayButtonForward = QPushButton(self.verticalLayoutWidget_2)
        self.Page04_ClipPlayButtonForward.setObjectName(u"Page04_ClipPlayButtonForward")
        self.Page04_ClipPlayButtonForward.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_ClipPlayButtonLayout.addWidget(self.Page04_ClipPlayButtonForward)


        self.Page04_setClipPlayLayout.addLayout(self.Page04_ClipPlayButtonLayout)

        self.horizontalLayoutWidget_8 = QWidget(self.Page04)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(580, 430, 191, 31))
        self.Page04_CaptureLayout = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.Page04_CaptureLayout.setObjectName(u"Page04_CaptureLayout")
        self.Page04_CaptureLayout.setContentsMargins(0, 0, 0, 0)
        self.Page04_CaptureLabel = QLabel(self.horizontalLayoutWidget_8)
        self.Page04_CaptureLabel.setObjectName(u"Page04_CaptureLabel")

        self.Page04_CaptureLayout.addWidget(self.Page04_CaptureLabel)

        self.Page04_CaptureSetButton = QPushButton(self.horizontalLayoutWidget_8)
        self.Page04_CaptureSetButton.setObjectName(u"Page04_CaptureSetButton")
        self.Page04_CaptureSetButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_CaptureLayout.addWidget(self.Page04_CaptureSetButton)

        self.Page04_CaptureReleaseButton = QPushButton(self.horizontalLayoutWidget_8)
        self.Page04_CaptureReleaseButton.setObjectName(u"Page04_CaptureReleaseButton")
        self.Page04_CaptureReleaseButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Page04_CaptureLayout.addWidget(self.Page04_CaptureReleaseButton)

        self.stackedWidget.addWidget(self.Page04)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(11, 10, 171, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu_LivepushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_LivepushButton.setObjectName(u"Menu_LivepushButton")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        gradient = QLinearGradient(1, 0.477, 1, 1)
        gradient.setSpread(QGradient.ReflectSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(110, 110, 110, 255))
        gradient.setColorAt(1, QColor(255, 255, 255, 255))
        brush20 = QBrush(gradient)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        gradient1 = QLinearGradient(1, 0.477, 1, 1)
        gradient1.setSpread(QGradient.ReflectSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(110, 110, 110, 255))
        gradient1.setColorAt(1, QColor(255, 255, 255, 255))
        brush21 = QBrush(gradient1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush21)
        gradient2 = QLinearGradient(1, 0.477, 1, 1)
        gradient2.setSpread(QGradient.ReflectSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(110, 110, 110, 255))
        gradient2.setColorAt(1, QColor(255, 255, 255, 255))
        brush22 = QBrush(gradient2)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush22)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        gradient3 = QLinearGradient(1, 0.477, 1, 1)
        gradient3.setSpread(QGradient.ReflectSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(110, 110, 110, 255))
        gradient3.setColorAt(1, QColor(255, 255, 255, 255))
        brush23 = QBrush(gradient3)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        gradient4 = QLinearGradient(1, 0.477, 1, 1)
        gradient4.setSpread(QGradient.ReflectSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(110, 110, 110, 255))
        gradient4.setColorAt(1, QColor(255, 255, 255, 255))
        brush24 = QBrush(gradient4)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush24)
        gradient5 = QLinearGradient(1, 0.477, 1, 1)
        gradient5.setSpread(QGradient.ReflectSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(110, 110, 110, 255))
        gradient5.setColorAt(1, QColor(255, 255, 255, 255))
        brush25 = QBrush(gradient5)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush25)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        gradient6 = QLinearGradient(1, 0.477, 1, 1)
        gradient6.setSpread(QGradient.ReflectSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(110, 110, 110, 255))
        gradient6.setColorAt(1, QColor(255, 255, 255, 255))
        brush26 = QBrush(gradient6)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        gradient7 = QLinearGradient(1, 0.477, 1, 1)
        gradient7.setSpread(QGradient.ReflectSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(110, 110, 110, 255))
        gradient7.setColorAt(1, QColor(255, 255, 255, 255))
        brush27 = QBrush(gradient7)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush27)
        gradient8 = QLinearGradient(1, 0.477, 1, 1)
        gradient8.setSpread(QGradient.ReflectSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(110, 110, 110, 255))
        gradient8.setColorAt(1, QColor(255, 255, 255, 255))
        brush28 = QBrush(gradient8)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush28)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Menu_LivepushButton.setPalette(palette18)
        font = QFont()
        font.setFamily(u"Arial Rounded MT Bold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Menu_LivepushButton.setFont(font)
        self.Menu_LivepushButton.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0.477, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.Menu_LivepushButton)

        self.Menu_CapturepushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_CapturepushButton.setObjectName(u"Menu_CapturepushButton")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        gradient9 = QLinearGradient(1, 0.477, 1, 1)
        gradient9.setSpread(QGradient.ReflectSpread)
        gradient9.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(110, 110, 110, 255))
        gradient9.setColorAt(1, QColor(255, 255, 255, 255))
        brush29 = QBrush(gradient9)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush29)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette19.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        gradient10 = QLinearGradient(1, 0.477, 1, 1)
        gradient10.setSpread(QGradient.ReflectSpread)
        gradient10.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(110, 110, 110, 255))
        gradient10.setColorAt(1, QColor(255, 255, 255, 255))
        brush30 = QBrush(gradient10)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush30)
        gradient11 = QLinearGradient(1, 0.477, 1, 1)
        gradient11.setSpread(QGradient.ReflectSpread)
        gradient11.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(110, 110, 110, 255))
        gradient11.setColorAt(1, QColor(255, 255, 255, 255))
        brush31 = QBrush(gradient11)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush31)
        palette19.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        gradient12 = QLinearGradient(1, 0.477, 1, 1)
        gradient12.setSpread(QGradient.ReflectSpread)
        gradient12.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(110, 110, 110, 255))
        gradient12.setColorAt(1, QColor(255, 255, 255, 255))
        brush32 = QBrush(gradient12)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush32)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        gradient13 = QLinearGradient(1, 0.477, 1, 1)
        gradient13.setSpread(QGradient.ReflectSpread)
        gradient13.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(110, 110, 110, 255))
        gradient13.setColorAt(1, QColor(255, 255, 255, 255))
        brush33 = QBrush(gradient13)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush33)
        gradient14 = QLinearGradient(1, 0.477, 1, 1)
        gradient14.setSpread(QGradient.ReflectSpread)
        gradient14.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(110, 110, 110, 255))
        gradient14.setColorAt(1, QColor(255, 255, 255, 255))
        brush34 = QBrush(gradient14)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush34)
        palette19.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        gradient15 = QLinearGradient(1, 0.477, 1, 1)
        gradient15.setSpread(QGradient.ReflectSpread)
        gradient15.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient15.setColorAt(0, QColor(110, 110, 110, 255))
        gradient15.setColorAt(1, QColor(255, 255, 255, 255))
        brush35 = QBrush(gradient15)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush35)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette19.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        gradient16 = QLinearGradient(1, 0.477, 1, 1)
        gradient16.setSpread(QGradient.ReflectSpread)
        gradient16.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient16.setColorAt(0, QColor(110, 110, 110, 255))
        gradient16.setColorAt(1, QColor(255, 255, 255, 255))
        brush36 = QBrush(gradient16)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush36)
        gradient17 = QLinearGradient(1, 0.477, 1, 1)
        gradient17.setSpread(QGradient.ReflectSpread)
        gradient17.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient17.setColorAt(0, QColor(110, 110, 110, 255))
        gradient17.setColorAt(1, QColor(255, 255, 255, 255))
        brush37 = QBrush(gradient17)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush37)
        palette19.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Menu_CapturepushButton.setPalette(palette19)
        font1 = QFont()
        font1.setFamily(u"Arial Rounded MT Bold")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.Menu_CapturepushButton.setFont(font1)
        self.Menu_CapturepushButton.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0.477, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.Menu_CapturepushButton)

        self.Menu_RecordpushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_RecordpushButton.setObjectName(u"Menu_RecordpushButton")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        gradient18 = QLinearGradient(1, 0.477, 1, 1)
        gradient18.setSpread(QGradient.ReflectSpread)
        gradient18.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient18.setColorAt(0, QColor(110, 110, 110, 255))
        gradient18.setColorAt(1, QColor(255, 255, 255, 255))
        brush38 = QBrush(gradient18)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush38)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette20.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        gradient19 = QLinearGradient(1, 0.477, 1, 1)
        gradient19.setSpread(QGradient.ReflectSpread)
        gradient19.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient19.setColorAt(0, QColor(110, 110, 110, 255))
        gradient19.setColorAt(1, QColor(255, 255, 255, 255))
        brush39 = QBrush(gradient19)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush39)
        gradient20 = QLinearGradient(1, 0.477, 1, 1)
        gradient20.setSpread(QGradient.ReflectSpread)
        gradient20.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient20.setColorAt(0, QColor(110, 110, 110, 255))
        gradient20.setColorAt(1, QColor(255, 255, 255, 255))
        brush40 = QBrush(gradient20)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush40)
        palette20.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        gradient21 = QLinearGradient(1, 0.477, 1, 1)
        gradient21.setSpread(QGradient.ReflectSpread)
        gradient21.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient21.setColorAt(0, QColor(110, 110, 110, 255))
        gradient21.setColorAt(1, QColor(255, 255, 255, 255))
        brush41 = QBrush(gradient21)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush41)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        gradient22 = QLinearGradient(1, 0.477, 1, 1)
        gradient22.setSpread(QGradient.ReflectSpread)
        gradient22.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient22.setColorAt(0, QColor(110, 110, 110, 255))
        gradient22.setColorAt(1, QColor(255, 255, 255, 255))
        brush42 = QBrush(gradient22)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush42)
        gradient23 = QLinearGradient(1, 0.477, 1, 1)
        gradient23.setSpread(QGradient.ReflectSpread)
        gradient23.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient23.setColorAt(0, QColor(110, 110, 110, 255))
        gradient23.setColorAt(1, QColor(255, 255, 255, 255))
        brush43 = QBrush(gradient23)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush43)
        palette20.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        gradient24 = QLinearGradient(1, 0.477, 1, 1)
        gradient24.setSpread(QGradient.ReflectSpread)
        gradient24.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient24.setColorAt(0, QColor(110, 110, 110, 255))
        gradient24.setColorAt(1, QColor(255, 255, 255, 255))
        brush44 = QBrush(gradient24)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush44)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette20.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        gradient25 = QLinearGradient(1, 0.477, 1, 1)
        gradient25.setSpread(QGradient.ReflectSpread)
        gradient25.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient25.setColorAt(0, QColor(110, 110, 110, 255))
        gradient25.setColorAt(1, QColor(255, 255, 255, 255))
        brush45 = QBrush(gradient25)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush45)
        gradient26 = QLinearGradient(1, 0.477, 1, 1)
        gradient26.setSpread(QGradient.ReflectSpread)
        gradient26.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient26.setColorAt(0, QColor(110, 110, 110, 255))
        gradient26.setColorAt(1, QColor(255, 255, 255, 255))
        brush46 = QBrush(gradient26)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush46)
        palette20.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Menu_RecordpushButton.setPalette(palette20)
        self.Menu_RecordpushButton.setFont(font)
        self.Menu_RecordpushButton.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0.477, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.Menu_RecordpushButton)

        self.Menu_ClipPlaypushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_ClipPlaypushButton.setObjectName(u"Menu_ClipPlaypushButton")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        gradient27 = QLinearGradient(1, 0.477, 1, 1)
        gradient27.setSpread(QGradient.ReflectSpread)
        gradient27.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient27.setColorAt(0, QColor(110, 110, 110, 255))
        gradient27.setColorAt(1, QColor(255, 255, 255, 255))
        brush47 = QBrush(gradient27)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush47)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette21.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        gradient28 = QLinearGradient(1, 0.477, 1, 1)
        gradient28.setSpread(QGradient.ReflectSpread)
        gradient28.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient28.setColorAt(0, QColor(110, 110, 110, 255))
        gradient28.setColorAt(1, QColor(255, 255, 255, 255))
        brush48 = QBrush(gradient28)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush48)
        gradient29 = QLinearGradient(1, 0.477, 1, 1)
        gradient29.setSpread(QGradient.ReflectSpread)
        gradient29.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient29.setColorAt(0, QColor(110, 110, 110, 255))
        gradient29.setColorAt(1, QColor(255, 255, 255, 255))
        brush49 = QBrush(gradient29)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush49)
        palette21.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        gradient30 = QLinearGradient(1, 0.477, 1, 1)
        gradient30.setSpread(QGradient.ReflectSpread)
        gradient30.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient30.setColorAt(0, QColor(110, 110, 110, 255))
        gradient30.setColorAt(1, QColor(255, 255, 255, 255))
        brush50 = QBrush(gradient30)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush50)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        gradient31 = QLinearGradient(1, 0.477, 1, 1)
        gradient31.setSpread(QGradient.ReflectSpread)
        gradient31.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient31.setColorAt(0, QColor(110, 110, 110, 255))
        gradient31.setColorAt(1, QColor(255, 255, 255, 255))
        brush51 = QBrush(gradient31)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush51)
        gradient32 = QLinearGradient(1, 0.477, 1, 1)
        gradient32.setSpread(QGradient.ReflectSpread)
        gradient32.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient32.setColorAt(0, QColor(110, 110, 110, 255))
        gradient32.setColorAt(1, QColor(255, 255, 255, 255))
        brush52 = QBrush(gradient32)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush52)
        palette21.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        gradient33 = QLinearGradient(1, 0.477, 1, 1)
        gradient33.setSpread(QGradient.ReflectSpread)
        gradient33.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient33.setColorAt(0, QColor(110, 110, 110, 255))
        gradient33.setColorAt(1, QColor(255, 255, 255, 255))
        brush53 = QBrush(gradient33)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush53)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        gradient34 = QLinearGradient(1, 0.477, 1, 1)
        gradient34.setSpread(QGradient.ReflectSpread)
        gradient34.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient34.setColorAt(0, QColor(110, 110, 110, 255))
        gradient34.setColorAt(1, QColor(255, 255, 255, 255))
        brush54 = QBrush(gradient34)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush54)
        gradient35 = QLinearGradient(1, 0.477, 1, 1)
        gradient35.setSpread(QGradient.ReflectSpread)
        gradient35.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient35.setColorAt(0, QColor(110, 110, 110, 255))
        gradient35.setColorAt(1, QColor(255, 255, 255, 255))
        brush55 = QBrush(gradient35)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush55)
        palette21.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Menu_ClipPlaypushButton.setPalette(palette21)
        self.Menu_ClipPlaypushButton.setFont(font)
        self.Menu_ClipPlaypushButton.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0.477, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.Menu_ClipPlaypushButton)

        self.MenubarLabel = QLabel(self.verticalLayoutWidget)
        self.MenubarLabel.setObjectName(u"MenubarLabel")

        self.verticalLayout.addWidget(self.MenubarLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 991, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.CameratabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Page01_Livelabel1.setText(QCoreApplication.translate("MainWindow", u"CAM 1", None))
        self.Page01_Livelabel2.setText(QCoreApplication.translate("MainWindow", u"CAM 2", None))
        self.Page01_Livelabel3.setText(QCoreApplication.translate("MainWindow", u"CAM 3", None))
        self.Page01_Livelabel4.setText(QCoreApplication.translate("MainWindow", u"CAM 4", None))
        self.Page01_LiveImagelabel1.setText("")
        self.Page01_LiveImagelabel3.setText("")
        self.Page01_LiveImagelabel2.setText("")
        self.Page01_LiveImagelabel4.setText("")
        self.Page02_ImageLabel1.setText("")
        self.Page02_CaptureLabel1.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton1.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton1.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_Videolabel1.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1", None))
        self.Page02_VideoStopButton1.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.Page02_VideoPlayButton1.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc0dd", None))
        self.Page02_setOKImageLabel1.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_OKImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_setNGImageLabel1.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_NGImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page02_setAImageLabel1.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 A:", None))
        self.Page02_setAImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_AImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setBImageLabel1.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 B:", None))
        self.Page02_setBImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_BImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setCImageLabel1.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 C:", None))
        self.Page02_setCImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"CAM1", None))
        self.Page02_ImageLabel2.setText("")
        self.Page02_CaptureLabel2.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton2.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton2.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_Videolabel2.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1", None))
        self.Page02_VideoStopButton2.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.Page02_VideoPlayButton2.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc0dd", None))
        self.Page02_setOKImageLabel2.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_OKImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_setNGImageLabel2.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_NGImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page02_setAImageLabel2.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 A:", None))
        self.Page02_setAImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_AImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setBImageLabel2.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 B:", None))
        self.Page02_setBImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_BImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setCImageLabel2.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 C:", None))
        self.Page02_setCImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"CAM2", None))
        self.Page02_CaptureLabel3.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_ImageLabel3.setText("")
        self.Page02_Videolabel3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1", None))
        self.Page02_VideoStopButton3.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.Page02_VideoPlayButton3.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc0dd", None))
        self.Page02_setOKImageLabel3.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_OKImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_setNGImageLabel3.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_NGImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page02_setAImageLabel3.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 A:", None))
        self.Page02_setAImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_AImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setBImageLabel3.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 B:", None))
        self.Page02_setBImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_BImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setCImageLabel3.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 C:", None))
        self.Page02_setCImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"CAM3", None))
        self.Page02_CaptureLabel4.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton4.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton4.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_ImageLabel4.setText("")
        self.Page02_Videolabel4.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1", None))
        self.Page02_VideoStopButton4.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.Page02_VideoPlayButton4.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc0dd", None))
        self.Page02_setOKImageLabel4.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_OKImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_setNGImageLabel4.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_NGImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page02_setAImageLabel4.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 A:", None))
        self.Page02_setAImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_AImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setBImageLabel4.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 B:", None))
        self.Page02_setBImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_BImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page02_setCImageLabel4.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 C:", None))
        self.Page02_setCImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"CAM4", None))
        self.Page03_groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"CAM1", None))
        self.Page03_RecordCapLabel1.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc6a9\ub7c9(MB)", None))
        self.Page03_RecordStartButton1.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc2dc\uc791", None))
        self.Page03_RecordEndButton1.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\ud574\uc81c", None))
        self.Page03_RecordStatusTitle1.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc0c1\ud0dc:", None))
        self.Page03_RecordStatuslabel1.setText(QCoreApplication.translate("MainWindow", u"(\ub179\ud654\ud574\uc81c)", None))
        self.Page03_setVideoDirLabel1.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1 \uc800\uc7a5\uacbd\ub85c:", None))
        self.Page03_setVideoDirbutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page03_groupBox2.setTitle(QCoreApplication.translate("MainWindow", u"CAM2", None))
        self.Page03_RecordCapLabel2.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc6a9\ub7c9(MB)", None))
        self.Page03_RecordStartButton2.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc2dc\uc791", None))
        self.Page03_RecordEndButton2.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\ud574\uc81c", None))
        self.Page03_RecordStatusTitle2.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc0c1\ud0dc:", None))
        self.Page03_RecordStatuslabel2.setText(QCoreApplication.translate("MainWindow", u"(\ub179\ud654\ud574\uc81c)", None))
        self.Page03_setVideoDirLabel2.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1 \uc800\uc7a5\uacbd\ub85c:", None))
        self.Page03_setVideoDirbutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page03_groupBox3.setTitle(QCoreApplication.translate("MainWindow", u"CAM3", None))
        self.Page03_RecordCapLabel3.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc6a9\ub7c9(MB)", None))
        self.Page03_RecordStartButton3.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc2dc\uc791", None))
        self.Page03_RecordEndButton3.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\ud574\uc81c", None))
        self.Page03_RecordStatusTitle3.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc0c1\ud0dc:", None))
        self.Page03_RecordStatuslabel3.setText(QCoreApplication.translate("MainWindow", u"(\ub179\ud654\ud574\uc81c)", None))
        self.Page03_setVideoDirLabel3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1 \uc800\uc7a5\uacbd\ub85c:", None))
        self.Page03_setVideoDirbutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page03_groupBox4.setTitle(QCoreApplication.translate("MainWindow", u"CAM4", None))
        self.Page03_RecordCapLabel4.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc6a9\ub7c9(MB)", None))
        self.Page03_RecordStartButton4.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc2dc\uc791", None))
        self.Page03_RecordEndButton4.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\ud574\uc81c", None))
        self.Page03_RecordStatusTitle4.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc0c1\ud0dc:", None))
        self.Page03_RecordStatuslabel4.setText(QCoreApplication.translate("MainWindow", u"(\ub179\ud654\ud574\uc81c)", None))
        self.Page03_setVideoDirLabel4.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1 \uc800\uc7a5\uacbd\ub85c:", None))
        self.Page03_setVideoDirbutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_ImageLabel.setText("")
        self.Page04_setOKImageLabel.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page04_setOKImagebutton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_OKImageSaveButton.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page04_setNGImageLabel.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page04_setNGImagebutton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_NGImageSaveButton.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page04_setAImageLabel.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 A:", None))
        self.Page04_setAImagebutton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_AImageSaveButton.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page04_setBImageLabel.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 B:", None))
        self.Page04_setBImagebutton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_BImageSaveButton.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page04_setCImageLabel.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 C:", None))
        self.Page04_setCImagebutton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_CImageSaveButton.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc800\uc7a5", None))
        self.Page04_ClipPlayDirLabel.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1\uacbd\ub85c:", None))
        self.Page04_ClipPlayDirbutton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page04_ClipPlayFrameNumLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Page04_ClipPlayFrameMaxLabel.setText(QCoreApplication.translate("MainWindow", u"/0", None))
        self.Page04_ClipPlayButtonPlay.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uc0dd", None))
        self.Page04_ClipPlayButtonPause.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.Page04_ClipPlayButtonBack.setText(QCoreApplication.translate("MainWindow", u"\ub4a4\ub85c", None))
        self.Page04_ClipPlayButtonForward.setText(QCoreApplication.translate("MainWindow", u"\uc55e\uc73c\ub85c", None))
        self.Page04_CaptureLabel.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page04_CaptureSetButton.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page04_CaptureReleaseButton.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Menu_LivepushButton.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.Menu_CapturepushButton.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.Menu_RecordpushButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.Menu_ClipPlaypushButton.setText(QCoreApplication.translate("MainWindow", u"Clip Play", None))
        self.MenubarLabel.setText("")
    # retranslateUi

## Cam Thread (BEGIN) - Live(Page01, Page02), Recording, Capture
semaphore = threading.Semaphore(5) #Live: 4, ClipPlay: 1
g_isRecordStatus = [False, False, False, False]

g_isStopClicked = [False, False, False, False]
g_isPlayClicked = [False, False, False, False]
g_isDrawRectangleStatus = [False, False, False, False]
g_isDrawingEnded = [False, False, False, False]
g_startX, g_startY, g_endX, g_endY = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
g_capImage = []

class camThread(threading.Thread):
    def __init__(self, camID, width, height, captureImage, liveW, liveH, liveLabel, captureLabel, videoDir, maxStorageSpinBox):
        super().__init__()
        self.width = width
        self.height = height
        self.captureImage = captureImage
        self.liveW = liveW
        self.liveH = liveH
        self.liveLabel = liveLabel
        self.captureLabel = captureLabel
        self.camID = camID # Zero base

        self.strVideoFileDir = videoDir
        self.maxRecordStorageSpinBox = maxStorageSpinBox
        self.tempVideoFileForMERGE = "tempMergeVideo.mp4"  # temp for Merge original
        self.isOversizeStatus = False
        self.isCreateFile = False
        self.isCreateOversizeFile = False

        self.isStopFrameCaptured = False
        self.stopFrame = np.zeros((self.width, self.height, 3), np.uint8)
        self.originalStopFrame = np.zeros((self.width, self.height, 3), np.uint8)

    def run(self):
        semaphore.acquire()
        while True:
            self.displayVideoStream()
        semaphore.release()

    def displayVideoStream(self):
        success, frame = self.captureImage.read()
        global g_capImage

        if success:
            frame = cv2.flip(frame, 1)
            self.frameRecording(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            liveImage = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            liveImage1 = liveImage.copy().scaled(self.liveW, self.liveH)

            frame = self.captureFrame(frame)
            frame, x, y, width, height = self.drawRectangleRegion(frame)
            capImage = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            captureImage1 = capImage.scaled(self.width, self.height)
            try:
                g_capImage[self.camID] = capImage.copy(x, y, width, height)
            except IndexError:
                g_capImage.insert(self.camID, capImage.copy(x, y, width, height))
        else:
            noVideoImage = QImage(860, 480, QImage.Format_RGB888)
            noVideoImage.fill(qRgb(50, 50, 50))
            liveImage1 = noVideoImage.copy()
            captureImage1 = noVideoImage.copy()

        self.liveLabel.setPixmap(QPixmap.fromImage(liveImage1))
        self.captureLabel.setPixmap(QPixmap.fromImage(captureImage1))

    ## Record in Thread(START)
    def frameRecording(self, frame):
        global g_isRecordStatus
        strVideoFile = "CAM{}_Video.mp4".format(self.camID + 1)  # original video
        if len(self.strVideoFileDir.text()) > 0: strVideoFile = self.strVideoFileDir.text() + "/" + strVideoFile

        if g_isRecordStatus[self.camID]:
            frame = cv2.resize(frame, (self.width, self.height))

            ### Create Video File from Frame (START) - (NOTE: 'Codec: mp4v, 확장자:mp4'를 사용해야 VideoWriter 및 VideoFileClip 클래스가 정상적으로 동작함.)
            if not self.isOversizeStatus:
                if not self.isCreateFile:
                    self.videoWriterOriginal = cv2.VideoWriter(strVideoFile, cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (self.width, self.height))
                    self.isCreateFile = True
                self.videoWriterOriginal.write(frame)
                fileSize = os.path.getsize(strVideoFile)
            else:
                if not self.isCreateOversizeFile:
                    self.videoWriterMergeFile = cv2.VideoWriter(self.tempVideoFileForMERGE, cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (self.width, self.height))
                    self.isCreateOversizeFile = True
                self.videoWriterMergeFile.write(frame)
                fileSize = os.path.getsize(strVideoFile) + os.path.getsize(self.tempVideoFileForMERGE)
            ### Create Video File from Frame (ENDED)

            if self.maxRecordStorageSpinBox.value() * 1024 * 1024 < fileSize:  # 1MB = 1048576
                if not self.isOversizeStatus:
                    self.videoWriterOriginal.release()  # Orignal Video File을 release해주어 앞부분 cut할 수 있도록 해줌.
                else:
                    self.videoWriterMergeFile.release()
                    self.mergeVideoFile(strVideoFile, self.tempVideoFileForMERGE, strVideoFile)
                    self.isCreateOversizeFile = False

                self.cutVideoFile(10, strVideoFile)     # cut Video prev 10sec.
                self.isOversizeStatus = True
        else:
            if not self.isOversizeStatus:
                if self.isCreateFile:
                    self.videoWriterOriginal.release()
                    self.isCreateFile = False
            else:
                if self.isCreateOversizeFile:
                    self.videoWriterMergeFile.release()
                    self.mergeVideoFile(strVideoFile, self.tempVideoFileForMERGE, strVideoFile)
                    self.isCreateOversizeFile = False

    def cutVideoFile(self, second, fileName):
        tempVideoFileforCUT = 'tempCutVideo.mp4'        # temp for cut original
        with VideoFileClip(fileName) as video:
            new = video.subclip(second, video.duration) # cut prev 'second'
            new.write_videofile(tempVideoFileforCUT, audio_codec='aac')  # 앞의 영상을 자르는 동작을 정상적으로 해주기 위해 audio_codec에 대해 설정해 줌.
        os.remove(fileName)
        os.rename(tempVideoFileforCUT, fileName)        # tempVideoFileforCUT을 Orignal Video File Name으로 변경해주어 저장.

    def mergeVideoFile(self, clip1, clip2, finalName):
        tempMergedFileName = "tempMergedFile.mp4"
        mergeClip1 = VideoFileClip(clip1)
        mergeClip2 = VideoFileClip(clip2)
        mergeResultClip = concatenate_videoclips([mergeClip1, mergeClip2])
        mergeResultClip.write_videofile(tempMergedFileName)
        os.remove(clip1)
        os.remove(clip2)
        os.rename(tempMergedFileName, finalName)
        print("merge success!!!!!!!!!!")
    ## Record in Thread(ENDED)

    ## Capture in Thread(BEGIN)
    def captureFrame(self, frame):
        global g_isStopClicked, g_isPlayClicked

        if g_isStopClicked[self.camID] and not self.isStopFrameCaptured:
            self.isStopFrameCaptured = True
            g_isPlayClicked[self.camID] = False
            self.stopFrame = frame
            self.originalStopFrame = frame.copy()

        if g_isPlayClicked[self.camID]:
            self.isStopFrameCaptured = False
            g_isStopClicked[self.camID] = False

        if self.isStopFrameCaptured:
            global g_isDrawRectangleStatus, g_isDrawingEnded
            if not g_isDrawRectangleStatus[self.camID] or not g_isDrawingEnded[self.camID]:
                self.stopFrame = self.originalStopFrame.copy()
            return self.stopFrame
        else:
            return frame

    def drawRectangleRegion(self, frame):
        global g_isDrawRectangleStatus, g_isDrawingEnded
        global g_startX, g_startY, g_endX, g_endY

        if g_isDrawRectangleStatus[self.camID] and g_isDrawingEnded[self.camID]:
            frameHeight, frameWidth = frame.shape[:2]

            ratioX = frameWidth / self.width
            ratioY = frameHeight / self.height
            drawMargin = 2  # 이미지캡쳐에서 rectangle이 포함되지 않도록 drawMargin 추가

            stPosX, stPosY, endPosX, endPosY = int(g_startX[self.camID] * ratioX), int(g_startY[self.camID] * ratioY), int(g_endX[self.camID] * ratioX), int(g_endY[self.camID] * ratioY)

            frame = cv2.rectangle(frame, (stPosX - drawMargin, stPosY - drawMargin), (endPosX + drawMargin, endPosY + drawMargin), (0, 0, 255), 2)
            return frame, stPosX, stPosY, endPosX - stPosX, endPosY - stPosY
        else:
            return frame, 0, 0, frame.shape[1], frame.shape[0]
    ## Capture in Thread(ENDED)
## Cam Thread (ENDED)

## ClipPlay Thread(BEGIN)
g_isPlayVideo = False
g_clipPlayFrameNum = 0
g_needResetClipPlay = True

class clipPlayThread(threading.Thread):
    def __init__(self, clipPlayWidth, clipPlayHeight, clipPlayFilePath, clipImageLabel, clipPlaySlider):
        super().__init__()
        self.clipPlayWidth = clipPlayWidth
        self.clipPlayHeight = clipPlayHeight
        self.clipPlayFilePath = clipPlayFilePath
        self.clipImageLabel = clipImageLabel
        self.clipPlaySlider = clipPlaySlider

        self.prevClipPlayFilePath = ""
        self.curClipPlayFilePath = ""

        self.prev_time = 0
        self.fps = 30
        self.frame_len = 0

    def run(self):
        semaphore.acquire()
        while True:
            self.showClipPlay()
        semaphore.release()

    def showClipPlay(self):
        global g_isPlayVideo, g_clipPlayFrameNum, g_needResetClipPlay
        while True:
            if g_isPlayVideo:
                self.curClipPlayFilePath = self.clipPlayFilePath.text()
                if self.prevClipPlayFilePath != self.curClipPlayFilePath: # Change path
                    self.prevClipPlayFilePath = self.curClipPlayFilePath
                    g_clipPlayFrameNum = 0
                    g_needResetClipPlay = True
                    print("Change path!!")

                if g_needResetClipPlay:
                    cap = cv2.VideoCapture(self.curClipPlayFilePath)
                    self.fps = cap.get(cv2.CAP_PROP_FPS)
                    self.frame_len = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                    cap.set(cv2.CAP_PROP_POS_FRAMES, g_clipPlayFrameNum)
                    g_needResetClipPlay = False
                    print("Frame reset frameNum:{}({})".format(g_clipPlayFrameNum, self.frame_len))

                current_time = time.time() - self.prev_time
                if current_time > 1./self.fps:                          # 영상의 FPS에 알맞게 영상을 재생하도록 함.
                    self.prev_time = time.time()
                    success, clipFrame = cap.read()                     # 받는 매개변수: 성공여부, image 저장장소; read시마다 frame이 1씩 증가되어 받음.
                    g_clipPlayFrameNum = cap.get(cv2.CAP_PROP_POS_FRAMES) # Pause시 해당 framenumber 저장됨
                    if g_clipPlayFrameNum == self.frame_len:              # Video 끝에 오는 경우 cv2 error 방지를 위한 방어 코드
                        g_isPlayVideo = False
                        g_clipPlayFrameNum = 0
                        print("END of Video")
                    print("frameNumber: {}({})".format(g_clipPlayFrameNum, self.frame_len))

                    clipFrame = cv2.cvtColor(clipFrame, cv2.COLOR_RGB2BGR)
                    clipImage = QImage(clipFrame, clipFrame.shape[1], clipFrame.shape[0], clipFrame.strides[0], QImage.Format_RGB888)
                    clipImage1 = clipImage.copy().scaled(self.clipPlayWidth, self.clipPlayHeight)
                    self.clipImageLabel.setPixmap(QPixmap.fromImage(clipImage1))
                    self.clipPlaySlider.setValue(g_clipPlayFrameNum)
            else:   # not g_isPlayVideo (Pause, no ClipFile ...)
                g_needResetClipPlay = True
## ClipPlay Thread(ENDED)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.capture = []
        self.listThread = []

        self.cameraWindowWidth, self.cameraWindowHeight = 0, 0

        self.setupUi(self)
        self.setupCamra()
        self.setupRecord()
        self.setupCapture()
        self.setupClipPlay()
        self.setupMenuBar()

## ClipPlay(BEGIN)
    def setupClipPlay(self):
        self.clipSliderPressed = False

        self.Page04_ClipPlayDirbutton.clicked.connect(lambda: self.setFilePath(1))
        self.Page04_ClipPlayButtonPlay.clicked.connect(lambda: self.setPlayVideoStatus(True))
        self.Page04_ClipPlayButtonPause.clicked.connect(lambda: self.setPlayVideoStatus(False))

        self.Page04_ClipPlaySlider.sliderPressed.connect(lambda: self.setPlayVideoStatus(False))
        self.Page04_ClipPlaySlider.valueChanged.connect(self.showClipToImageLabel)

        self.Page04_ClipPlayButtonBack.clicked.connect(lambda: self.setMoveVideoFrame(-1))
        self.Page04_ClipPlayButtonForward.clicked.connect(lambda: self.setMoveVideoFrame(1))

        clipPlayWidth = self.horizontalLayoutWidget_7.width()
        clipPlayHeight = self.horizontalLayoutWidget_7.height()
        clipPlayFilePath = self.Page04_ClipPlayDirlineEdit
        clipImageLabel = self.Page04_ImageLabel
        clipPlaySlider = self.Page04_ClipPlaySlider

        self.listThread.append(clipPlayThread(clipPlayWidth, clipPlayHeight, clipPlayFilePath, clipImageLabel, clipPlaySlider))
        self.listThread[-1].start()

    def setMoveVideoFrame(self, value):
        self.Page04_ClipPlaySlider.setValue(g_clipPlayFrameNum + value)
        self.setPlayVideoStatus(False)
        self.showClipToImageLabel()

    def showClipToImageLabel(self):
        global g_clipPlayFrameNum, g_isPlayVideo, g_needResetClipPlay
        g_clipPlayFrameNum = self.Page04_ClipPlaySlider.value()
        self.Page04_ClipPlayFrameNumLabel.setText(str(int(g_clipPlayFrameNum)))
        print("Slider Value: ", g_clipPlayFrameNum)

        if self.clipSliderPressed:
            g_isPlayVideo = False
            g_needResetClipPlay = True

            cap = cv2.VideoCapture(self.Page04_ClipPlayDirlineEdit.text())
            cap.set(cv2.CAP_PROP_POS_FRAMES, g_clipPlayFrameNum)
            success, clipFrame = cap.read()

            clipFrame = cv2.cvtColor(clipFrame, cv2.COLOR_RGB2BGR)
            clipImage = QImage(clipFrame, clipFrame.shape[1], clipFrame.shape[0], clipFrame.strides[0], QImage.Format_RGB888)
            clipImage1 = clipImage.copy().scaled(self.horizontalLayoutWidget_7.width(), self.horizontalLayoutWidget_7.height())
            self.Page04_ImageLabel.setPixmap(QPixmap.fromImage(clipImage1))

    def setFilePath(self, id):
        global g_clipPlayFrameNum
        pathName = QFileDialog.getOpenFileName(self, 'Open file', './')
        if id == 1:     #이미지 경로 설정 및 Load시 첫번째 frame show
            """lineEdit 보여주기"""
            self.Page04_ClipPlayDirlineEdit.setText(pathName[0])

            """ImageLabel 보여주기"""
            cap = cv2.VideoCapture(self.Page04_ClipPlayDirlineEdit.text())
            success, clipFrame = cap.read()
            clipFrame = cv2.cvtColor(clipFrame, cv2.COLOR_RGB2BGR)
            clipImage = QImage(clipFrame, clipFrame.shape[1], clipFrame.shape[0], clipFrame.strides[0], QImage.Format_RGB888)
            clipImage1 = clipImage.copy().scaled(self.horizontalLayoutWidget_7.width(), self.horizontalLayoutWidget_7.height())
            self.Page04_ImageLabel.setPixmap(QPixmap.fromImage(clipImage1))

            """Slider Frame Count로 Max값 설정하기"""
            frame_len = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.Page04_ClipPlaySlider.setRange(0, frame_len - 1)
            self.Page04_ClipPlaySlider.setValue(0)
            g_clipPlayFrameNum = 0
            self.Page04_ClipPlayFrameMaxLabel.setText("/{}".format(str(int(frame_len - 1))))
            print("min: ", self.Page04_ClipPlaySlider.minimum(), "max: ", self.Page04_ClipPlaySlider.maximum())

    def setPlayVideoStatus(self, isBoolState):
        global g_isPlayVideo
        g_isPlayVideo = isBoolState
        self.clipSliderPressed = not isBoolState
        print("setPlayVideoStatus: ", g_isPlayVideo)
## ClipPlay(ENDED)

## MenuBar(BEGIN)
    def setupMenuBar(self):
        self.capturePageOn = False
        self.Menu_LivepushButton.clicked.connect(lambda: self.changeStackWidget(0))
        self.Menu_CapturepushButton.clicked.connect(lambda: self.changeStackWidget(1))
        self.Menu_RecordpushButton.clicked.connect(lambda: self.changeStackWidget(2))
        self.Menu_ClipPlaypushButton.clicked.connect(lambda: self.changeStackWidget(3))

    def changeStackWidget(self, id):
        PageIdList = [self.Page01, self.Page02, self.Page03, self.Page04]

        self.stackedWidget.setCurrentWidget(PageIdList[id])
        self.capturePageOn = (id == 1)
## MenuBar(ENDED)

## WebCam Image(BEGIN)
    def CameraWindowSize(self, ch=0):
        width, height = 0, 0
        if ch == 0:
            width = self.horizontalLayoutWidget.width()
            height = self.horizontalLayoutWidget.height()
        return width, height

    def setupCamra(self):
        """Initialize camera.
        """
        self.cameraWindowWidth, self.cameraWindowHeight = self.CameraWindowSize(0)

        Page01_LiveImagelabelList       = [self.Page01_LiveImagelabel1, self.Page01_LiveImagelabel2, self.Page01_LiveImagelabel3, self.Page01_LiveImagelabel4]
        Page02_ImageLabelList           = [self.Page02_ImageLabel1, self.Page02_ImageLabel2, self.Page02_ImageLabel3, self.Page02_ImageLabel4]
        Page03_setVideoDirlineEditList  = [self.Page03_setVideoDirlineEdit1, self.Page03_setVideoDirlineEdit2, self.Page03_setVideoDirlineEdit3, self.Page03_setVideoDirlineEdit4]
        Page03_RecordCapSpinBoxList     = [self.Page03_RecordCapSpinBox1, self.Page03_RecordCapSpinBox2, self.Page03_RecordCapSpinBox3, self.Page03_RecordCapSpinBox4]

        liveWidth, liveHeight = self.horizontalLayoutWidget_5.geometry().width(), self.horizontalLayoutWidget_5.geometry().height()

        for capIndex in range(0, 2):  ### tempRange!!
            self.capture.insert(capIndex, cv2.VideoCapture(capIndex))          # cv2.VideoCapture(capIndex) temp ==> change for settingValue
            self.capture[capIndex].set(cv2.CAP_PROP_FRAME_WIDTH, self.cameraWindowWidth)
            self.capture[capIndex].set(cv2.CAP_PROP_FRAME_HEIGHT, self.cameraWindowHeight)

            self.listThread.append(camThread(capIndex, self.cameraWindowWidth, self.cameraWindowHeight, self.capture[capIndex], liveWidth, liveHeight,
                                             Page01_LiveImagelabelList[capIndex], Page02_ImageLabelList[capIndex],
                                             Page03_setVideoDirlineEditList[capIndex], Page03_RecordCapSpinBoxList[capIndex]))
            self.listThread[-1].start()
## WebCam Image(ENDED)

## Record(START)
    def setupRecord(self):
        self.Page03_setVideoDirbutton1.clicked.connect(lambda: self.setDirectory(0))
        self.Page03_setVideoDirbutton2.clicked.connect(lambda: self.setDirectory(1))
        self.Page03_setVideoDirbutton3.clicked.connect(lambda: self.setDirectory(2))
        self.Page03_setVideoDirbutton4.clicked.connect(lambda: self.setDirectory(3))

        self.Page03_RecordStartButton1.clicked.connect(lambda: self.recordStatus(True, 0))
        self.Page03_RecordEndButton1.clicked.connect(lambda: self.recordStatus(False, 0))
        self.Page03_RecordStartButton2.clicked.connect(lambda: self.recordStatus(True, 1))
        self.Page03_RecordEndButton2.clicked.connect(lambda: self.recordStatus(False, 1))
        self.Page03_RecordStartButton3.clicked.connect(lambda: self.recordStatus(True, 2))
        self.Page03_RecordEndButton3.clicked.connect(lambda: self.recordStatus(False, 2))
        self.Page03_RecordStartButton4.clicked.connect(lambda: self.recordStatus(True, 3))
        self.Page03_RecordEndButton4.clicked.connect(lambda: self.recordStatus(False, 3))

    def recordStatus(self, isBoolState, index):
        global g_isRecordStatus
        Page03_RecordStatuslabelList = [self.Page03_RecordStatuslabel1, self.Page03_RecordStatuslabel2, self.Page03_RecordStatuslabel3, self.Page03_RecordStatuslabel4]
        Page03_RecordCapSpinBoxList = [self.Page03_RecordCapSpinBox1, self.Page03_RecordCapSpinBox2, self.Page03_RecordCapSpinBox3, self.Page03_RecordCapSpinBox4]

        g_isRecordStatus[index] = isBoolState
        strRecordStatus = "(녹화중)" if isBoolState else "(녹화해제)"
        Page03_RecordStatuslabelList[index].setText(strRecordStatus)
        Page03_RecordCapSpinBoxList[index].setDisabled(isBoolState)
## Record(ENDED)

## Capture(BEGIN)
    def setupCapture(self):
        self.isStPosOnImage = False
        self.capImgStartX, self.capImgStartY, self.capImgEndX, self.capImgEndY = 212, 30, 962, 450  ### Note: Image Mouse Postion

        self.Page02_setOKImagelineEditList = [self.Page02_setOKImagelineEdit1, self.Page02_setOKImagelineEdit2,
                                              self.Page02_setOKImagelineEdit3, self.Page02_setOKImagelineEdit4]
        self.Page02_setNGImagelineEditList = [self.Page02_setNGImagelineEdit1, self.Page02_setNGImagelineEdit2,
                                              self.Page02_setNGImagelineEdit3, self.Page02_setNGImagelineEdit4]
        self.Page02_setAImagelineEditList = [self.Page02_setAImagelineEdit1, self.Page02_setAImagelineEdit2,
                                             self.Page02_setAImagelineEdit3, self.Page02_setAImagelineEdit4]
        self.Page02_setBImagelineEditList = [self.Page02_setBImagelineEdit1, self.Page02_setBImagelineEdit2,
                                             self.Page02_setBImagelineEdit3, self.Page02_setBImagelineEdit4]
        self.Page02_setCImagelineEditList = [self.Page02_setCImagelineEdit1, self.Page02_setCImagelineEdit2,
                                             self.Page02_setCImagelineEdit3, self.Page02_setCImagelineEdit4]

        self.Page02_OKImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(0, 0))
        self.Page02_NGImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(1, 0))
        self.Page02_AImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(2, 0))
        self.Page02_BImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(3, 0))
        self.Page02_CImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(4, 0))

        self.Page02_OKImageSaveButton2.clicked.connect(lambda: self.saveCaptureImage(0, 1))
        self.Page02_NGImageSaveButton2.clicked.connect(lambda: self.saveCaptureImage(1, 1))
        self.Page02_AImageSaveButton2.clicked.connect(lambda: self.saveCaptureImage(2, 1))
        self.Page02_BImageSaveButton2.clicked.connect(lambda: self.saveCaptureImage(3, 1))
        self.Page02_CImageSaveButton2.clicked.connect(lambda: self.saveCaptureImage(4, 1))

        self.Page02_OKImageSaveButton3.clicked.connect(lambda: self.saveCaptureImage(0, 2))
        self.Page02_NGImageSaveButton3.clicked.connect(lambda: self.saveCaptureImage(1, 2))
        self.Page02_AImageSaveButton3.clicked.connect(lambda: self.saveCaptureImage(2, 2))
        self.Page02_BImageSaveButton3.clicked.connect(lambda: self.saveCaptureImage(3, 2))
        self.Page02_CImageSaveButton3.clicked.connect(lambda: self.saveCaptureImage(4, 2))

        self.Page02_OKImageSaveButton4.clicked.connect(lambda: self.saveCaptureImage(0, 3))
        self.Page02_NGImageSaveButton4.clicked.connect(lambda: self.saveCaptureImage(1, 3))
        self.Page02_AImageSaveButton4.clicked.connect(lambda: self.saveCaptureImage(2, 3))
        self.Page02_BImageSaveButton4.clicked.connect(lambda: self.saveCaptureImage(3, 3))
        self.Page02_CImageSaveButton4.clicked.connect(lambda: self.saveCaptureImage(4, 3))

        self.Page02_setOKImagebutton1.clicked.connect(lambda: self.setDirectory(100, 0))
        self.Page02_setNGImagebutton1.clicked.connect(lambda: self.setDirectory(101, 0))
        self.Page02_setAImagebutton1.clicked.connect(lambda: self.setDirectory(102, 0))
        self.Page02_setBImagebutton1.clicked.connect(lambda: self.setDirectory(103, 0))
        self.Page02_setCImagebutton1.clicked.connect(lambda: self.setDirectory(104, 0))

        self.Page02_setOKImagebutton2.clicked.connect(lambda: self.setDirectory(100, 1))
        self.Page02_setNGImagebutton2.clicked.connect(lambda: self.setDirectory(101, 1))
        self.Page02_setAImagebutton2.clicked.connect(lambda: self.setDirectory(102, 1))
        self.Page02_setBImagebutton2.clicked.connect(lambda: self.setDirectory(103, 1))
        self.Page02_setCImagebutton2.clicked.connect(lambda: self.setDirectory(104, 1))

        self.Page02_setOKImagebutton3.clicked.connect(lambda: self.setDirectory(100, 2))
        self.Page02_setNGImagebutton3.clicked.connect(lambda: self.setDirectory(101, 2))
        self.Page02_setAImagebutton3.clicked.connect(lambda: self.setDirectory(102, 2))
        self.Page02_setBImagebutton3.clicked.connect(lambda: self.setDirectory(103, 2))
        self.Page02_setCImagebutton3.clicked.connect(lambda: self.setDirectory(104, 2))

        self.Page02_setOKImagebutton4.clicked.connect(lambda: self.setDirectory(100, 3))
        self.Page02_setNGImagebutton4.clicked.connect(lambda: self.setDirectory(101, 3))
        self.Page02_setAImagebutton4.clicked.connect(lambda: self.setDirectory(102, 3))
        self.Page02_setBImagebutton4.clicked.connect(lambda: self.setDirectory(103, 3))
        self.Page02_setCImagebutton4.clicked.connect(lambda: self.setDirectory(104, 3))

        self.Page02_VideoStopButton1.clicked.connect(lambda: self.captureFrameStop(0))
        self.Page02_VideoPlayButton1.clicked.connect(lambda: self.captureFramePlay(0))
        self.Page02_CaptureSetButton1.clicked.connect(lambda: self.drawRectangleStatus(True, 0))
        self.Page02_CaptureReleaseButton1.clicked.connect(lambda: self.drawRectangleStatus(False, 0))

        self.Page02_VideoStopButton2.clicked.connect(lambda: self.captureFrameStop(1))
        self.Page02_VideoPlayButton2.clicked.connect(lambda: self.captureFramePlay(1))
        self.Page02_CaptureSetButton2.clicked.connect(lambda: self.drawRectangleStatus(True, 1))
        self.Page02_CaptureReleaseButton2.clicked.connect(lambda: self.drawRectangleStatus(False, 1))

        self.Page02_VideoStopButton3.clicked.connect(lambda: self.captureFrameStop(2))
        self.Page02_VideoPlayButton3.clicked.connect(lambda: self.captureFramePlay(2))
        self.Page02_CaptureSetButton3.clicked.connect(lambda: self.drawRectangleStatus(True, 2))
        self.Page02_CaptureReleaseButton3.clicked.connect(lambda: self.drawRectangleStatus(False, 2))

        self.Page02_VideoStopButton4.clicked.connect(lambda: self.captureFrameStop(3))
        self.Page02_VideoPlayButton4.clicked.connect(lambda: self.captureFramePlay(3))
        self.Page02_CaptureSetButton4.clicked.connect(lambda: self.drawRectangleStatus(True, 3))
        self.Page02_CaptureReleaseButton4.clicked.connect(lambda: self.drawRectangleStatus(False, 3))



    def captureFrameStop(self, camID):
        global g_isStopClicked, g_isPlayClicked

        g_isStopClicked[camID] = True
        g_isPlayClicked[camID] = False

    def captureFramePlay(self, camID):
        global g_isStopClicked, g_isPlayClicked

        g_isPlayClicked[camID] = True
        g_isStopClicked[camID] = False

    def setDirectory(self, id, camID=0):
        """ setDirectory ID
        VIDEO ID   - 0: CAM1 Video, 1: CAM2 Video, 2: CAM3 Video, 3: CAM4 Video
        CAPTURE ID - 100: OK Image, 101: NG Image, 102: A Image, 103: B Image, 104: C Image
        """
        dirName = QFileDialog.getExistingDirectory(self, self.tr("저장 경로 설정"), "./", QFileDialog.ShowDirsOnly)

        if id == 0:    # 0 Video1
            self.Page03_setVideoDirlineEdit1.setText(dirName)
        elif id == 1:  # 1 Video2
            self.Page03_setVideoDirlineEdit2.setText(dirName)
        elif id == 2:  # 2 Video3
            self.Page03_setVideoDirlineEdit3.setText(dirName)
        elif id == 3:  # 3 Video4
            self.Page03_setVideoDirlineEdit4.setText(dirName)
        elif id == 100:
            self.Page02_setOKImagelineEditList[camID].setText(dirName)
        elif id == 101:
            self.Page02_setNGImagelineEditList[camID].setText(dirName)
        elif id == 102:
            self.Page02_setAImagelineEditList[camID].setText(dirName)
        elif id == 103:
            self.Page02_setBImagelineEditList[camID].setText(dirName)
        elif id == 104:
            self.Page02_setCImagelineEditList[camID].setText(dirName)

    def mousePressEvent(self, QMouseEvent):
        global g_isDrawingEnded
        global g_startX, g_startY

        tabIndex = self.CameratabWidget.currentIndex()

        if self.capturePageOn and self.capImgStartX < QMouseEvent.x() <= self.capImgEndX and self.capImgStartY < QMouseEvent.y() <= self.capImgEndY:
            self.isStPosOnImage = True
        else:
            self.isStPosOnImage = False
            return

        g_isDrawingEnded[tabIndex] = False
        g_startX[tabIndex], g_startY[tabIndex] = QMouseEvent.x(), QMouseEvent.y()

    def mouseReleaseEvent(self, QMouseEvent):
        global g_isDrawRectangleStatus, g_isDrawingEnded
        global g_startX, g_startY, g_endX, g_endY
        tabIndex = self.CameratabWidget.currentIndex()

        if not self.isStPosOnImage or not g_isDrawRectangleStatus[tabIndex]:
            return

        g_isDrawingEnded[tabIndex] = True
        g_endX[tabIndex], g_endY[tabIndex] = QMouseEvent.x(), QMouseEvent.y()

        if g_endX[tabIndex] < g_startX[tabIndex]:
            g_startX[tabIndex], g_endX[tabIndex] = g_endX[tabIndex], g_startX[tabIndex]
        if g_endY[tabIndex] < g_startY[tabIndex]:
            g_startY[tabIndex], g_endY[tabIndex] = g_endY[tabIndex], g_startY[tabIndex]

        if g_startX[tabIndex] < self.capImgStartX : g_startX[tabIndex] = self.capImgStartX
        if g_startY[tabIndex] < self.capImgStartY : g_startY[tabIndex] = self.capImgStartY
        if g_endX[tabIndex] >= self.capImgEndX    : g_endX[tabIndex] = self.capImgEndX
        if g_endY[tabIndex] >= self.capImgEndY    : g_endY[tabIndex] = self.capImgEndY

        g_startX[tabIndex] -= self.capImgStartX
        g_startY[tabIndex] -= self.capImgStartY
        g_endX[tabIndex] -= self.capImgStartX
        g_endY[tabIndex] -= self.capImgStartY

    def drawRectangleStatus(self, isBoolState, camID):
        global g_isDrawRectangleStatus
        global g_startX, g_startY, g_endX, g_endY
        tabIndex = self.CameratabWidget.currentIndex()

        g_isDrawRectangleStatus[camID] = isBoolState
        if g_isDrawRectangleStatus[camID]:
            g_startX[tabIndex], g_startY[tabIndex], g_endX[tabIndex], g_endY[tabIndex] = 0, 0, self.cameraWindowWidth, self.cameraWindowHeight

    def saveCaptureImage(self, id, camID): # id - 0:OK, 1: NG, 2: A, 3: B, 4: C
        global g_capImage

        imageNumber = 1
        tempCurPwd = os.getcwd()
        if id == 0 and (len(self.Page02_setOKImagelineEditList[camID].text()) > 0):
            os.chdir(self.Page02_setOKImagelineEditList[camID].text()) # Move TO Save PWD
        elif id == 1 and (len(self.Page02_setNGImagelineEditList[camID].text()) > 0):
            os.chdir(self.Page02_setNGImagelineEditList[camID].text()) # Move TO Save PWD
        elif id == 2 and (len(self.Page02_setAImagelineEditList[camID].text()) > 0):
            os.chdir(self.Page02_setAImagelineEditList[camID].text())
        elif id == 3 and (len(self.Page02_setBImagelineEditList[camID].text()) > 0):
            os.chdir(self.Page02_setBImagelineEditList[camID].text())
        elif id == 4 and (len(self.Page02_setCImagelineEditList[camID].text()) > 0):
            os.chdir(self.Page02_setCImagelineEditList[camID].text())

        while True:
            if cv2.imread("image.jpg") is None:
                g_capImage[camID].save("image.jpg")
                break

            fileName = "image(" + str(imageNumber) + ").jpg"
            if cv2.imread(fileName) is None:
                g_capImage[camID].save(fileName)
                break
            else:
                imageNumber = imageNumber + 1
        os.chdir(tempCurPwd)
## Capture(ENDED)

def main():
    app = QApplication(sys.argv)
    main_view = MainWindow()
    main_view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()