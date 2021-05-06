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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 9, 791, 521))
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
        self.Page01_LiveImagelabel = QLabel(self.horizontalLayoutWidget_5)
        self.Page01_LiveImagelabel.setObjectName(u"Page01_LiveImagelabel")

        self.Page01_CameraImage1.addWidget(self.Page01_LiveImagelabel)

        self.horizontalLayoutWidget_6 = QWidget(self.Page01)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 280, 391, 241))
        self.Page01_CameraImage3 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.Page01_CameraImage3.setObjectName(u"Page01_CameraImage3")
        self.Page01_CameraImage3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_10 = QWidget(self.Page01)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(400, 20, 391, 241))
        self.Page01_CameraImage2 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.Page01_CameraImage2.setObjectName(u"Page01_CameraImage2")
        self.Page01_CameraImage2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_11 = QWidget(self.Page01)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(400, 280, 391, 241))
        self.Page01_CameraImage4 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.Page01_CameraImage4.setObjectName(u"Page01_CameraImage4")
        self.Page01_CameraImage4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.Page01)
        self.Page02 = QWidget()
        self.Page02.setObjectName(u"Page02")
        self.CameratabWidget = QTabWidget(self.Page02)
        self.CameratabWidget.setObjectName(u"CameratabWidget")
        self.CameratabWidget.setGeometry(QRect(0, 0, 791, 521))
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

        self.horizontalLayoutWidget_8 = QWidget(self.tab)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(0, 460, 411, 31))
        self.Page02_setNGImageLayout1 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.Page02_setNGImageLayout1.setObjectName(u"Page02_setNGImageLayout1")
        self.Page02_setNGImageLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page02_setNGImageLabel1 = QLabel(self.horizontalLayoutWidget_8)
        self.Page02_setNGImageLabel1.setObjectName(u"Page02_setNGImageLabel1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_setNGImageLabel1)

        self.Page02_setNGImagelineEdit1 = QLineEdit(self.horizontalLayoutWidget_8)
        self.Page02_setNGImagelineEdit1.setObjectName(u"Page02_setNGImagelineEdit1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_setNGImagelineEdit1)

        self.Page02_setNGImagebutton1 = QPushButton(self.horizontalLayoutWidget_8)
        self.Page02_setNGImagebutton1.setObjectName(u"Page02_setNGImagebutton1")

        self.Page02_setNGImageLayout1.addWidget(self.Page02_setNGImagebutton1)

        self.horizontalLayoutWidget_3 = QWidget(self.tab)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(430, 440, 350, 31))
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

        self.Page02_OKImageSaveButton1 = QPushButton(self.horizontalLayoutWidget_3)
        self.Page02_OKImageSaveButton1.setObjectName(u"Page02_OKImageSaveButton1")

        self.Page02_CaptureLayout1.addWidget(self.Page02_OKImageSaveButton1)

        self.Page02_NGImageSaveButton1 = QPushButton(self.horizontalLayoutWidget_3)
        self.Page02_NGImageSaveButton1.setObjectName(u"Page02_NGImageSaveButton1")

        self.Page02_CaptureLayout1.addWidget(self.Page02_NGImageSaveButton1)

        self.horizontalLayoutWidget_7 = QWidget(self.tab)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 430, 411, 31))
        self.Page02_setOKImageLayout1 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.Page02_setOKImageLayout1.setObjectName(u"Page02_setOKImageLayout1")
        self.Page02_setOKImageLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page02_setOKImageLabel1 = QLabel(self.horizontalLayoutWidget_7)
        self.Page02_setOKImageLabel1.setObjectName(u"Page02_setOKImageLabel1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_setOKImageLabel1)

        self.Page02_setOKImagelineEdit1 = QLineEdit(self.horizontalLayoutWidget_7)
        self.Page02_setOKImagelineEdit1.setObjectName(u"Page02_setOKImagelineEdit1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_setOKImagelineEdit1)

        self.Page02_setOKImagebutton1 = QPushButton(self.horizontalLayoutWidget_7)
        self.Page02_setOKImagebutton1.setObjectName(u"Page02_setOKImagebutton1")

        self.Page02_setOKImageLayout1.addWidget(self.Page02_setOKImagebutton1)

        self.CameratabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget_9 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(0, 430, 411, 31))
        self.Page02_setOKImageLayout2 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.Page02_setOKImageLayout2.setObjectName(u"Page02_setOKImageLayout2")
        self.Page02_setOKImageLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page02_setOKImageLabel2 = QLabel(self.horizontalLayoutWidget_9)
        self.Page02_setOKImageLabel2.setObjectName(u"Page02_setOKImageLabel2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_setOKImageLabel2)

        self.Page02_setOKImagelineEdit2 = QLineEdit(self.horizontalLayoutWidget_9)
        self.Page02_setOKImagelineEdit2.setObjectName(u"Page02_setOKImagelineEdit2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_setOKImagelineEdit2)

        self.Page02_setOKImagebutton2 = QPushButton(self.horizontalLayoutWidget_9)
        self.Page02_setOKImagebutton2.setObjectName(u"Page02_setOKImagebutton2")

        self.Page02_setOKImageLayout2.addWidget(self.Page02_setOKImagebutton2)

        self.horizontalLayoutWidget_2 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Page02_CameraImage2.setObjectName(u"Page02_CameraImage2")
        self.Page02_CameraImage2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_4 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(430, 440, 350, 31))
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

        self.Page02_OKImageSaveButton2 = QPushButton(self.horizontalLayoutWidget_4)
        self.Page02_OKImageSaveButton2.setObjectName(u"Page02_OKImageSaveButton2")

        self.Page02_CaptureLayout2.addWidget(self.Page02_OKImageSaveButton2)

        self.Page02_NGImageSaveButton2 = QPushButton(self.horizontalLayoutWidget_4)
        self.Page02_NGImageSaveButton2.setObjectName(u"Page02_NGImageSaveButton2")

        self.Page02_CaptureLayout2.addWidget(self.Page02_NGImageSaveButton2)

        self.horizontalLayoutWidget_12 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(0, 460, 411, 31))
        self.Page02_setNGImageLayout2 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.Page02_setNGImageLayout2.setObjectName(u"Page02_setNGImageLayout2")
        self.Page02_setNGImageLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page02_setNGImageLabel2 = QLabel(self.horizontalLayoutWidget_12)
        self.Page02_setNGImageLabel2.setObjectName(u"Page02_setNGImageLabel2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_setNGImageLabel2)

        self.Page02_setNGImagelineEdit2 = QLineEdit(self.horizontalLayoutWidget_12)
        self.Page02_setNGImagelineEdit2.setObjectName(u"Page02_setNGImagelineEdit2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_setNGImagelineEdit2)

        self.Page02_setNGImagebutton2 = QPushButton(self.horizontalLayoutWidget_12)
        self.Page02_setNGImagebutton2.setObjectName(u"Page02_setNGImagebutton2")

        self.Page02_setNGImageLayout2.addWidget(self.Page02_setNGImagebutton2)

        self.CameratabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayoutWidget_13 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(0, 460, 411, 31))
        self.Page02_setNGImageLayout3 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.Page02_setNGImageLayout3.setObjectName(u"Page02_setNGImageLayout3")
        self.Page02_setNGImageLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page02_setNGImageLabel3 = QLabel(self.horizontalLayoutWidget_13)
        self.Page02_setNGImageLabel3.setObjectName(u"Page02_setNGImageLabel3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_setNGImageLabel3)

        self.Page02_setNGImagelineEdit3 = QLineEdit(self.horizontalLayoutWidget_13)
        self.Page02_setNGImagelineEdit3.setObjectName(u"Page02_setNGImagelineEdit3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_setNGImagelineEdit3)

        self.Page02_setNGImagebutton3 = QPushButton(self.horizontalLayoutWidget_13)
        self.Page02_setNGImagebutton3.setObjectName(u"Page02_setNGImagebutton3")

        self.Page02_setNGImageLayout3.addWidget(self.Page02_setNGImagebutton3)

        self.horizontalLayoutWidget_14 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(0, 430, 411, 31))
        self.Page02_setOKImageLayout3 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.Page02_setOKImageLayout3.setObjectName(u"Page02_setOKImageLayout3")
        self.Page02_setOKImageLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page02_setOKImageLabel3 = QLabel(self.horizontalLayoutWidget_14)
        self.Page02_setOKImageLabel3.setObjectName(u"Page02_setOKImageLabel3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_setOKImageLabel3)

        self.Page02_setOKImagelineEdit3 = QLineEdit(self.horizontalLayoutWidget_14)
        self.Page02_setOKImagelineEdit3.setObjectName(u"Page02_setOKImagelineEdit3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_setOKImagelineEdit3)

        self.Page02_setOKImagebutton3 = QPushButton(self.horizontalLayoutWidget_14)
        self.Page02_setOKImagebutton3.setObjectName(u"Page02_setOKImagebutton3")

        self.Page02_setOKImageLayout3.addWidget(self.Page02_setOKImagebutton3)

        self.horizontalLayoutWidget_15 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(430, 440, 350, 31))
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

        self.Page02_OKImageSaveButton3 = QPushButton(self.horizontalLayoutWidget_15)
        self.Page02_OKImageSaveButton3.setObjectName(u"Page02_OKImageSaveButton3")

        self.Page02_CaptureLayout3.addWidget(self.Page02_OKImageSaveButton3)

        self.Page02_NGImageSaveButton3 = QPushButton(self.horizontalLayoutWidget_15)
        self.Page02_NGImageSaveButton3.setObjectName(u"Page02_NGImageSaveButton3")

        self.Page02_CaptureLayout3.addWidget(self.Page02_NGImageSaveButton3)

        self.horizontalLayoutWidget_16 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage3 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.Page02_CameraImage3.setObjectName(u"Page02_CameraImage3")
        self.Page02_CameraImage3.setContentsMargins(0, 0, 0, 0)
        self.CameratabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayoutWidget_17 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(0, 460, 411, 31))
        self.Page02_setNGImageLayout4 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.Page02_setNGImageLayout4.setObjectName(u"Page02_setNGImageLayout4")
        self.Page02_setNGImageLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page02_setNGImageLabel4 = QLabel(self.horizontalLayoutWidget_17)
        self.Page02_setNGImageLabel4.setObjectName(u"Page02_setNGImageLabel4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_setNGImageLabel4)

        self.Page02_setNGImagelineEdit4 = QLineEdit(self.horizontalLayoutWidget_17)
        self.Page02_setNGImagelineEdit4.setObjectName(u"Page02_setNGImagelineEdit4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_setNGImagelineEdit4)

        self.Page02_setNGImagebutton4 = QPushButton(self.horizontalLayoutWidget_17)
        self.Page02_setNGImagebutton4.setObjectName(u"Page02_setNGImagebutton4")

        self.Page02_setNGImageLayout4.addWidget(self.Page02_setNGImagebutton4)

        self.horizontalLayoutWidget_18 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(0, 430, 411, 31))
        self.Page02_setOKImageLayout4 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.Page02_setOKImageLayout4.setObjectName(u"Page02_setOKImageLayout4")
        self.Page02_setOKImageLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page02_setOKImageLabel4 = QLabel(self.horizontalLayoutWidget_18)
        self.Page02_setOKImageLabel4.setObjectName(u"Page02_setOKImageLabel4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_setOKImageLabel4)

        self.Page02_setOKImagelineEdit4 = QLineEdit(self.horizontalLayoutWidget_18)
        self.Page02_setOKImagelineEdit4.setObjectName(u"Page02_setOKImagelineEdit4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_setOKImagelineEdit4)

        self.Page02_setOKImagebutton4 = QPushButton(self.horizontalLayoutWidget_18)
        self.Page02_setOKImagebutton4.setObjectName(u"Page02_setOKImagebutton4")

        self.Page02_setOKImageLayout4.addWidget(self.Page02_setOKImagebutton4)

        self.horizontalLayoutWidget_19 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(430, 440, 350, 31))
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

        self.Page02_OKImageSaveButton4 = QPushButton(self.horizontalLayoutWidget_19)
        self.Page02_OKImageSaveButton4.setObjectName(u"Page02_OKImageSaveButton4")

        self.Page02_CaptureLayout4.addWidget(self.Page02_OKImageSaveButton4)

        self.Page02_NGImageSaveButton4 = QPushButton(self.horizontalLayoutWidget_19)
        self.Page02_NGImageSaveButton4.setObjectName(u"Page02_NGImageSaveButton4")

        self.Page02_CaptureLayout4.addWidget(self.Page02_NGImageSaveButton4)

        self.horizontalLayoutWidget_20 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(20, 0, 751, 421))
        self.Page02_CameraImage4 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.Page02_CameraImage4.setObjectName(u"Page02_CameraImage4")
        self.Page02_CameraImage4.setContentsMargins(0, 0, 0, 0)
        self.CameratabWidget.addTab(self.tab_4, "")
        self.stackedWidget.addWidget(self.Page02)
        self.Page03 = QWidget()
        self.Page03.setObjectName(u"Page03")
        self.Page03_groupBox1 = QGroupBox(self.Page03)
        self.Page03_groupBox1.setObjectName(u"Page03_groupBox1")
        self.Page03_groupBox1.setGeometry(QRect(0, 10, 791, 61))
        self.horizontalLayoutWidget_22 = QWidget(self.Page03_groupBox1)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(390, 10, 401, 31))
        self.Page03_RecordLayout1 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.Page03_RecordLayout1.setObjectName(u"Page03_RecordLayout1")
        self.Page03_RecordLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel1 = QLabel(self.horizontalLayoutWidget_22)
        self.Page03_RecordCapLabel1.setObjectName(u"Page03_RecordCapLabel1")
        self.Page03_RecordCapLabel1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordCapLabel1)

        self.Page03_RecordCapSpinBox1 = QSpinBox(self.horizontalLayoutWidget_22)
        self.Page03_RecordCapSpinBox1.setObjectName(u"Page03_RecordCapSpinBox1")
        self.Page03_RecordCapSpinBox1.setMaximum(99)

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordCapSpinBox1)

        self.Page03_RecordStartButton1 = QPushButton(self.horizontalLayoutWidget_22)
        self.Page03_RecordStartButton1.setObjectName(u"Page03_RecordStartButton1")

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordStartButton1)

        self.Page03_RecordEndButton1 = QPushButton(self.horizontalLayoutWidget_22)
        self.Page03_RecordEndButton1.setObjectName(u"Page03_RecordEndButton1")

        self.Page03_RecordLayout1.addWidget(self.Page03_RecordEndButton1)

        self.horizontalLayoutWidget_21 = QWidget(self.Page03_groupBox1)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(660, 40, 131, 21))
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
        self.horizontalLayoutWidget_23.setGeometry(QRect(0, 10, 381, 31))
        self.Page03_setVideoDirLayout1 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirLayout1.setObjectName(u"Page03_setVideoDirLayout1")
        self.Page03_setVideoDirLayout1.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel1 = QLabel(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirLabel1.setObjectName(u"Page03_setVideoDirLabel1")

        self.Page03_setVideoDirLayout1.addWidget(self.Page03_setVideoDirLabel1)

        self.Page03_setVideoDirlineEdit1 = QLineEdit(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirlineEdit1.setObjectName(u"Page03_setVideoDirlineEdit1")

        self.Page03_setVideoDirLayout1.addWidget(self.Page03_setVideoDirlineEdit1)

        self.Page03_setVideoDirbutton1 = QPushButton(self.horizontalLayoutWidget_23)
        self.Page03_setVideoDirbutton1.setObjectName(u"Page03_setVideoDirbutton1")

        self.Page03_setVideoDirLayout1.addWidget(self.Page03_setVideoDirbutton1)

        self.Page03_groupBox2 = QGroupBox(self.Page03)
        self.Page03_groupBox2.setObjectName(u"Page03_groupBox2")
        self.Page03_groupBox2.setGeometry(QRect(0, 80, 791, 61))
        self.horizontalLayoutWidget_24 = QWidget(self.Page03_groupBox2)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(390, 10, 401, 31))
        self.Page03_RecordLayout2 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.Page03_RecordLayout2.setObjectName(u"Page03_RecordLayout2")
        self.Page03_RecordLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel2 = QLabel(self.horizontalLayoutWidget_24)
        self.Page03_RecordCapLabel2.setObjectName(u"Page03_RecordCapLabel2")
        self.Page03_RecordCapLabel2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordCapLabel2)

        self.Page03_RecordCapSpinBox2 = QSpinBox(self.horizontalLayoutWidget_24)
        self.Page03_RecordCapSpinBox2.setObjectName(u"Page03_RecordCapSpinBox2")

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordCapSpinBox2)

        self.Page03_RecordStartButton2 = QPushButton(self.horizontalLayoutWidget_24)
        self.Page03_RecordStartButton2.setObjectName(u"Page03_RecordStartButton2")

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordStartButton2)

        self.Page03_RecordEndButton2 = QPushButton(self.horizontalLayoutWidget_24)
        self.Page03_RecordEndButton2.setObjectName(u"Page03_RecordEndButton2")

        self.Page03_RecordLayout2.addWidget(self.Page03_RecordEndButton2)

        self.horizontalLayoutWidget_25 = QWidget(self.Page03_groupBox2)
        self.horizontalLayoutWidget_25.setObjectName(u"horizontalLayoutWidget_25")
        self.horizontalLayoutWidget_25.setGeometry(QRect(660, 40, 131, 21))
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
        self.horizontalLayoutWidget_26.setGeometry(QRect(0, 10, 381, 31))
        self.Page03_setVideoDirLayout2 = QHBoxLayout(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirLayout2.setObjectName(u"Page03_setVideoDirLayout2")
        self.Page03_setVideoDirLayout2.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel2 = QLabel(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirLabel2.setObjectName(u"Page03_setVideoDirLabel2")

        self.Page03_setVideoDirLayout2.addWidget(self.Page03_setVideoDirLabel2)

        self.Page03_setVideoDirlineEdit2 = QLineEdit(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirlineEdit2.setObjectName(u"Page03_setVideoDirlineEdit2")

        self.Page03_setVideoDirLayout2.addWidget(self.Page03_setVideoDirlineEdit2)

        self.Page03_setVideoDirbutton2 = QPushButton(self.horizontalLayoutWidget_26)
        self.Page03_setVideoDirbutton2.setObjectName(u"Page03_setVideoDirbutton2")

        self.Page03_setVideoDirLayout2.addWidget(self.Page03_setVideoDirbutton2)

        self.Page03_groupBox3 = QGroupBox(self.Page03)
        self.Page03_groupBox3.setObjectName(u"Page03_groupBox3")
        self.Page03_groupBox3.setGeometry(QRect(0, 150, 791, 61))
        self.horizontalLayoutWidget_27 = QWidget(self.Page03_groupBox3)
        self.horizontalLayoutWidget_27.setObjectName(u"horizontalLayoutWidget_27")
        self.horizontalLayoutWidget_27.setGeometry(QRect(390, 10, 401, 31))
        self.Page03_RecordLayout3 = QHBoxLayout(self.horizontalLayoutWidget_27)
        self.Page03_RecordLayout3.setObjectName(u"Page03_RecordLayout3")
        self.Page03_RecordLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel3 = QLabel(self.horizontalLayoutWidget_27)
        self.Page03_RecordCapLabel3.setObjectName(u"Page03_RecordCapLabel3")
        self.Page03_RecordCapLabel3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordCapLabel3)

        self.Page03_RecordCapSpinBox3 = QSpinBox(self.horizontalLayoutWidget_27)
        self.Page03_RecordCapSpinBox3.setObjectName(u"Page03_RecordCapSpinBox3")

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordCapSpinBox3)

        self.Page03_RecordStartButton3 = QPushButton(self.horizontalLayoutWidget_27)
        self.Page03_RecordStartButton3.setObjectName(u"Page03_RecordStartButton3")

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordStartButton3)

        self.Page03_RecordEndButton3 = QPushButton(self.horizontalLayoutWidget_27)
        self.Page03_RecordEndButton3.setObjectName(u"Page03_RecordEndButton3")

        self.Page03_RecordLayout3.addWidget(self.Page03_RecordEndButton3)

        self.horizontalLayoutWidget_28 = QWidget(self.Page03_groupBox3)
        self.horizontalLayoutWidget_28.setObjectName(u"horizontalLayoutWidget_28")
        self.horizontalLayoutWidget_28.setGeometry(QRect(660, 40, 131, 21))
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
        self.horizontalLayoutWidget_29.setGeometry(QRect(0, 10, 381, 31))
        self.Page03_setVideoDirLayout3 = QHBoxLayout(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirLayout3.setObjectName(u"Page03_setVideoDirLayout3")
        self.Page03_setVideoDirLayout3.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel3 = QLabel(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirLabel3.setObjectName(u"Page03_setVideoDirLabel3")

        self.Page03_setVideoDirLayout3.addWidget(self.Page03_setVideoDirLabel3)

        self.Page03_setVideoDirlineEdit3 = QLineEdit(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirlineEdit3.setObjectName(u"Page03_setVideoDirlineEdit3")

        self.Page03_setVideoDirLayout3.addWidget(self.Page03_setVideoDirlineEdit3)

        self.Page03_setVideoDirbutton3 = QPushButton(self.horizontalLayoutWidget_29)
        self.Page03_setVideoDirbutton3.setObjectName(u"Page03_setVideoDirbutton3")

        self.Page03_setVideoDirLayout3.addWidget(self.Page03_setVideoDirbutton3)

        self.Page03_groupBox4 = QGroupBox(self.Page03)
        self.Page03_groupBox4.setObjectName(u"Page03_groupBox4")
        self.Page03_groupBox4.setGeometry(QRect(0, 220, 791, 61))
        self.horizontalLayoutWidget_62 = QWidget(self.Page03_groupBox4)
        self.horizontalLayoutWidget_62.setObjectName(u"horizontalLayoutWidget_62")
        self.horizontalLayoutWidget_62.setGeometry(QRect(390, 10, 401, 31))
        self.Page03_RecordLayout4 = QHBoxLayout(self.horizontalLayoutWidget_62)
        self.Page03_RecordLayout4.setObjectName(u"Page03_RecordLayout4")
        self.Page03_RecordLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page03_RecordCapLabel4 = QLabel(self.horizontalLayoutWidget_62)
        self.Page03_RecordCapLabel4.setObjectName(u"Page03_RecordCapLabel4")
        self.Page03_RecordCapLabel4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordCapLabel4)

        self.Page03_RecordCapSpinBox4 = QSpinBox(self.horizontalLayoutWidget_62)
        self.Page03_RecordCapSpinBox4.setObjectName(u"Page03_RecordCapSpinBox4")

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordCapSpinBox4)

        self.Page03_RecordStartButton4 = QPushButton(self.horizontalLayoutWidget_62)
        self.Page03_RecordStartButton4.setObjectName(u"Page03_RecordStartButton4")

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordStartButton4)

        self.Page03_RecordEndButton4 = QPushButton(self.horizontalLayoutWidget_62)
        self.Page03_RecordEndButton4.setObjectName(u"Page03_RecordEndButton4")

        self.Page03_RecordLayout4.addWidget(self.Page03_RecordEndButton4)

        self.horizontalLayoutWidget_63 = QWidget(self.Page03_groupBox4)
        self.horizontalLayoutWidget_63.setObjectName(u"horizontalLayoutWidget_63")
        self.horizontalLayoutWidget_63.setGeometry(QRect(660, 40, 131, 21))
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
        self.horizontalLayoutWidget_64.setGeometry(QRect(0, 10, 381, 31))
        self.Page03_setVideoDirLayout4 = QHBoxLayout(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirLayout4.setObjectName(u"Page03_setVideoDirLayout4")
        self.Page03_setVideoDirLayout4.setContentsMargins(0, 0, 0, 0)
        self.Page03_setVideoDirLabel4 = QLabel(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirLabel4.setObjectName(u"Page03_setVideoDirLabel4")

        self.Page03_setVideoDirLayout4.addWidget(self.Page03_setVideoDirLabel4)

        self.Page03_setVideoDirlineEdit4 = QLineEdit(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirlineEdit4.setObjectName(u"Page03_setVideoDirlineEdit4")

        self.Page03_setVideoDirLayout4.addWidget(self.Page03_setVideoDirlineEdit4)

        self.Page03_setVideoDirbutton4 = QPushButton(self.horizontalLayoutWidget_64)
        self.Page03_setVideoDirbutton4.setObjectName(u"Page03_setVideoDirbutton4")

        self.Page03_setVideoDirLayout4.addWidget(self.Page03_setVideoDirbutton4)

        self.stackedWidget.addWidget(self.Page03)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(11, 10, 171, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu_LivepushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_LivepushButton.setObjectName(u"Menu_LivepushButton")

        self.verticalLayout.addWidget(self.Menu_LivepushButton)

        self.Menu_CapturepushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_CapturepushButton.setObjectName(u"Menu_CapturepushButton")

        self.verticalLayout.addWidget(self.Menu_CapturepushButton)

        self.Menu_RecordpushButton = QPushButton(self.verticalLayoutWidget)
        self.Menu_RecordpushButton.setObjectName(u"Menu_RecordpushButton")

        self.verticalLayout.addWidget(self.Menu_RecordpushButton)

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
        self.Page02_ImageLabel1.setText("")
        self.Page02_setNGImageLabel1.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CaptureLabel1.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton1.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton1.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_OKImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_NGImageSaveButton1.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page02_setOKImageLabel1.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton1.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"CAM1", None))
        self.Page02_setOKImageLabel2.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CaptureLabel2.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton2.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton2.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_OKImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_NGImageSaveButton2.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.Page02_setNGImageLabel2.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"CAM2", None))
        self.Page02_setNGImageLabel3.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_setOKImageLabel3.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton3.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CaptureLabel3.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_OKImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_NGImageSaveButton3.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
        self.CameratabWidget.setTabText(self.CameratabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"CAM3", None))
        self.Page02_setNGImageLabel4.setText(QCoreApplication.translate("MainWindow", u"NG \uc774\ubbf8\uc9c0:", None))
        self.Page02_setNGImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_setOKImageLabel4.setText(QCoreApplication.translate("MainWindow", u"OK \uc774\ubbf8\uc9c0:", None))
        self.Page02_setOKImagebutton4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Page02_CaptureLabel4.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Page02_CaptureSetButton4.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.Page02_CaptureReleaseButton4.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.Page02_OKImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"OK \uc800\uc7a5", None))
        self.Page02_NGImageSaveButton4.setText(QCoreApplication.translate("MainWindow", u"NG \uc800\uc7a5", None))
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
        self.Menu_LivepushButton.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.Menu_CapturepushButton.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.Menu_RecordpushButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654", None))
        self.MenubarLabel.setText("")
    # retranslateUi

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.isRecordStatus = False
        self.isCreateFile = False
        self.isOversizeStatus = False
        self.isCreateOversizeFile = False

        self.cameraWindowWidth, self.cameraWindowHeight = 0, 0
        self.isDrawRectangleStatus, self.isDrawingEnded = False, False
        self.startX, self.startY, self.endX, self.endY = 0, 0, 0, 0

        self.setupUi(self)
        self.setupCamra()
        self.setupRecord()
        self.setupCapture()
        self.setupMenuBar()

