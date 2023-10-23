import os
import sys

#import Pyqt5
from PyQt5.QtGui import QPainter 

#IMPORT CUSTOM WIDGETS
from Custom_Widgets.Widgets import *

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


# Main window class
class MainWindowInterface(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(MainWindow)      # Set up the UI elements on this QMainWindow instance

        self.timer = QTimer(MainWindow)       # Create a QTimer instance
        self.timer.timeout.connect(self.update_data_container)  # Connect timer timeout signal to update function
        self.timer.start(1000)           # Update every 100 milliseconds (0.1 second)

        self.ui.setupBtn.clicked.connect(self.open_setup_menu)
        self.ui.manualControlBtn.clicked.connect(self.open_manual_control_menu)
        self.ui.automaticControlBtn.clicked.connect(self.open_automatic_control_menu)
        self.ui.resultsBtn.clicked.connect(self.open_results_menu)
        self.ui.settingsBtn.clicked.connect(self.open_settings_menu)
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
        current_data["thrust"] = random.uniform(0, 100)
        current_data["torque"] = random.uniform(0, 100)
        current_data["rpm"] = random.uniform(0, 5000)
        current_data["motor_temp"] = random.uniform(0, 100)
        current_data["esc_temp"] = random.uniform(0, 100)
        current_data["voltage"] = random.uniform(0, 50)
        current_data["current"] = random.uniform(0, 50)
        current_data["airspeed"] = random.uniform(0, 200)
        current_data["noise"] = random.uniform(0, 100)

    def open_setup_menu(self):
        self.ui.mainMenu.setCurrentWidget(self.ui.setupMenu)
    
    def open_manual_control_menu(self):
        self.ui.mainMenu.setCurrentWidget(self.ui.manualControlMenu)
    
    def open_automatic_control_menu(self):
        self.ui.mainMenu.setCurrentWidget(self.ui.automaticControlMenu)

    def open_results_menu(self):
        self.ui.mainMenu.setCurrentWidget(self.ui.resultsMenu)
       
    def open_settings_menu(self):
        self.ui.mainMenu.setCurrentWidget(self.ui.settingsMenu)
    



        




#execute app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create a QApplication instance
    MainWindow = QtWidgets.QMainWindow()
    
    ui = MainWindowInterface(MainWindow)         # Create an instance of the MainWindowInterface class
    MainWindow.show()
    sys.exit(app.exec_())                  # Start the application event loop

