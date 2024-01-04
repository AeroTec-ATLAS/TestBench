import sys
import csv
import os

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


# Import GUI file
if __name__ == "__main__":
    from manualTestInterface import Ui_Frame
else:
    from stackWidgets.manualTestMenu.manualTestInterface import Ui_Frame

# Main window class
class manualTestFrame(QtWidgets.QWidget):

    dataUpdated = QtCore.pyqtSignal()
    dataCleared = QtCore.pyqtSignal()

    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance

        self.motorArmed = False
        self.workingDirectory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DesktopLocation)
        self.currentData = {}
        self.fullData = [{'1': "text"}]
        self.sampleData = []
        #self.sampleFileName = None
        #self.fullFileName = None
        self.throttle = 0


        # Connect take Sample and record btns signals to respective actions:
        self.ui.takeSampleBtn.clicked.connect(self.add_sampleData_element)
        self.dataUpdated.connect(self.add_recorded_data)
        
        
        # Connect to changes in file names
        self.ui.sampleLEdit.textChanged.connect(self.update_file_names)
        self.ui.fullDataLEdit.textChanged.connect(self.update_file_names)
        self.update_file_names()

        # Connect saveDataBtn
        self.ui.saveDataBtn.clicked.connect(self.save_test_data)

        #conncet clearData btn
        self.ui.clearDataBtn.clicked.connect(self.clear_test_data)
    
        # Connect the valueChanged signal of the spin box and slider
        self.ui.escValueSpinBox.valueChanged.connect(lambda: self.update_trotlle('spinBox'))
        self.ui.escValueSlider.valueChanged.connect(lambda: self.update_trotlle('slider'))

        # conncet to the value changes signal of the armMotor Checkbox
        self.ui.armMotorBtn.stateChanged.connect(self.change_motor_state)
        self.change_motor_state(False)


    # Used by the main program to update test data 
    def update_data(self, value):
        self.currentData = value
        self.dataUpdated.emit()

    # Update List of manual samples - Take Sample option
    def add_sampleData_element(self, value):
        self.sampleData.append(self.currentData)
        print(self.sampleData)
    
    # Update list of automatic samples - Record option
    def add_recorded_data(self):
        if self.ui.recordBtn.isChecked():
            self.fullData.append(self.currentData)

    # Define names of the files to save data after test
    def update_file_names(self):
        self.sampleFileName = self.ui.sampleLEdit.text()
        self.fullFileName = self.ui.fullDataLEdit.text()

    def save_test_data(self):
        # Open a file dialog to get the file path
        options = QtWidgets.QFileDialog.Options()
        
        if len(self.sampleData) + len(self.fullData) > 0:
            # Open a QFileDialog to select a folder
            folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Test Results Folder', self.workingDirectory)
            if folder_path != None:
                folder_path = QtCore.QDir(self.workingDirectory).filePath(folder_path)
                # Use QDir to join the desktop directory with a subdirectory
                sampleData_directory = QtCore.QDir(folder_path).filePath(self.sampleFileName)
                fullData_directory = QtCore.QDir(folder_path).filePath(self.fullFileName)

                # Save sample Data
                if len(self.sampleData) > 0:
                    sample_file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save CSV File for Sample Data", sampleData_directory, "CSV Files (*.csv);;All Files (*)", options=options)
                    
                    if sample_file_path != None:
                        self.write_csv(self.sampleData, sample_file_path)
                        self.sampleData.clear()
                        QtWidgets.QMessageBox.information(self, 'Warning', 'Sample data has been saved with success!')

                # Save full data
                if len(self.fullData) > 0:   
                    full_file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save CSV File for Recording Data", fullData_directory, "CSV Files (*.csv);;All Files (*)", options=options)
                    
                    if full_file_path != None:
                        self.write_csv(self.fullData, full_file_path)
                        self.fullData.clear()
                        QtWidgets.QMessageBox.information(self, 'Warning', 'Recorded data has been saved with success!')

                    self.write_csv(self.fullData,full_file_path)
                self.dataCleared.emit()
        else:
            QtWidgets.QMessageBox.information(self, 'Warning', 'There is no data to be saved!')

        
    # Copy data from test to a csv file
    def write_csv(self, dataSet, filename):
        fieldnames = list(dataSet[0].keys()) # dataSet is a list of dictionaries

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataSet)

    def write_powerTrain_file (self, file):

        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the formatted data to the file
            for key, value in configuration_data.items():
                file.write(f"{key}: {value}\n")



    # Clear test data
    def clear_test_data(self):
        if len(self.sampleData) + len(self.fullData) != 0:
            dialog = DataCleanDialog()
            dialog.show()

            loop = QtCore.QEventLoop()
            dialog.clean.connect(loop.quit)

            # Connect the clean_data method to clear_data slot
            dialog.clean.connect(self.clear_data)
            loop.exec_()  # This will block until the event loop is quit (when the dialog emits clean signal)

        else:
            self.clear_data(True)
        
    def clear_data(self, value):
        if value:
            QtWidgets.QMessageBox.information(self, 'Data Cleaned', 'Data has been cleaned!')
            self.fullData.clear()
            self.sampleData.clear()
            self.dataCleared.emit()

    # Chhange are and disarmed position od the slider
    def change_motor_state(self, state):
        if state:
            self.ui.escValueSlider.setEnabled(True)
            self.ui.escValueSpinBox.setEnabled(True)

        else:
            self.ui.escValueSlider.setValue(0)
            self.ui.escValueSpinBox.setValue(0)
            self.throttle = 0

            self.ui.escValueSlider.setEnabled(False)
            self.ui.escValueSpinBox.setEnabled(False)

    #define throttle
    def update_trotlle(self, element):
        if element == 'spinBox':
            self.throttle = self.ui.escValueSpinBox.value()
            self.ui.escValueSlider.setValue(self.throttle)

        else:
            self.throttle = self.ui.escValueSlider.value()
            self.ui.escValueSpinBox.setValue(self.throttle)


class DataCleanDialog(QtWidgets.QWidget):
    clean = QtCore.pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        vbox = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Data set is not saved. Are you sure you want to clean the data?")
        vbox.addWidget(label)

        yes_button = QtWidgets.QPushButton('Yes', self)
        yes_button.clicked.connect(self.confirm)
        vbox.addWidget(yes_button)

        cancel_button = QtWidgets.QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.cancel)
        vbox.addWidget(cancel_button)

        self.setLayout(vbox)

        self.setWindowTitle('Clear Test Data')
        self.setGeometry(300, 300, 300, 150)

    def confirm(self):
        self.clean.emit(True)
        self.close()

    def cancel(self):
        self.clean.emit(False)
        self.close()



#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = manualTestFrame(Frame)
    Frame.show()
    sys.exit(app.exec_())




