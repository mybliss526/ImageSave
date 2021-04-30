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
        self.RecordCapSpinBox.setValue(20)
        self.RecordCapSpinBox.setMinimum(5)
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
        self.RecordCapLabel.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc6a9\ub7c9(MB)", None))
        self.RecordStartButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc2dc\uc791", None))
        self.RecordEndButton.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\ud574\uc81c", None))
        self.CaptureLabel.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.CaptureSetButton.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\uc124\uc815", None))
        self.CaptureReleaseButton.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc5ed\ud574\uc81c", None))
        self.CaptureSaveButton.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.RecordStatusTitle.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654\uc0c1\ud0dc:", None))
        self.RecordStatuslabel.setText(QCoreApplication.translate("MainWindow", u"(녹화해제)", None))
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
        frame, x, y, width, height = self.drawRectangleRegion(frame)

        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.ImageLabel.setPixmap(QPixmap.fromImage(image))
        self.capImage = image.copy(x, y, width, height)
## WebCam Image(ENDED)

## Record(START)
    def setupRecord(self):
        self.RecordStartButton.clicked.connect(lambda: self.recordStatus(True))
        self.RecordEndButton.clicked.connect(lambda: self.recordStatus(False))

    def recordStatus(self, isBoolState):
        self.isRecordStatus = isBoolState
        strRecordStatus = "(녹화중)" if isBoolState else "(녹화해제)"
        self.RecordStatuslabel.setText(strRecordStatus)
        self.maxRecordStorage = self.RecordCapSpinBox.value()
        self.RecordCapSpinBox.setDisabled(isBoolState)

        print("{} maxRecordStorage: {}(MB)".format(strRecordStatus, self.maxRecordStorage))

    def frameRecording(self, frame):
        strVideoFile = "Video.mp4"                      #original video
        tempVideoFileForMERGE = "tempMergeVideo.mp4"    #temp for Merge original

        if self.isRecordStatus:
            frameHeight, frameWidth = frame.shape[:2]
            offsetX = frameWidth - self.cameraWindowWidth
            offsetY = (frameHeight - self.cameraWindowHeight) // 2
            frame = frame[offsetY : offsetY + self.cameraWindowHeight, offsetX: offsetX + self.cameraWindowWidth] #cropImage

            ### Create Video File from Frame (START) - (NOTE: 'Codec: mp4v, 확장자:mp4'를 사용해야 VideoWriter 및 VideoFileClip 클래스가 정상적으로 동작함.)
            if not self.isOversizeStatus:
                if not self.isCreateFile:
                    self.videoCodec = cv2.VideoWriter_fourcc(*'mp4v')
                    self.videoWriterOriginal = cv2.VideoWriter(strVideoFile, self.videoCodec, 30.0,
                                                               (self.cameraWindowWidth, self.cameraWindowHeight))
                    self.isCreateFile = True
                    print("isCreateFile: {}".format(self.isCreateFile))

                self.videoWriterOriginal.write(frame)
                fileSize = os.path.getsize(strVideoFile)
            else:
                if not self.isCreateOversizeFile:
                    self.videoCodec = cv2.VideoWriter_fourcc(*'mp4v')
                    self.videoWriterMergeFile = cv2.VideoWriter(tempVideoFileForMERGE, self.videoCodec, 30.0,
                                                                (self.cameraWindowWidth, self.cameraWindowHeight))
                    self.isCreateOversizeFile = True
                    print("isCreateFile: {}".format(self.isCreateFile))
                self.videoWriterMergeFile.write(frame)
                fileSize = os.path.getsize(strVideoFile) + os.path.getsize(tempVideoFileForMERGE)
            ### Create Video File from Frame (ENDED)

            if self.maxRecordStorage * 1024 * 1024 < fileSize:  # 1MB = 1048576
                if not self.isOversizeStatus:
                    self.videoWriterOriginal.release()          #Orignal Video File을 release해주어 앞부분 cut할 수 있도록 해줌.
                else:
                    self.videoWriterMergeFile.release()
                    self.mergeVideoFile(strVideoFile, tempVideoFileForMERGE, strVideoFile)
                    self.isCreateOversizeFile = False

                self.cutVideoFile(10, strVideoFile)             #cut Video prev 10sec.
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
                    self.mergeVideoFile(strVideoFile, tempVideoFileForMERGE, strVideoFile)
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
        self.CaptureSaveButton.clicked.connect(self.saveCaptureImage)
        self.CaptureSetButton.clicked.connect(lambda: self.drawRectangleStatus(True))
        self.CaptureReleaseButton.clicked.connect(lambda: self.drawRectangleStatus(False))

    def drawRectangleRegion(self, frame):
        if self.isDrawRectangleStatus and self.isDrawingEnded:
            frameHeight, frameWidth = frame.shape[:2]
            offsetX = frameWidth - self.cameraWindowWidth
            offsetY = (frameHeight - self.cameraWindowHeight) // 2
            drawMargin = 2      #이미지캡쳐에서 rectangle이 포함되지 않도록 drawMargin 추가
            frame = cv2.rectangle(frame, (offsetX + self.startX - drawMargin, offsetY + self.startY - drawMargin),
                                  (offsetX + self.endX + drawMargin, offsetY + self.endY + drawMargin), (0, 0, 255), 2)
            return frame, offsetX + self.startX, offsetY + self.startY, self.endX - self.startX, self.endY - self.startY
        else:
            return frame, 0, 0, self.cameraWindowWidth, self.cameraWindowHeight

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

    def drawRectangleStatus(self, isBoolState):
        self.isDrawRectangleStatus = isBoolState
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
