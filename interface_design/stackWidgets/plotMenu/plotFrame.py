import sys
import random
import numpy as np

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI file
if __name__ == "__main__":
    from plotInterface  import Ui_Frame
else:
    from stackWidgets.plotMenu.plotInterface import Ui_Frame


# Main window class
class plotFrame(QtWidgets.QWidget):

    dataUpdated = QtCore.pyqtSignal()
    cutoffsUpdated = QtCore.pyqtSignal()

    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance

        # Dictionary of the graph plots:
        self.plots = {
            'Airspeed (m/s)': self.ui.airspeedPlot,
            'Voltage (V)': self.ui.voltagePlot,
            'Current (A)': self.ui.currentPlot,
            'Torque (N/m)': self.ui.torquePlot,
            'Rpm': self.ui.rpmPlot,
            'Acceleration (m/s^2)': self.ui.acelerationPlot,
            'Temperatura do Esc (ºC)': self.ui.escTempPlot,
            'Temperatura do Motor (ºC)': self.ui.motorTempPlot,
            'Thrust (N)': self.ui.thrustPlot
        }

        self.plotData = {
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

        self.systemcutoffs = {
            ("Tension (V)", "Cutoff Max"): 90,
            ("Current (A)", "Cutoff Max"): 155,
            ("Thrust (Kg)", "Cutoff Max"): 10,
            ("Torque (Kg)", "Cutoff Max"): 90,
            ("RPM", "Cutoff Max"): 155
            #("Vibrations", "Cutoff Max"): 10 
        }

        for key in self.plotData.keys():
            # For simplicity, generating random data as an example
            if key == 'Time (s)':
                self.plotData[key] = np.linspace(1, 50, 50)
            else:
                self.plotData[key] = [random.uniform(0, 10) for _ in range(50)]

        # Initialize the data_line attribute as an empty dictionary
        self.data_line = {}

        # Place 


        self.lifeSpan = self.ui.lifeSpanSpinBox.value()

        # Connect signals of slider and Spinbox
        self.ui.lifeSpanSpinBox.valueChanged.connect(lambda: self.update_life_span('spinBox'))
        self.ui.lifeSpanSlider.valueChanged.connect(lambda: self.update_life_span('slider'))
        
        # Define first properties of the plots
        self.custumize_plots()

        # include cutoff lines in the plots
        self.define_system_cutoffs()

        # Associate dataUpdated signal to update plot data
        self.dataUpdated.connect(self.update_plot_data)

    # Change lifeSpan
    def update_life_span(self, font):

        if font == 'spin_box':
            self.lifeSpan = self.ui.lifeSpanSpinBox.value()
            self.ui.lifeSpanSlider.setValue(self.lifeSpan)
        else:
            self.lifeSpan = self.ui.lifeSpanSlider.value()
            self.ui.lifeSpanSpinBox.setValue(self.lifeSpan)

        self.dataUpdated.emit()
        
    def custumize_plots(self):

        # Define basic properties for each plot
        for title, plot in self.plots.items():
            
            plot.setMouseEnabled(x=False, y=False) # Prevent user slicing of the plot
            plot.setBackground('w')                # Set gackground to white
            plot.showGrid(x=True, y=True)          # activate grid
            pen = pg.mkPen(color=(255, 165, 0), width=2) # Define pen caracteristics
            plot.setTitle(title, color="k", size="15pt") # Define lot Title
            
            styles = {'color':'r', 'font-size':'20px'}
            plot.setLabel('bottom', 'time (s)', **styles) # Add plot label
            
            # Define data
            self.data_line[title] =  plot.plot(self.plotData['Time (s)'], self.plotData[title], pen=pen)

    # Update existing plot         
    def update_plot_data(self):
            for title in self.data_line.keys():
                self.data_line[title].setData(self.plotData['Time (s)'][-self.lifeSpan-1:], self.plotData[title][-self.lifeSpan-1:])

    def update_data(self, full_Data):
        if not self.ui.pauseBtn.isChecked():
            self.plotData = {key: value[-90:] for key, value in full_Data.items()}
        
    # Create a horizontal lines for system cuoffs
    def define_system_cutoffs(self):
        self.currentMax = pg.InfiniteLine(pos=self.systemcutoffs[("Tension (V)", "Cutoff Max")], angle=0, pen=pg.mkPen(color='k', style=pg.QtCore.Qt.DashLine))
        self.voltageMax = pg.InfiniteLine(pos=self.systemcutoffs[("Current (A)", "Cutoff Max")], angle=0, pen=pg.mkPen(color='k', style=pg.QtCore.Qt.DashLine))
        self.thrustMax = pg.InfiniteLine(pos=self.systemcutoffs[("Thrust (Kg)", "Cutoff Max")], angle=0, pen=pg.mkPen(color='k', style=pg.QtCore.Qt.DashLine))
        self.torqueMax = pg.InfiniteLine(pos=self.systemcutoffs[("Torque (Kg)", "Cutoff Max")], angle=0, pen=pg.mkPen(color='k', style=pg.QtCore.Qt.DashLine))
        self.rpmMax = pg.InfiniteLine(pos=self.systemcutoffs[("RPM", "Cutoff Max")], angle=0, pen=pg.mkPen(color='k', style=pg.QtCore.Qt.DashLine))

        self.plots['Voltage (V)'].addItem(self.voltageMax)
        self.plots['Current (A)'].addItem(self.currentMax)
        self.plots['Rpm'].addItem(self.rpmMax)
        self.plots['Voltage (V)'].addItem(self.thrustMax)
        self.plots['Torque (N/m)'].addItem(self.torqueMax)

        self.cutoffsUpdated.connect(self.update_system_cutoffs)

    # Update cuoffs limits
    def update_system_cutoffs(self):
        self.currentMax.setPos(self.systemcutoffs[("Current (A)", "Cutoff Max")])
        self.voltageMax.setPos(self.systemcutoffs[("Tension (V)", "Cutoff Max")])
        self.thrustMax.setPos(self.systemcutoffs[("Thrust (Kg)", "Cutoff Max")])
        self.torqueMax.setPos(self.systemcutoffs[("Torque (Kg)", "Cutoff Max")])
        self.rpmMax.setPos(self.systemcutoffs("RPM", "Cutoff Max"))


#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = plotFrame(Frame)
    Frame.show()
    sys.exit(app.exec_())




