# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\manualTestInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(743, 590)
        Frame.setStyleSheet("*{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"#headerLine{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerTab = QtWidgets.QFrame(Frame)
        self.headerTab.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headerTab.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerTab.setObjectName("headerTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.headerTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.headerTab)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.headerTab, 0, QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(Frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(Frame)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 731, 492))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dataRecordFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.dataRecordFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dataRecordFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataRecordFrame.setObjectName("dataRecordFrame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.dataRecordFrame)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_6 = QtWidgets.QFrame(self.dataRecordFrame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_19 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_13.addWidget(self.label_19)
        self.verticalLayout_18.addWidget(self.frame_6)
        self.saveDataFrame = QtWidgets.QFrame(self.dataRecordFrame)
        self.saveDataFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.saveDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveDataFrame.setObjectName("saveDataFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.saveDataFrame)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.filesFrame = QtWidgets.QFrame(self.saveDataFrame)
        self.filesFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filesFrame.setObjectName("filesFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.filesFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnFrame = QtWidgets.QFrame(self.filesFrame)
        self.btnFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.btnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnFrame.setObjectName("btnFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.btnFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.takeSampleBtn = QtWidgets.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.takeSampleBtn.setFont(font)
        self.takeSampleBtn.setAutoDefault(False)
        self.takeSampleBtn.setDefault(False)
        self.takeSampleBtn.setFlat(False)
        self.takeSampleBtn.setObjectName("takeSampleBtn")
        self.verticalLayout_7.addWidget(self.takeSampleBtn)
        self.recordBtn = QtWidgets.QCheckBox(self.btnFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recordBtn.setFont(font)
        self.recordBtn.setTristate(False)
        self.recordBtn.setObjectName("recordBtn")
        self.verticalLayout_7.addWidget(self.recordBtn)
        self.horizontalLayout_3.addWidget(self.btnFrame)
        self.frame_12 = QtWidgets.QFrame(self.filesFrame)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_25 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_8.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_8.addWidget(self.label_26)
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.fileNamesFrame = QtWidgets.QFrame(self.filesFrame)
        self.fileNamesFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fileNamesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileNamesFrame.setObjectName("fileNamesFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fileNamesFrame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.sampleLEdit = QtWidgets.QLineEdit(self.fileNamesFrame)
        self.sampleLEdit.setText("")
        self.sampleLEdit.setObjectName("sampleLEdit")
        self.verticalLayout_9.addWidget(self.sampleLEdit)
        self.fullDataLEdit = QtWidgets.QLineEdit(self.fileNamesFrame)
        self.fullDataLEdit.setText("")
        self.fullDataLEdit.setObjectName("fullDataLEdit")
        self.verticalLayout_9.addWidget(self.fullDataLEdit)
        self.horizontalLayout_3.addWidget(self.fileNamesFrame)
        self.horizontalLayout_14.addWidget(self.filesFrame)
        self.dataChangeFrame = QtWidgets.QFrame(self.saveDataFrame)
        self.dataChangeFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dataChangeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataChangeFrame.setObjectName("dataChangeFrame")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.dataChangeFrame)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.saveDataBtn = QtWidgets.QPushButton(self.dataChangeFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saveDataBtn.setFont(font)
        self.saveDataBtn.setObjectName("saveDataBtn")
        self.horizontalLayout_17.addWidget(self.saveDataBtn)
        self.clearDataBtn = QtWidgets.QPushButton(self.dataChangeFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clearDataBtn.setFont(font)
        self.clearDataBtn.setObjectName("clearDataBtn")
        self.horizontalLayout_17.addWidget(self.clearDataBtn)
        self.horizontalLayout_14.addWidget(self.dataChangeFrame)
        self.verticalLayout_18.addWidget(self.saveDataFrame)
        self.verticalLayout_4.addWidget(self.dataRecordFrame)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.outputControlFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.outputControlFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.outputControlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputControlFrame.setObjectName("outputControlFrame")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.outputControlFrame)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_20 = QtWidgets.QFrame(self.outputControlFrame)
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_21 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_18.addWidget(self.label_21)
        self.verticalLayout_21.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.outputControlFrame)
        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QtWidgets.QLabel(self.frame_21)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/b_icons/icons-black/x.svg"))
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22, 0, QtCore.Qt.AlignLeft)
        self.label_23 = QtWidgets.QLabel(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_19.addWidget(self.label_23)
        self.verticalLayout_21.addWidget(self.frame_21)
        self.escTrottleControlFrame = QtWidgets.QFrame(self.outputControlFrame)
        self.escTrottleControlFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.escTrottleControlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.escTrottleControlFrame.setObjectName("escTrottleControlFrame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.escTrottleControlFrame)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_24 = QtWidgets.QLabel(self.escTrottleControlFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_20.addWidget(self.label_24)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem2)
        self.armMotorBtn = QtWidgets.QCheckBox(self.escTrottleControlFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.armMotorBtn.setFont(font)
        self.armMotorBtn.setText("")
        self.armMotorBtn.setObjectName("armMotorBtn")
        self.horizontalLayout_20.addWidget(self.armMotorBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.escValueSpinBox = QtWidgets.QSpinBox(self.escTrottleControlFrame)
        self.escValueSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.escValueSpinBox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.escValueSpinBox.setFont(font)
        self.escValueSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.escValueSpinBox.setMinimum(0)
        self.escValueSpinBox.setMaximum(100)
        self.escValueSpinBox.setSingleStep(1)
        self.escValueSpinBox.setProperty("value", 0)
        self.escValueSpinBox.setObjectName("escValueSpinBox")
        self.horizontalLayout_20.addWidget(self.escValueSpinBox)
        self.escValueSlider = QtWidgets.QSlider(self.escTrottleControlFrame)
        self.escValueSlider.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.escValueSlider.setFont(font)
        self.escValueSlider.setMinimum(0)
        self.escValueSlider.setMaximum(100)
        self.escValueSlider.setSingleStep(1)
        self.escValueSlider.setPageStep(50)
        self.escValueSlider.setSliderPosition(0)
        self.escValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.escValueSlider.setInvertedAppearance(False)
        self.escValueSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.escValueSlider.setObjectName("escValueSlider")
        self.horizontalLayout_20.addWidget(self.escValueSlider)
        self.verticalLayout_21.addWidget(self.escTrottleControlFrame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addWidget(self.outputControlFrame)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.plotFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy)
        self.plotFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plotFrame.setObjectName("plotFrame")
        self.verticalLayout_4.addWidget(self.plotFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Manual Test Menu"))
        self.label_19.setText(_translate("Frame", "Data Recorder"))
        self.takeSampleBtn.setText(_translate("Frame", "Take Sample"))
        self.recordBtn.setText(_translate("Frame", "Record"))
        self.label_25.setText(_translate("Frame", "Samples File Title"))
        self.label_26.setText(_translate("Frame", "Full File Title"))
        self.saveDataBtn.setText(_translate("Frame", "Save Data"))
        self.clearDataBtn.setText(_translate("Frame", "Clear Data"))
        self.label_21.setText(_translate("Frame", "Output Control"))
        self.label_23.setText(_translate("Frame", "Danger! Activating outputs may cause the motor to spin. Experiment without a propeller installed to get familiar with the operation. Never approach energized equipment while in software cutoff mode. Read the product user manual for more safety directives Press space bar to disarm the motor in case od danger. Press space bar to stop test"))
        self.label_24.setText(_translate("Frame", "Esc trotlle (%)"))
import black_icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())