## MenuBar(BEGIN)
    def setupMenuBar(self):
        self.capturePageOn = False
        self.Menu_LivepushButton.clicked.connect(lambda: self.changeStackWidget(0))
        self.Menu_CapturepushButton.clicked.connect(lambda: self.changeStackWidget(1))
        self.Menu_RecordpushButton.clicked.connect(lambda: self.changeStackWidget(2))

    def changeStackWidget(self, id):
        PageIdList = [self.Page01, self.Page02, self.Page03]

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

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.cameraWindowWidth)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cameraWindowHeight)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayVideoStream)
        self.timer.start(30)

    def displayVideoStream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.flip(frame, 1)
        self.frameRecording(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        liveImage = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        liveImage1 = liveImage.scaled(self.Page01_CameraImage1.geometry().width(), self.Page01_CameraImage1.geometry().height())
        self.Page01_LiveImagelabel.setPixmap(QPixmap.fromImage(liveImage1))

        frame, x, y, width, height = self.drawRectangleRegion(frame)
        capImage = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        captureImage1 = capImage.scaled(self.Page02_CameraImage1.geometry().width(), self.Page02_CameraImage1.geometry().height())
        self.Page02_ImageLabel1.setPixmap(QPixmap.fromImage(captureImage1))
        self.capImage = capImage.copy(x, y, width, height)
## WebCam Image(ENDED)

## Record(START)
    def setupRecord(self):
        self.strVideoFile = self.Page03_setVideoDirlineEdit1.text() + "Video.mp4"  # original video
        self.tempVideoFileForMERGE = "tempMergeVideo.mp4"  # temp for Merge original

        self.Page03_RecordStartButton1.clicked.connect(lambda: self.recordStatus(True))
        self.Page03_RecordEndButton1.clicked.connect(lambda: self.recordStatus(False))

    def recordStatus(self, isBoolState):
        self.isRecordStatus = isBoolState
        strRecordStatus = "(녹화중)" if isBoolState else "(녹화해제)"
        self.Page03_RecordStatuslabel1.setText(strRecordStatus)
        self.maxRecordStorage = self.Page03_RecordCapSpinBox1.value()
        self.Page03_RecordCapSpinBox1.setDisabled(isBoolState)

        print("{} maxRecordStorage: {}(MB)".format(strRecordStatus, self.maxRecordStorage))

    def frameRecording(self, frame):
        if self.isRecordStatus:
            frameHeight, frameWidth = frame.shape[:2]
            offsetX = frameWidth - self.cameraWindowWidth
            offsetY = (frameHeight - self.cameraWindowHeight) // 2
            frame = frame[offsetY : offsetY + self.cameraWindowHeight, offsetX: offsetX + self.cameraWindowWidth] #cropImage

            ### Create Video File from Frame (START) - (NOTE: 'Codec: mp4v, 확장자:mp4'를 사용해야 VideoWriter 및 VideoFileClip 클래스가 정상적으로 동작함.)
            if not self.isOversizeStatus:
                if not self.isCreateFile:
                    self.videoCodec = cv2.VideoWriter_fourcc(*'mp4v')
                    self.videoWriterOriginal = cv2.VideoWriter(self.strVideoFile, self.videoCodec, 30.0,
                                                               (self.cameraWindowWidth, self.cameraWindowHeight))
                    self.isCreateFile = True
                    print("isCreateFile: {}".format(self.isCreateFile))

                self.videoWriterOriginal.write(frame)
                fileSize = os.path.getsize(self.strVideoFile)
            else:
                if not self.isCreateOversizeFile:
                    self.videoCodec = cv2.VideoWriter_fourcc(*'mp4v')
                    self.videoWriterMergeFile = cv2.VideoWriter(self.tempVideoFileForMERGE, self.videoCodec, 30.0,
                                                                (self.cameraWindowWidth, self.cameraWindowHeight))
                    self.isCreateOversizeFile = True
                    print("isCreateFile: {}".format(self.isCreateFile))
                self.videoWriterMergeFile.write(frame)
                fileSize = os.path.getsize(self.strVideoFile) + os.path.getsize(self.tempVideoFileForMERGE)
            ### Create Video File from Frame (ENDED)

            if self.maxRecordStorage * 1024 * 1024 < fileSize:  # 1MB = 1048576
                if not self.isOversizeStatus:
                    self.videoWriterOriginal.release()          #Orignal Video File을 release해주어 앞부분 cut할 수 있도록 해줌.
                else:
                    self.videoWriterMergeFile.release()
                    self.mergeVideoFile(self.strVideoFile, self.tempVideoFileForMERGE, self.strVideoFile)
                    self.isCreateOversizeFile = False

                self.cutVideoFile(10, self.strVideoFile)             #cut Video prev 10sec.
                self.isOversizeStatus = True
        else:
            if not self.isOversizeStatus:
                if self.isCreateFile:
                    self.videoWriterOriginal.release()
                    self.isCreateFile = False
                    print("isCreateFile: {}".format(self.isCreateFile))
            else:
                if self.isCreateOversizeFile:
                    self.videoWriterMergeFile.release()
                    self.mergeVideoFile(self.strVideoFile, self.tempVideoFileForMERGE, self.strVideoFile)
                    self.isCreateOversizeFile = False
                    print("isCreateFile: {}".format(self.isCreateFile))

    def cutVideoFile(self, second, fileName):
        tempVideoFileforCUT = 'tempCutVideo.mp4'                            # temp for cut original
        with VideoFileClip(fileName) as video:
            new = video.subclip(second, video.duration)                     # cut prev 'second'
            new.write_videofile(tempVideoFileforCUT, audio_codec='aac')     # 앞의 영상을 자르는 동작을 정상적으로 해주기 위해 audio_codec에 대해 설정해 줌.
        os.remove(fileName)
        os.rename(tempVideoFileforCUT, fileName)                            # tempVideoFileforCUT을 Orignal Video File Name으로 변경해주어 저장.

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
## Record(ENDED)

## Capture(BEGIN)
    def setupCapture(self):
        self.isStPosOnImage = False
        self.capImgStartX, self.capImgStartY, self.capImgEndX, self.capImgEndY = 212, 30, 962, 450  ### Note: Image Mouse Postion

        self.Page02_OKImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(0))
        self.Page02_NGImageSaveButton1.clicked.connect(lambda: self.saveCaptureImage(1))
        self.Page02_CaptureSetButton1.clicked.connect(lambda: self.drawRectangleStatus(True))
        self.Page02_CaptureReleaseButton1.clicked.connect(lambda: self.drawRectangleStatus(False))
        self.Page03_setVideoDirbutton1.clicked.connect(lambda: self.setDirectory(0))
        self.Page02_setOKImagebutton1.clicked.connect(lambda: self.setDirectory(1))
        self.Page02_setNGImagebutton1.clicked.connect(lambda: self.setDirectory(2))

    def setDirectory(self, id): ## 0 Video, 1: OK Image, 2: NG Image
        dirName = QFileDialog.getExistingDirectory(self, self.tr("저장 경로 설정"), "./", QFileDialog.ShowDirsOnly)
        print(dirName)
        if id == 0:
            self.Page03_setVideoDirlineEdit1.setText(dirName)
            self.strVideoFile = dirName + "/Video.mp4"  # original video
            print(self.strVideoFile)
        elif id == 1:
            self.Page02_setOKImagelineEdit1.setText(dirName)
        elif id == 2:
            self.Page02_setNGImagelineEdit1.setText(dirName)

    def drawRectangleRegion(self, frame):
        if self.isDrawRectangleStatus and self.isDrawingEnded:
            frameHeight, frameWidth = frame.shape[:2]

            ratioX = frameWidth / self.cameraWindowWidth
            ratioY = frameHeight / self.cameraWindowHeight
            drawMargin = 2  # 이미지캡쳐에서 rectangle이 포함되지 않도록 drawMargin 추가

            stPosX, stPosY, endPosX, endPosY= int(self.startX * ratioX), int(self.startY * ratioY), int(self.endX * ratioX), int(self.endY * ratioY)

            frame = cv2.rectangle(frame, (stPosX - drawMargin, stPosY - drawMargin),
                                   (endPosX + drawMargin, endPosY + drawMargin), (0, 0, 255), 2)
            return frame, stPosX, stPosY, endPosX - stPosX, endPosY - stPosY
        else:
            return frame, 0, 0, frame.shape[1], frame.shape[0]

    def mousePressEvent(self, QMouseEvent):
        if self.capturePageOn and self.capImgStartX < QMouseEvent.x() <= self.capImgEndX and self.capImgStartY < QMouseEvent.y() <= self.capImgEndY:
            self.isStPosOnImage = True
        else:
            self.isStPosOnImage = False
            return

        self.isDrawingEnded = False
        self.startX, self.startY = QMouseEvent.x(), QMouseEvent.y()

    def mouseReleaseEvent(self, QMouseEvent):
        if not self.isStPosOnImage:
            return

        self.isDrawingEnded = True
        self.endX, self.endY = QMouseEvent.x(), QMouseEvent.y()

        if self.endX < self.startX:
            self.startX, self.endX = self.endX, self.startX
        if self.endY < self.startY:
            self.startY, self.endY = self.endY, self.startY

        if self.startX < self.capImgStartX : self.startX = self.capImgStartX
        if self.startY < self.capImgStartY : self.startY = self.capImgStartY
        if self.endX >= self.capImgEndX    : self.endX = self.capImgEndX
        if self.endY >= self.capImgEndY    : self.endY = self.capImgEndY

        self.startX -= self.capImgStartX
        self.startY -= self.capImgStartY
        self.endX -= self.capImgStartX
        self.endY -= self.capImgStartY

    def drawRectangleStatus(self, isBoolState):
        self.isDrawRectangleStatus = isBoolState
        print("isDrawRectangleStatus: {}".format(self.isDrawRectangleStatus))

    def saveCaptureImage(self, id): # id - 0:OK, 1: NG
        imageNumber = 1
        tempCurPwd = os.getcwd()
        if id == 0 and (len(self.Page02_setOKImagelineEdit1.text()) > 0):
            os.chdir(self.Page02_setOKImagelineEdit1.text()) # Move TO Save PWD
        elif id == 1 and (len(self.Page02_setNGImagelineEdit1.text()) > 0):
            os.chdir(self.Page02_setNGImagelineEdit1.text()) # Move TO Save PWD

        while True:
            if cv2.imread("image.jpg") is None:
                self.capImage.save("image.jpg")
                break

            fileName = "image(" + str(imageNumber) + ").jpg"
            if cv2.imread(fileName) is None:
                self.capImage.save(fileName)
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