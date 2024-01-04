import sys
import os
import copy

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI file
if __name__ == "__main__":
    from setupInterface import Ui_Frame 
else:
    from stackWidgets.setupMenu.setupInterface import Ui_Frame


# Main window class
class setupFrame(QtWidgets.QWidget):
    
    # Define a signal that will be emitted when the properties are updated
    updated = QtCore.pyqtSignal()

    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance

        self.powerTrain = {
            'motor': '',
            'propeller': '',
            'esc': '',
            'powerSource': '',
        }  

        self.workingDirectory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DesktopLocation)

        self.systemLimits = {
            ("Tension (V)", "Min System Cutoff"): -2,
            ("Tension (V)", "Max System Cutoff"): 90,
            ("Current (A)", "Min System Cutoff"): -2,
            ("Current (A)", "Max System Cutoff"): 155,
            ("Thrust (Kg)", "Min System Cutoff"): 0,
            ("Thrust (Kg)", "Max System Cutoff"): 10,
            ("Torque (Kg)", "Min System Cutoff"): -2,
            ("Torque (Kg)", "Max System Cutoff"): 90,
            ("RPM", "Min System Cutoff"): -2,
            ("RPM", "Max System Cutoff"): 155,
            ("Vibrations", "Min System Cutoff"): 0,
            ("Vibrations", "Max System Cutoff"): 10 
        }

        self.safetyLimits = {
            ("Tension (V)", "Cutoff Min"): -2,
            ("Tension (V)", "Cutoff Max"): 90,
            ("Current (A)", "Cutoff Min"): -2,
            ("Current (A)", "Cutoff Max"): 155,
            ("Thrust (Kg)", "Cutoff Min"): 0,
            ("Thrust (Kg)", "Cutoff Max"): 10,
            ("Torque (Kg)", "Cutoff Min"): -2,
            ("Torque (Kg)", "Cutoff Max"): 90,
            ("RPM", "Cutoff Min"): -2,
            ("RPM", "Cutoff Max"): 155,
            ("Vibrations", "Cutoff Min"): 0,
            ("Vibrations", "Cutoff Max"): 10 
        }
        self.numberTapes = 0

        # Connect the textChanged signal to the onTextChanged slot
        self.ui.motorLabel.textChanged.connect(self.update_powertrain_motor)
        self.ui.escLabel.textChanged.connect(self.update_powertrain_esc)
        self.ui.propellerLabel.textChanged.connect(self.update_powertrain_propeller)
        self.ui.powerSourceLabel.textChanged.connect(self.update_powertrain_powerSource)

       # Associate workspace directory
        self.ui.folderDirectoryBtn.clicked.connect(self.update_working_directory)
        self.ui.folderDirectoryLEdit.setText(str(self.workingDirectory))

        # Define number of tapes
        self.ui.nTapesSpinBox.valueChanged.connect(self.update_number_tapes)

        # Associate tables changes
        self.ui.safetyLimitsTable.itemChanged.connect(self.update_safety_limites)

        # Make last two columns in safety limits table uneditable
        for row in range(self.ui.safetyLimitsTable.rowCount()):
            for column in range(self.ui.safetyLimitsTable.columnCount()-2, self.ui.safetyLimitsTable.columnCount()):
                item = self.ui.safetyLimitsTable.item(row, column)
                if item != None:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def update_powertrain_motor(self):
        self.powerTrain['motor'] = str(self.ui.motorLabel.text())
        # Emit the updated signal when properties are updated
        self.updated.emit()

    def update_powertrain_esc(self):
        self.powerTrain['esc'] = str(self.ui.escLabel.text())
        # Emit the updated signal when properties are updated
        self.updated.emit()

    def update_powertrain_propeller(self):
        self.powerTrain['propeller'] = str(self.ui.propellerLabel.text())
        # Emit the updated signal when properties are updated
        self.updated.emit()

    def update_powertrain_powerSource(self):
        self.powerTrain['powerSource'] = str(self.ui.powerSourceLabel.text())
        # Emit the updated signal when properties are updated
        self.updated.emit()

    def update_working_directory(self):
        """ Define Working Directory to save files """
        options = QtWidgets.QFileDialog.Options()
        self.workingDirectory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Folder", self.workingDirectory, options=options)
        self.ui.folderDirectoryLEdit.setText(str(self.workingDirectory))
        self.updated.emit()

    def update_safety_limites(self, item):
        row = item.row()
        column = item.column()
        value = float(item.text())

        rowHeader = self.ui.safetyLimitsTable.verticalHeaderItem(row).text()
        columnHeader = self.ui.safetyLimitsTable.horizontalHeaderItem(column).text()

        if columnHeader == 'Cutoff Min' and value > self.systemLimits[(rowHeader, "Min System Cutoff")]:
            self.safetyLimits[(rowHeader, columnHeader)] = value
            self.updated.emit()

        elif columnHeader == 'Cutoff Max' and value < self.systemLimits[(rowHeader, "Max System Cutoff")]:
            self.safetyLimits[(rowHeader, columnHeader)] = value
            self.updated.emit()

    def update_number_tapes(self):
        self.numberTapes = self.ui.nTapesSpinBox.value()
        self.updated.emit()


#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = setupFrame(Frame)
    Frame.show()
    sys.exit(app.exec_())
