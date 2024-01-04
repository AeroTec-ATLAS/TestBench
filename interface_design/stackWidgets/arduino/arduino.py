
import serial
import serial.tools.list_ports

import struct
import copy
import time

from PyQt5.QtCore import pyqtSignal

class Arduino():

    dataReceived = pyqtSignal()
    connectionLost = pyqtSignal()


    def _init_(self, device = None, boudrate = 115200, timeount = 1): 
        self.device = device
        self.boudrate = boudrate
        self.conectionState = False
        self.timeount = timeount
        self.ser = None

    def establish_connection(self, device): 
        try:
            self.ser=serial.Serial(device,self.boudrate,timeout=1)
            self.device = device
            self.conectionState = 1
            return 1
            
        except serial.SerialException:
            self.device = None
            self.connState = 0
            return 0
        

    def arduinoDataTransmission(self):        
        """
        Controls the flux of data between arduino and computer
        Protocol used:
            phase 1: computer sends two flags to the arduino
                        first indicates if motor is armed or not
                        second indicates the PWM signal
            
            phase 2: computer receives the data of the sensors
                     sent by the arduino
        """
        receive_PWM = 0
        receive_motorArmedFlag = 0

        while True: 

            # prepare data to send to the arduino
            motorArmed = copy,copy(receive_motorArmedFlag)
            pwmSignal  = copy.copy(receive_PWM)  

            message = struct.pack('!ii', motorArmed, pwmSignal) 
            #message = f"{motorArmed},{pwmSignal}\n"

            # send data to arduino
            self.ser.write(message)
            self.ser.write(message.encode('utf-8'))

            # wait for data sent by the arduino
            while self.ser.in_waiting == 0:
                time.sleep(0.1)

            # read data sent by the arduino and decode it
            #response = self.ser.readline().decode('utf-8').strip()
            received_data = self.ser.read(10)
            unpacked_values = struct.unpack('!' + 'f' * 10, received_data)

            self.testData = {
                'Time (s)': unpacked_values[0],
                'Airspeed (m/s)': unpacked_values[1],
                'Voltage (V)': unpacked_values[2],
                'Current (A)': unpacked_values[3],
                'Torque (N/m)': unpacked_values[4],
                'Rpm': unpacked_values[5],
                'Acceleration (m/s^2)': unpacked_values[6],
                'Temperatura do Esc (ºC)': unpacked_values[7],
                'Temperatura do Motor (ºC)': unpacked_values[8],
                'Thrust (N)': unpacked_values[9], 
            }

            self.dataReceived.emit()         




