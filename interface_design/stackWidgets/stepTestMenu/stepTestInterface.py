# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepTestMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(546, 525)
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
        self.scrollArea = QtWidgets.QScrollArea(Frame)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 532, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.stepReturnMenu = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.stepReturnMenu.setFont(font)
        self.stepReturnMenu.setWhatsThis("")
        self.stepReturnMenu.setAutoFillBackground(False)
        self.stepReturnMenu.setStyleSheet("")
        self.stepReturnMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stepReturnMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stepReturnMenu.setLineWidth(1)
        self.stepReturnMenu.setObjectName("stepReturnMenu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.stepReturnMenu)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stepReturnBtn = QtWidgets.QPushButton(self.stepReturnMenu)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stepReturnBtn.setPalette(palette)
        self.stepReturnBtn.setObjectName("stepReturnBtn")
        self.horizontalLayout_3.addWidget(self.stepReturnBtn)
        self.label_7 = QtWidgets.QLabel(self.stepReturnMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setMouseTracking(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_35.addWidget(self.stepReturnMenu)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_35.addWidget(self.line_2)
        self.stepSequenceEditorMenu = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.stepSequenceEditorMenu.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.stepSequenceEditorMenu.setFont(font)
        self.stepSequenceEditorMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stepSequenceEditorMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stepSequenceEditorMenu.setObjectName("stepSequenceEditorMenu")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.stepSequenceEditorMenu)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_11 = QtWidgets.QLabel(self.stepSequenceEditorMenu)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_33.addWidget(self.label_11)
        self.frame_5 = QtWidgets.QFrame(self.stepSequenceEditorMenu)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.stepAddNewLineBtn = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepAddNewLineBtn.setFont(font)
        self.stepAddNewLineBtn.setObjectName("stepAddNewLineBtn")
        self.horizontalLayout_21.addWidget(self.stepAddNewLineBtn, 0, QtCore.Qt.AlignLeft)
        self.stepClearTableBtn = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepClearTableBtn.setFont(font)
        self.stepClearTableBtn.setObjectName("stepClearTableBtn")
        self.horizontalLayout_21.addWidget(self.stepClearTableBtn)
        self.stepToolsBtn = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepToolsBtn.sizePolicy().hasHeightForWidth())
        self.stepToolsBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepToolsBtn.setFont(font)
        self.stepToolsBtn.setObjectName("stepToolsBtn")
        self.horizontalLayout_21.addWidget(self.stepToolsBtn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_33.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.stepSequenceEditorTable = QtWidgets.QTableWidget(self.stepSequenceEditorMenu)
        self.stepSequenceEditorTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stepSequenceEditorTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stepSequenceEditorTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stepSequenceEditorTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.stepSequenceEditorTable.setAutoScroll(True)
        self.stepSequenceEditorTable.setAutoScrollMargin(0)
        self.stepSequenceEditorTable.setAlternatingRowColors(False)
        self.stepSequenceEditorTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.stepSequenceEditorTable.setShowGrid(True)
        self.stepSequenceEditorTable.setGridStyle(QtCore.Qt.SolidLine)
        self.stepSequenceEditorTable.setWordWrap(True)
        self.stepSequenceEditorTable.setCornerButtonEnabled(True)
        self.stepSequenceEditorTable.setObjectName("stepSequenceEditorTable")
        self.stepSequenceEditorTable.setColumnCount(4)
        self.stepSequenceEditorTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stepSequenceEditorTable.setItem(1, 2, item)
        self.stepSequenceEditorTable.horizontalHeader().setVisible(True)
        self.stepSequenceEditorTable.horizontalHeader().setHighlightSections(True)
        self.stepSequenceEditorTable.verticalHeader().setVisible(False)
        self.verticalLayout_33.addWidget(self.stepSequenceEditorTable, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.stepSequenceEditorMenu)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_22.addWidget(self.label_9)
        self.stepNumLoopsLEdit = QtWidgets.QLineEdit(self.frame_6)
        self.stepNumLoopsLEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepNumLoopsLEdit.setFont(font)
        self.stepNumLoopsLEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stepNumLoopsLEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stepNumLoopsLEdit.setPlaceholderText("")
        self.stepNumLoopsLEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.stepNumLoopsLEdit.setClearButtonEnabled(False)
        self.stepNumLoopsLEdit.setObjectName("stepNumLoopsLEdit")
        self.horizontalLayout_22.addWidget(self.stepNumLoopsLEdit)
        self.verticalLayout_33.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_35.addWidget(self.stepSequenceEditorMenu)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_35.addWidget(self.line_4)
        self.stepSequencePreviewMenu = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepSequencePreviewMenu.sizePolicy().hasHeightForWidth())
        self.stepSequencePreviewMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.stepSequencePreviewMenu.setFont(font)
        self.stepSequencePreviewMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stepSequencePreviewMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stepSequencePreviewMenu.setObjectName("stepSequencePreviewMenu")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.stepSequencePreviewMenu)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.stepSequencePreviewMenu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8, 0, QtCore.Qt.AlignTop)
        self.stepPreviewTestGraphic = PlotWidget(self.stepSequencePreviewMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepPreviewTestGraphic.sizePolicy().hasHeightForWidth())
        self.stepPreviewTestGraphic.setSizePolicy(sizePolicy)
        self.stepPreviewTestGraphic.setObjectName("stepPreviewTestGraphic")
        self.verticalLayout_13.addWidget(self.stepPreviewTestGraphic)
        self.verticalLayout_35.addWidget(self.stepSequencePreviewMenu)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_35.addWidget(self.line_3)
        self.stepSequenceRunnerMenu = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepSequenceRunnerMenu.sizePolicy().hasHeightForWidth())
        self.stepSequenceRunnerMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.stepSequenceRunnerMenu.setFont(font)
        self.stepSequenceRunnerMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stepSequenceRunnerMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stepSequenceRunnerMenu.setObjectName("stepSequenceRunnerMenu")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.stepSequenceRunnerMenu)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_10 = QtWidgets.QLabel(self.stepSequenceRunnerMenu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_18.addWidget(self.label_10)
        self.frame_18 = QtWidgets.QFrame(self.stepSequenceRunnerMenu)
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.verticalLayout_18.addWidget(self.frame_18)
        self.frame_33 = QtWidgets.QFrame(self.stepSequenceRunnerMenu)
        self.frame_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_12 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_20.addWidget(self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_33)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_20.addWidget(self.lineEdit_2)
        self.verticalLayout_18.addWidget(self.frame_33)
        self.pushButton_3 = QtWidgets.QPushButton(self.stepSequenceRunnerMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_18.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_35.addWidget(self.stepSequenceRunnerMenu, 0, QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.stepReturnBtn.setText(_translate("Frame", "Back"))
        self.label_7.setText(_translate("Frame", "Step Test Wizard"))
        self.label_11.setText(_translate("Frame", "Sequence Editor"))
        self.stepAddNewLineBtn.setText(_translate("Frame", "New Line"))
        self.stepClearTableBtn.setText(_translate("Frame", "Clear Table"))
        self.stepToolsBtn.setText(_translate("Frame", "Tools"))
        item = self.stepSequenceEditorTable.verticalHeaderItem(0)
        item.setText(_translate("Frame", "New Row"))
        item = self.stepSequenceEditorTable.verticalHeaderItem(1)
        item.setText(_translate("Frame", "New Row"))
        item = self.stepSequenceEditorTable.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Time (s)"))
        item = self.stepSequenceEditorTable.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Esc Throttle (μs)"))
        item = self.stepSequenceEditorTable.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Take Sample"))
        __sortingEnabled = self.stepSequenceEditorTable.isSortingEnabled()
        self.stepSequenceEditorTable.setSortingEnabled(False)
        item = self.stepSequenceEditorTable.item(0, 0)
        item.setText(_translate("Frame", "0"))
        item = self.stepSequenceEditorTable.item(0, 1)
        item.setText(_translate("Frame", "1000"))
        self.stepSequenceEditorTable.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("Frame", "Number of Loops"))
        self.stepNumLoopsLEdit.setText(_translate("Frame", "1"))
        self.label_8.setText(_translate("Frame", "Sequence Preview"))
        self.label_10.setText(_translate("Frame", "Sequence Runner"))
        self.radioButton_3.setText(_translate("Frame", "Continuously record data during test"))
        self.label_12.setText(_translate("Frame", "Document Title:"))
        self.pushButton_3.setText(_translate("Frame", "Execute Sequence"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
