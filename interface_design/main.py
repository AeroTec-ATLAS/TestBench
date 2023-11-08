import os
import sys

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI files
from ui_interface import Ui_MainWindow
from stackWidgets.stepTestMenu.stepTestWidget import stepTestWidget
from stackWidgets.rampTestMenu.rampTestWidget import rampTestWidget

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
        self.ui.setupUi(MainWindow)      # Set up the UI elements on this QMainWindow instanc


        self.include_step_test_widget()

        self.setup_fundamental_functionalities()

    def include_step_test_widget(self):
        # Associate stepTestWidget Class to the stepTestInterface Frame in the main interface
        self.ui.stepTestInterface = stepTestWidget(self.ui.stepTestInterface)

        # Define stepTestWidget buttoms functionalities
        self.ui.stepTestInterface.ui.ReturnBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.automaticControlMenu))



        
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

    






#execute app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create a QApplication instance
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowInterface(MainWindow)         # Create an instance of the MainWindowInterface class
    MainWindow.show()
    sys.exit(app.exec_())                  # Start the application event loop

