import sys

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
    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance

        # Dictionary of the graph plots:
        self.plots = {
            'airspeed': self.ui.airspeedPlot,
            'voltage': self.ui.voltagePlot,
            'current': self.ui.currentPlot,
            'torque': self.ui.torquePlot,
            'rpm': self.ui.rpmPlot,
            'acceleration': self.ui.acelerationPlot,
            'escTemp': self.ui.escTempPlot,
            'motorTemp': self.ui.motorTempPlot,
            'thrust': self.ui.thrustPlot
        }

        self.lifeSpan = self.ui.lifeSpanSpinBox.value()

        # Connect signals of slider and Spinbox
        self.ui.lifeSpanSpinBox.valueChanged.connect(lambda: self.update_life_span('spinBox'))
        self.ui.lifeSpanSlider.valueChanged.connect(lambda: self.update_life_span('slider'))
        
        # Define first properties of the plots
        self.custumize_plots()


    def update_life_span(self, font):

        if font == 'spin_box':
            self.lifeSpan = self.ui.lifeSpanSpinBox.value()
            self.ui.lifeSpanSlider.setValue(self.lifeSpan)
        else:
            self.lifeSpan = self.ui.lifeSpanSlider.value()
            self.ui.lifeSpanSpinBox.setValue(self.lifeSpan)

       

        
    def custumize_plots(self):

        for title, plot in self.plots.items():
            x = [1, 2, 3, 4, 5]
            y = [2, 4, 1, 7, 3]
            plot.setMouseEnabled(x=False, y=False)
            plot.setBackground('w')  # change background
            plot.showGrid(x=True, y=True)
            pen = pg.mkPen(color=(255, 165, 0), width=2) # change pen
            plot.setTitle(title, color="k", size="15pt")
            
            #change labels of axis
            #styles = {'color':'r', 'font-size':'20px'}
            #self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
            #self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
            
            # plot data: x, y values and markers
            #self.graphWidget.plot(hour, temperature, pen=pen, symbol='+', symbolSize=20, symbolBrush=('b'))
            #self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

            
            #self.timer = QtCore.QTimer()
            #self.timer.setInterval(50)
            #self.timer.timeout.connect(self.update_plot_data)
            #self.timer.start()


            plot.plot(x, y, pen=pen)
    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0,100))  # Add a new random value.
        

        self.data_line.setData(self.x, self.y)  # Update the data.

    def update_plots(self):
        if not self.ui.pauseBtn.isChecked():
            
        

   

        
#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = plotFrame(Frame)
    Frame.show()
    sys.exit(app.exec_())




