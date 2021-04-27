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
import cv2

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
        self.ImageLabel = QLabel(self.horizontalLayoutWidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.CameraImage.addWidget(self.ImageLabel)

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



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.cameraWidth, self.cameraHeight = 0, 0
        self.isDrawRectangleStatus, self.isDrawingEnded = False, False
        self.startX, self.startY, self.endX, self.endY = 0, 0, 0, 0

        self.setupUi(self)
        self.setupCamra()
        self.setupCapture()

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
        self.cameraWidth, self.cameraHeight = self.CameraWindowSize(0)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.cameraWidth)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cameraHeight)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayVideoStream)
        self.timer.start(30)

    def displayVideoStream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)

        x, y, width, height = 0, 0, self.cameraWidth, self.cameraHeight
        if self.isDrawRectangleStatus and self.isDrawingEnded:
            frame, x, y, width, height = self.drawRectangleRegion(frame)
        else:
            x, y, width, height = 0, 0, self.cameraWidth, self.cameraHeight

        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.ImageLabel.setPixmap(QPixmap.fromImage(image))
        self.capImage = image.copy(x, y, width, height)
## WebCam Image(ENDED)

## Capture(BEGIN)
    def setupCapture(self):
        self.CaptureSaveButton.clicked.connect(self.saveCaptureImage)
        self.CaptureSetButton.clicked.connect(lambda: self.drawRectangleStatus(True))
        self.CaptureReleaseButton.clicked.connect(lambda: self.drawRectangleStatus(False))

    def drawRectangleRegion(self, frame):
        frameHeight, frameWidth = frame.shape[:2]
        offsetX = frameWidth - self.cameraWidth
        offsetY = (frameHeight - self.cameraHeight) // 2
        drawMargin = 2      #이미지캡쳐에서 rectangle이 포함되지 않도록 drawMargin 추가
        frame = cv2.rectangle(frame, (offsetX + self.startX - drawMargin, offsetY + self.startY - drawMargin),
                              (offsetX + self.endX + drawMargin, offsetY + self.endY + drawMargin), (0, 0, 255), 2)
        return frame, offsetX + self.startX, offsetY + self.startY, self.endX - self.startX, self.endY - self.startY

    def mousePressEvent(self, QMouseEvent):
        self.isDrawingEnded = False
        self.startX, self.startY = QMouseEvent.x(), QMouseEvent.y()

    def mouseReleaseEvent(self, QMouseEvent):
        self.isDrawingEnded = True
        self.endX, self.endY = QMouseEvent.x(), QMouseEvent.y()

        if self.endX < self.startX:
            self.startX, self.endX = self.endX, self.startX
        if self.endY < self.startY:
            self.startY, self.endY = self.endY, self.startY

        #code refactoring point!!(about. size)
        if self.startX < 9: self.startX = 9
        if self.startY < 9: self.startY = 9
        if self.endX >= 760: self.endX = 760
        if self.endY >= 430: self.endY = 430

        self.startX -= 9
        self.startY -= 9
        self.endX -= 9
        self.endY -= 9

    def drawRectangleStatus(self, isTrue):
        self.isDrawRectangleStatus = isTrue
        print("isDrawRectangleStatus: {}".format(self.isDrawRectangleStatus))

    def saveCaptureImage(self):
        imageNumber = 1
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
## Capture(ENDED)

def main():
    app = QApplication(sys.argv)
    main_view = MainWindow()
    main_view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
