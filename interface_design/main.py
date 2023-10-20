import os
import sys

#import Pyqt5
from PyQt5.QtGui import QPainter 

#IMPORT CUSTOM WIDGETS
from Custom_Widgets.Widgets import *

# Import GUI file
from ui_interface import *

#import math mod
#from random import randrange
from functools import partial

# imprt csv
import csv


# Main window class
class MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SET MINIMUM WINDOW SIZE
        self.setMiniumSize(10000, 2000)

        # Connect button clicks to switching containers in QStackedWidget
        self.ui.setupBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setupMenu))
        self.ui.powerTrainBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.powerTrainMenu))
        self.ui.manualControlBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.manualControlMenu))
        self.ui.automaticControlBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.automaticControlMenu))
        self.ui.resultsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.resultsMenu))
        
        #show window
        self.show()

#execute app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
