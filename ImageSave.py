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

import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 584)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 751, 421))
        self.CameraImage = QHBoxLayout(self.horizontalLayoutWidget)
        self.CameraImage.setObjectName(u"CameraImage")
        self.CameraImage.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(440, 440, 321, 31))
        self.RecordLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.RecordLayout.setObjectName(u"RecordLayout")
        self.RecordLayout.setContentsMargins(0, 0, 0, 0)
        self.RecordCapLabel = QLabel(self.horizontalLayoutWidget_2)
        self.RecordCapLabel.setObjectName(u"RecordCapLabel")
        self.RecordCapLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.RecordLayout.addWidget(self.RecordCapLabel)

        self.RecordCapSpinBox = QSpinBox(self.horizontalLayoutWidget_2)
        self.RecordCapSpinBox.setObjectName(u"RecordCapSpinBox")

        self.RecordLayout.addWidget(self.RecordCapSpinBox)

        self.RecordStartButton = QPushButton(self.horizontalLayoutWidget_2)
        self.RecordStartButton.setObjectName(u"RecordStartButton")

        self.RecordLayout.addWidget(self.RecordStartButton)

        self.RecordEndButton = QPushButton(self.horizontalLayoutWidget_2)
        self.RecordEndButton.setObjectName(u"RecordEndButton")

        self.RecordLayout.addWidget(self.RecordEndButton)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(470, 500, 291, 31))
        self.CaptureLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.CaptureLayout.setObjectName(u"CaptureLayout")
        self.CaptureLayout.setContentsMargins(0, 0, 0, 0)
        self.CaptureLabel = QLabel(self.horizontalLayoutWidget_3)
        self.CaptureLabel.setObjectName(u"CaptureLabel")

        self.CaptureLayout.addWidget(self.CaptureLabel)

        self.CaptureSetButton = QPushButton(self.horizontalLayoutWidget_3)
        self.CaptureSetButton.setObjectName(u"CaptureSetButton")

        self.CaptureLayout.addWidget(self.CaptureSetButton)

        self.CaptureReleaseButton = QPushButton(self.horizontalLayoutWidget_3)
        self.CaptureReleaseButton.setObjectName(u"CaptureReleaseButton")

        self.CaptureLayout.addWidget(self.CaptureReleaseButton)

        self.CaptureSaveButton = QPushButton(self.horizontalLayoutWidget_3)
        self.CaptureSaveButton.setObjectName(u"CaptureSaveButton")

        self.CaptureLayout.addWidget(self.CaptureSaveButton)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(620, 470, 141, 21))
        self.RecordStatusLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.RecordStatusLayout.setObjectName(u"RecordStatusLayout")
        self.RecordStatusLayout.setContentsMargins(0, 0, 0, 0)
        self.RecordStatusTitle = QLabel(self.horizontalLayoutWidget_4)
        self.RecordStatusTitle.setObjectName(u"RecordStatusTitle")
        self.RecordStatusTitle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.RecordStatusLayout.addWidget(self.RecordStatusTitle)

        self.RecordStatuslabel = QLabel(self.horizontalLayoutWidget_4)
        self.RecordStatuslabel.setObjectName(u"RecordStatuslabel")
        self.RecordStatuslabel.setTextFormat(Qt.AutoText)
        self.RecordStatuslabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.RecordStatusLayout.addWidget(self.RecordStatuslabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RecordCapLabel.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc6a9\ub7c9", None))
        self.RecordStartButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc2dc\uc791", None))
        self.RecordEndButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\ud574\uc81c", None))
        self.CaptureLabel.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.CaptureSetButton.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.CaptureReleaseButton.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.CaptureSaveButton.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.RecordStatusTitle.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc0c1\ud0dc:", None))
        self.RecordStatuslabel.setText(QCoreApplication.translate("MainWindow", u"(\ub179\ud654\uc911)", None))
    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_view = MainWindow()
    main_view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
