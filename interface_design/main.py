import os
import sys

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import copy
import time

# Import task modules
import threading
import serial
import serial.tools.list_ports

# Import GUI files
from ui_interface import Ui_MainWindow
from stackWidgets.stepTestMenu.stepTestWidget import stepTestWidget
from stackWidgets.manualTestMenu.manualTestFrame import manualTestFrame
from stackWidgets.plotMenu.plotFrame import plotFrame
from stackWidgets.setupMenu.setupFrame import setupFrame

from stackWidgets.arduino.arduino import Arduino

# imprt csv
import csv
import random


# Dictionary to store sensor data values




trash = [i for i in range(100)]

# Main window class
class MainWindowInterface(QtWidgets.QMainWindow):

    manualTestFinished = QtCore.pyqtSignal()
    endArduinoIteraction = QtCore.pyqtSignal() 
    arduinoConnectionEstablished = QtCore.pyqtSignal() 
    arduinoConnectionLost = QtCore.pyqtSignal() 


    test_data = {
        'Time (s)': [],
        'Airspeed (m/s)': [],
        'Voltage (V)': [],
        'Current (A)': [],
        'Torque (N/m)': [],
        'Rpm': [],
        'Acceleration (m/s^2)': [],
        'Temperatura do Esc (ºC)': [],
        'Temperatura do Motor (ºC)': [],
        'Thrust (N)': [], 
    }
    
    current_data ={
        'Time (s)': 0,
        'Airspeed (m/s)': 0,
        'Voltage (V)': 0,
        'Current (A)': 0,
        'Torque (N/m)': 0,
        'Rpm': 0,
        'Acceleration (m/s^2)': 0,
        'Temperatura do Esc (ºC)': 0,
        'Temperatura do Motor (ºC)': 0,
        'Thrust (N)': 0, 
    }

    arduino = Arduino()

    def __init__(self, MainWindow):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(MainWindow)      # Set up the UI elements on this QMainWindow instanc

        self.throttle = 0

        self.setup_lateral_frame()
        self.include_setup_frame()
        self.include_manual_test_frame()
        self.include_plot_frame()
        
        self.setup_fundamental_functionalities()

        #self.connectionToArduino = threading.Thread(target=self.connectionToArduino, daemon=True)
        #self.connectionToArduino.start()
  
    def setup_lateral_frame(self):
        # define btn properties
        self.ui.connectStandBtn.clicked.connect(self.set_arduino_connection)
        #self.ui.tareSensorsBtn.clicked.connect(self.tare_sensors)
        self.ui.setupBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.setupMenu))
        self.ui.manualControlBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.manualTestMenu))
        self.ui.automaticControlBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.automaticControlMenu))
        self.ui.resultsBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.resultsMenu))

        # create a clock to update devices connected to the pc when arduino is not connected
        self.updatePortsTimer = QtCore.QTimer(MainWindow)      
        self.updatePortsTimer.timeout.connect(self.update_ports_box) 

        # create a clock to check if arduino is still connected to the pc 
        self.checkArduinoConnectionTimer = QtCore.QTimer(MainWindow)      
        self.checkArduinoConnectionTimer.timeout.connect(self.checkArduinoConnection) 

        # define initial condition of the lateral frame
        self.update_lateral_frame_disconnected()

        # define when the clock should be in execution ot not
        self.arduinoConnectionLost.connect(self.update_lateral_frame_disconnected)
        self.arduinoConnectionEstablished.connect(self.update_lateral_frame_connected)

    def update_ports_box(self):

        # remember the current elmenet selected
        currentItem = self.ui.portsBox.currentText()

        # get devices connected to the computer
        devices =  [p.description for p in serial.tools.list_ports.comports()]

        # update list
        self.ui.portsBox.clear()
        self.ui.portsBox.addItems(devices)
        self.ui.portsBox.addItem("")

        # make combo box show all the elements in the list at once:
        self.ui.portsBox.view().setMinimumHeight(self.ui.portsBox.view().sizeHintForRow(0) * self.ui.portsBox.count())

        # remember last choice
        self.ui.portsBox.setCurrentText(currentItem)

    # update lateral frame when connection to arduino is set
    def update_lateral_frame_connected(self): 
        self.ui.connectStandBtn.hide() 
        self.ui.portsBox.hide()
        self.ui.tareSensorsBtn.show()

        self.ui.measurementsContainer.show()
        self.ui.controlContainer.show()

        self.ui.manualControlBtn.setEnabled(True)
        self.ui.automaticControlBtn.setEnabled(True)

        self.updatePortsTimer.stop()


    # update lateral frame when connection to arduino is lost
    def update_lateral_frame_disconnected(self):
        self.ui.connectStandBtn.show() 
        self.ui.portsBox.show()
        self.ui.tareSensorsBtn.hide()

        self.ui.measurementsContainer.hide()
        self.ui.controlContainer.hide()

        # when connection is lost return to setup Menu
        self.ui.mainMenu.setCurrentWidget(self.ui.setupMenu)
        #self.ui.manualControlBtn.setEnabled(False)
        self.ui.automaticControlBtn.setEnabled(False)
        
        self.updatePortsTimer.start(500) # timer has a duration of 0.5 seconds


    def checkArduinoConnection(self):
        if self.arduino.ser.device in [str(p.device) for p in serial.tools.list_ports.comports()]:
            return
        
        self.arduino.conectionState = 0
        self.arduinoConnectionLost.emit()


    # Try to stablish connection with arduino
    def set_arduino_connection(self):

        # get the description of the device to connect
        deviceDescription = self.ui.portsBox.currentText()
        if deviceDescription == None:
            QtWidgets.QMessageBox.information(self, 'Error', 'No port selectec')
            return

        # get the port where arduino is connected
        port = [str(p.device) for p in serial.tools.list_ports.comports() if p.description == deviceDescription][0]
        
        # try stablish connection
        try:
            self.arduino.establish_connection(port)
            self.arduinoConnectionEstablished.emit() # emit signal after connection is established


        except serial.SerialException:                        
            QtWidgets.QMessageBox.critical(self, 'Error', 'Impossible to connect to arduino')
            return
        
        #self.arduinoDataTransmissionThread = threading.Thread(target = self.arduino.?????, daemon=True) # give indication to start the test
        #self.arduinoDataTransmissionThread.start()
        #self.arduinoConnectionLost.connect(self.stop_arduino_data_transmission)

        self.checkArduinoConnection.start(5000) # timer to check connection state of the arduino in each 5 seconds

    def stop_arduino_data_transmission(self):
        self.arduinoDataTransmissionThread._stop()
        self.arduinoDataTransmissionThread = None      

    def include_setup_frame(self):
        """Include the setupFrame into the main window"""
        self.ui.setupInterface = setupFrame(self.ui.setupInterface)

        self.powerTrain = self.ui.setupInterface.powerTrain
        self.workingDirectory = self.ui.setupInterface.workingDirectory
        self.numberTapes = self.ui.setupInterface.numberTapes
        self.safetyLimits = self.ui.setupInterface.safetyLimits
        
        self.ui.setupInterface.updated.connect(self.update_setup_properties)

    def update_setup_properties(self):
            # Update elements of the powerTrain
            for element, description in self.ui.setupInterface.powerTrain.items():
                self.powerTrain[element] = description

            # Update workspace directory
            self.workingDirectory = self.ui.setupInterface.workingDirectory
    
            # Update number of tapes
            self.numberTapes = self.ui.setupInterface.numberTapes
            
            # Update Safety Limits
            self.safetyLimits = self.ui.setupInterface.safetyLimits
            print(self.powerTrain.items())

            # Update labels
            self.ui.motorLabel.setText(str(self.powerTrain['motor']))
            self.ui.propellerLabel.setText(str(self.powerTrain['propeller']))
            self.ui.powerSourceLabel.setText(str(self.powerTrain['powerSource']))
            self.ui.escLabel.setText(str(self.powerTrain['esc']))
        
    def include_manual_test_frame(self):
        self.ui.manualTestFrame = manualTestFrame(self.ui.manualTestFrame)
        self.ui.manualTestFrame.workingDirectory = self.workingDirectory

        # Associate armMotorBtn with test Execution
        self.ui.manualTestFrame.ui.armMotorBtn.stateChanged.connect(self.check_manual_test_conditions)
    
    def include_plot_frame(self):
        self.ui.manualTestFrame.ui.plotFrame = plotFrame(self.ui.manualTestFrame.ui.plotFrame)
        

    # Preparing for manual test execution
    def check_manual_test_conditions(self):
        if self.ui.manualTestFrame.ui.armMotorBtn.isChecked():
            self.enable_leftMenu_btns(False) # Disable movement between pages when test is in execution
            for key in self.test_data.keys(): # Clear all the previous data
                self.test_data[key].clear()
            self.ui.manualTestFrame.ui.armMotorBtn.stateChanged.disconnect(self.check_manual_test_conditions)

            self.manualTestThread = threading.Thread(target = self.manual_test_in_execution, daemon=True) # give indication to start the test
            self.manualTestThread.start()
            self.manualTestFinished.connect(self.stop_manual_test)

    # Code for manual test execution
    def manual_test_in_execution(self):
        #Troca de informações com o arduino para inicio de teste
        while self.ui.manualTestFrame.ui.armMotorBtn.isChecked() or (len(self.ui.manualTestFrame.sampleData) + len(self.ui.manualTestFrame.fullData)) > 0:
            #event_loop = QtCore.QEventLoop()
            #self.endArduinoIteraction.connect(event_loop.quit)
            #event_loop.exec_()  # Wait until new data is reveivedthe signal is detected
           
            # Send new data to respective plots
            self.ui.manualTestFrame.update_data(self.current_data)
            self.ui.manualTestFrame.ui.plotFrame.update_data(self.test_data)

            # Read thotle values
            self.throttle = self.ui.manualTestFrame.throttle if self.ui.manualTestFrame.ui.armMotorBtn.isChecked() else 0


        # Emit signal of end of test
        self.manualTestFinished.emit()
        

    # Redefine parameters after test has finished
    def stop_manual_test(self):
        self.manualTestThread._stop()
        self.manualTestThread = None
        self.manualTestFinished.disconnect(self.stop_manual_test)

        self.enable_leftMenu_btns(True) # Disable movement between pages when test is in execution
        self.ui.manualTestFrame.ui.armMotorBtn.stateChanged.connect(self.check_manual_test_conditions)

    def enable_leftMenu_btns(self, state):
        self.ui.setupBtn.setEnabled(state)
        self.ui.manualControlBtn.setEnabled(state)
        self.ui.automaticControlBtn.setEnabled(state)
        self.ui.resultsBtn.setEnabled(state)











    def setup_fundamental_functionalities(self):
        self.timer1 = QtCore.QTimer(MainWindow)       # Create a QTimer instance
        self.timer1.timeout.connect(self.update_data_container)  # Connect timer timeout signal to update function
        self.timer1.start(1000)           # Update every 100 milliseconds (0.1 second)

        
        # Associate buttoms to correspondent functionalities:
        # Left container Btns
        self.ui.setupBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.setupMenu))
        self.ui.manualControlBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.manualTestMenu))
        self.ui.automaticControlBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.automaticControlMenu))
        self.ui.resultsBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.resultsMenu))
        
        #self.ui.settingsBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.settingsMenu))
        #self.ui.exitBtn.clicked.connect(sys.exit)

    def update_data_container(self):
        # Update current_data dictionary with random continuous values
        self.update_data()

        # Update labels with current data values
        self.ui.ThrustValueText.setText(str(self.current_data["Thrust (N)"]))
        self.ui.TorqueValueText.setText(str(self.current_data['Torque (N/m)']))
        self.ui.RpmValueText.setText(str(self.current_data['Rpm']))
        self.ui.MotorTempValueText.setText(str(self.current_data["Temperatura do Motor (ºC)"]))
        self.ui.EscTempValueText.setText(str(self.current_data["Temperatura do Esc (ºC)"]))
        self.ui.VoltageValueText.setText(str(self.current_data["Voltage (V)"]))
        self.ui.CurrentValueText.setText(str(self.current_data["Current (A)"]))
        self.ui.AirspeedValueText.setText(str(self.current_data['Airspeed (m/s)']))
        self.ui.NoiseValueText.setText(str(self.current_data["Acceleration (m/s^2)"]))

        #print(self.ui.manualTestFrame.throttle)
        #print()

  
    def update_data(self): # develop serial communication here
        
        # Assign random continuous values to the current_data dictionary
        self.current_data['Time (s)'] += 1
        self.current_data["Thrust (N)"] = random.choice(trash)
        self.current_data['Torque (N/m)'] = random.choice(trash)
        self.current_data['Rpm'] = random.choice(trash)
        self.current_data["Temperatura do Motor (ºC)"] = random.choice(trash)
        self.current_data["Temperatura do Esc (ºC)"] = random.choice(trash)
        self.current_data["Voltage (V)"] = random.choice(trash)
        self.current_data['Current (A)'] = random.choice(trash)
        self.current_data['Airspeed (m/s)'] = random.choice(trash)
        self.current_data["Acceleration (m/s^2)"] = random.choice(trash)

    

        







#execute app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create a QApplication instance
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowInterface(MainWindow)         # Create an instance of the MainWindowInterface class
    MainWindow.showMaximized()
    sys.exit(app.exec_())                  # Start the application event loop


    #def include_step_test_widget(self):
        # Associate stepTestWidget Class to the stepTestInterface Frame in the main interface
     #   self.ui.stepTestInterface = stepTestWidget(self.ui.stepTestInterface)

        # Define stepTestWidget buttoms functionalities
      #  self.ui.stepTestInterface.ui.ReturnBtn.clicked.connect(lambda : self.ui.mainMenu.setCurrentWidget(self.ui.stepTestMenu))

    
        