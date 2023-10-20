import serial
import serial.tools.list_ports
import csv

test_parameters = ["thrust", "torque", "rpm speed", "aceleracao", "motor temperature"]

connected_ports = list(serial.tools.list_ports.comports())
n_samples = 1000

def main():

    if not connected_ports:
        raise IOError("No Arduino found")    

    arduino = serial.Serial(connected_ports[0], baudrate=9600, timeout=1)
    arduino.open() # Opens the serial port for communication

    while(arduino.read() != 1) # wait for setup of arduino    
    
    line = 0
    with open("results.csv", 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=test_parameters)
        
        while(arduino.is_open() and line < n_samples)
            all_data = dict()

            for i in range(len(test_parameters)):
                # Read data from Arduino as integer
                try:
                    data = int(arduino.readline().strip())
                except ValueError:
                    print("Invalid data received. Skipping this sample.")
                    continue

                all_data[test_parameters[i]] = data

            print(all_data)
            writer.writerow(all_data)
            line += 1
    
    arduino.close()




