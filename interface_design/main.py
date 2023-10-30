import os
import sys

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI file
from ui_interface import Ui_MainWindow

#import math mod
#from random import randrange
from functools import partial

# imprt csv
import csv
import random

# Dictionary to store sensor data values
current_data ={
    "thrust": 0,
    "torque": 0,
    "rpm"   : 0,
    "motor_temp": 0,
    "esc_temp"  : 0,
    "voltage"   : 0,
    "current"   : 0,
    "airspeed"  : 0,
    "noise": 0   
     
}

trash = [i for i in range(100)]

# Main window class
class MainWindowInterface(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(MainWindow)      # Set up the UI elements on this QMainWindow instance
        self.setup_fundamental_functionalities()
        self.stepMenuTestSetup()

        
    def setup_fundamental_functionalities(self):
        self.timer1 = QtCore.QTimer(MainWindow)       # Create a QTimer instance
        self.timer1.timeout.connect(self.update_data_container)  # Connect timer timeout signal to update function
        self.timer1.start(100)           # Update every 100 milliseconds (0.1 second)

        
        # Associate buttoms to correspondent functionalities:
        # Left container Btns
        self.ui.setupBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.setupMenu))
        self.ui.manualControlBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.manualControlMenu))
        self.ui.automaticControlBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.automaticControlMenu))
        self.ui.resultsBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.resultsMenu))
        self.ui.settingsBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.settingsMenu))
        self.ui.exitBtn.clicked.connect(sys.exit)

    def update_data_container(self):
        # Update current_data dictionary with random continuous values
        self.update_data()

        # Update labels with current data values
        self.ui.ThrustValueText.setText(str(current_data["thrust"]))
        self.ui.TorqueValueText.setText(str(current_data["torque"]))
        self.ui.RpmValueText.setText(str(current_data["rpm"]))
        self.ui.MotorTempValueText.setText(str(current_data["motor_temp"]))
        self.ui.EscTempValueText.setText(str(current_data["esc_temp"]))
        self.ui.VoltageValueText.setText(str(current_data["voltage"]))
        self.ui.CurrentValueText.setText(str(current_data["current"]))
        self.ui.AirspeedValueText.setText(str(current_data["airspeed"]))
        self.ui.NoiseValueText.setText(str(current_data["noise"]))

    def update_data(self): # develop serial communication here
        
        # Assign random continuous values to the current_data dictionary
        current_data["thrust"] = random.choice(trash)
        current_data["torque"] = random.choice(trash)
        current_data["rpm"] = random.choice(trash)
        current_data["motor_temp"] = random.choice(trash)
        current_data["esc_temp"] = random.choice(trash)
        current_data["voltage"] = random.choice(trash)
        current_data["current"] = random.choice(trash)
        current_data["airspeed"] = random.choice(trash)
        current_data["noise"] = random.choice(trash)

    def stepMenuTestSetup(self):
        
        # List (of dictionaries) to store the data from ta table to the execution of the step test
        self.stepTestSequence = list()

        # Define Pattern functionalities:
        #self.ui.stepToolsBtn.clicked.connect()
        self.ui.stepAddNewLineBtn.clicked.connect(self.add_row_to_table)
        self.ui.stepClearTableBtn.clicked.connect(self.delete_table)
        self.ui.stepPreviewTestGraphic.setBackground('w')  # 'w' represents white color
        self.ui.stepPreviewTestGraphic.setMouseEnabled(x=False, y=False)
        #self.ui.stepPreviewTestGraphic.setRange(xrange=[0, None], yRange=[0, None])
        self.update_test_sequence()
        self.update_sequence_preview()

        # Define properties related to the step Sequence Editor Table
        for row in range(self.ui.stepSequenceEditorTable.rowCount()):
            self.step_update_table(row)

        # Connect the itemChanged signal from the table to to the custom method
        self.ui.stepSequenceEditorTable.itemChanged.connect(self.update_test_sequence)
        self.ui.stepNumLoopsLEdit.textChanged.connect(self.update_test_sequence)


    def step_update_table(self, row):

        """ Create rows in the table according to the format: line edit - checkbox - line edit - push btn """
          
        # Add line edit for columns 0 and 2 (Time and Throttle)
        #line_edit_time = QtWidgets.QLineEdit()
        #line_edit_throttle = QtWidgets.QLineEdit()
        #self.ui.stepSequenceEditorTable.setCellWidget(row, 0, line_edit_time)
        #self.ui.stepSequenceEditorTable.setCellWidget(row, 2, line_edit_throttle)

        # Add checkbox for column 1 (Save Sample)
        checkbox = QtWidgets.QCheckBox()
        checkbox_layout = QtWidgets.QHBoxLayout()
        checkbox_layout.setAlignment(QtCore.Qt.AlignLeft)  # Align the content to the left
        checkbox_layout.addWidget(checkbox)
        
        # Set the layout for checkbox
        checkbox_widget = QtWidgets.QWidget()
        checkbox_widget.setLayout(checkbox_layout)
        self.ui.stepSequenceEditorTable.setCellWidget(row, 2, checkbox_widget)

        # Add push button for column 3 (Delete row)
        push_button = QtWidgets.QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons-black/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        push_button.setIcon(icon)
        push_button.clicked.connect(lambda _, r=row: self.delete_row(r))
        
        # Create a horizontal layout for the button
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignRight)  # Align the content to the left
        button_layout.addWidget(push_button)
        

        # Set the layout as the button's layout
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(button_layout)
        button_widget.setStyleSheet("border: none; background-color: transparent;")  
        self.ui.stepSequenceEditorTable.setCellWidget(row, 3, button_widget)


    def delete_table(self):
        for row in range(1, self.ui.stepSequenceEditorTable.rowCount()):
            self.delete_row(row)


    def delete_row(self, row):
        """Delete the selected row from the table"""
        if self.ui.stepSequenceEditorTable.rowCount() != 0:
            self.ui.stepSequenceEditorTable.removeRow(row)
            self.update_test_sequence()


    def add_row_to_table(self):
        """Add row to the table"""
        current_row_count = self.ui.stepSequenceEditorTable.rowCount()
        self.ui.stepSequenceEditorTable.insertRow(current_row_count)
        self.step_update_table(self.ui.stepSequenceEditorTable.rowCount()-1)


    def update_test_sequence(self):
        """Update Sequence Preview based on the table data"""
        self.stepTestSequence.clear()

        for row in range(self.ui.stepSequenceEditorTable.rowCount()):
            time = self.ui.stepSequenceEditorTable.item(row, 0)
            esc_trotlle = self.ui.stepSequenceEditorTable.item(row, 1) 

            if time != None and esc_trotlle != None:
                time = int(time.text())
                esc_trotlle = int(esc_trotlle.text())
                self.stepTestSequence.append((time, esc_trotlle))

        num_loops = int(self.ui.stepNumLoopsLEdit.text())
        print(num_loops)
        if num_loops > 1:
            sequence_len = len(self.stepTestSequence)

            for i in range(num_loops-1):
                for j in range(1, sequence_len):
                    self.stepTestSequence.append((self.stepTestSequence[j][0] + self.stepTestSequence[sequence_len-1][0], self.stepTestSequence[j][1]))

        print(self.stepTestSequence)
        
        self.update_sequence_preview()


    def update_sequence_preview(self):
        x_data = list()
        y_data = list()
        
        self.ui.stepPreviewTestGraphic.clear()  # Clear previous plot data
    
        for time in range(len(self.stepTestSequence) - 1):
            x_start, x_end = self.stepTestSequence[time][0], self.stepTestSequence[time + 1][0]
            y_value = self.stepTestSequence[time][1]  # Y-value is the throttle value from the list
            
            # Append data points to the lists
            x_data.extend([x_start, x_end])
            y_data.extend([y_value, y_value])

            # Plot horizontal line between x_start and x_end with y_value
            self.ui.stepPreviewTestGraphic.plot(x_data, y_data, pen=pg.mkPen(color=(255, 165, 0), width=2))








#execute app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create a QApplication instance
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowInterface(MainWindow)         # Create an instance of the MainWindowInterface class
    MainWindow.show()
    sys.exit(app.exec_())                  # Start the application event loop

