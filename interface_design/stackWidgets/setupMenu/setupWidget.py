import sys
import csv

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI file
if __name__ == "__main__":
    from setupInterface import Ui_Frame 
else:
    from stackWidgets.setupMenu.setupInterface import Ui_Frame


# Main window class
class setupWidget(QtWidgets.QWidget):
    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance


        # Properties:
        self.powerTrain = {
            'esc':'',
            'motor': '',
            'propeller': '',
            'powerSource':''
        }  

        # Connect the textChanged signal to the onTextChanged slot
        self.ui.motorLabel.textChanged.connect(self.onTextChanged)
        self.ui.escLabel.textChanged.connect(self.onTextChanged)
        self.ui.propellerLabel.textChanged.connect(self.onTextChanged)
        self.ui.powerSourceLabel.textChanged.connect()
    def onTextChanged(self, text):
        # This method will be called whenever the text in the QLineEdit changes
        self.powerTrain['esc'] = str(self.ui.motorLabel.line_edit.text())
        self.powerTrain['motor'] = str(self.ui.motorLabel.line_edit.text())
        self.powerTrain['propeller'] = str(self.ui.motorLabel.line_edit.text())
        self.powerTrain['powerSource'] = str(self.ui.motorLabel.line_edit.text())

#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = setupWidget(Frame)
    Frame.show()
    sys.exit(app.exec_())




