import sys
import csv

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI file
if __name__ == "__main__":
    from stepTestInterface import Ui_Frame 
else:
    from stackWidgets.stepTestMenu.stepTestInterface import Ui_Frame


# Main window class
class stepTestWidget(QtWidgets.QWidget):
    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance

        self.step_sequence_editor_menu_properties()
        #self.ui.typeOfTestSlider.valueChanged.connect(self.type_of_automatic_test)
        
        # List (of dictionaries) to store the data from ta table to the execution of the step test
        self.stepTestSequence = list()

        
        self.ui.PreviewTestGraphic.setBackground('w')  # 'w' represents white color
        self.ui.PreviewTestGraphic.setMouseEnabled(x=False, y=False)

        
        
        self.update_test_sequence()
        self.update_sequence_preview()

    def type_of_automatic_test(self):
        if self.ui.typeOfTestSlider.value() == 0:
            self.test = 'ramp'
            self.ui.typeOfTestSlider.setValue(1)
        else:
            self.test = 'step'
            self.ui.typeOfTestSlider.setValue(0)

        print(self.test)
        return

    def step_sequence_editor_menu_properties(self):

        # Define buttoms functionalities:
        self.ui.AddNewLineBtn.clicked.connect(self.add_row_to_table)
        self.ui.ClearTableBtn.clicked.connect(self.delete_table)
        self.ui.ImportCSVBtn.clicked.connect(self.import_csv_file)

        # Define initial properties of the widget
        for row in range(self.ui.SequenceEditorTable.rowCount()):
            self.step_update_table(row)

        # Connect the itemChanged signal from the table to to the custom method
        self.ui.SequenceEditorTable.itemChanged.connect(self.update_test_sequence)
        self.ui.NumLoopsLEdit.textChanged.connect(self.update_test_sequence)

        
    def add_row_to_table(self):
        """ Add row to the table """
        current_row_count = self.ui.SequenceEditorTable.rowCount() # Compute number of rown in the table
        self.ui.SequenceEditorTable.insertRow(current_row_count-1)   # Insert new row to the end of the table
        self.step_update_table(self.ui.SequenceEditorTable.rowCount()-2)


    def delete_table(self):
        """ Delete the table, the first and last row showld keep unchanged"""
        for row in range(1, self.ui.SequenceEditorTable.rowCount() - 1):
            self.delete_row(1) # Here 1 represents the second row of the table.
                               # The loop will keep until only the forst and last row are present
        self.add_row_to_table()

    def delete_row(self, row):
        
        """Delete the selected row from the table"""
        self.ui.SequenceEditorTable.removeRow(row)
        self.update_test_sequence()

    def step_update_table(self, row):

        """ Create rows in the table according to the format: line edit - checkbox - line edit - push btn """
        # Disable editing for the first and last row
        if row == 0 or row == self.ui.SequenceEditorTable.rowCount()-1:  
            item1 = self.ui.SequenceEditorTable.item(row, 0)
            item2 = self.ui.SequenceEditorTable.item(row, 1)
            item3 = self.ui.SequenceEditorTable.item(row, 3)
            
            item1.setFlags(item1.flags() ^ 2)  # Disable the ItemIsEditable flag
            item2.setFlags(item2.flags() ^ 2)
            item3.setFlags(item3.flags() ^ 2)

            return
        
        # Add checkbox for column 2 (Save Sample)
        checkbox = QtWidgets.QCheckBox()
        checkbox_layout = QtWidgets.QHBoxLayout()
        checkbox_layout.setAlignment(QtCore.Qt.AlignLeft)  # Align the content to the left
        checkbox_layout.addWidget(checkbox)
        
        # Set the layout for checkbox
        checkbox_widget = QtWidgets.QWidget()
        checkbox_widget.setLayout(checkbox_layout)
        self.ui.SequenceEditorTable.setCellWidget(row, 2, checkbox_widget)

        # Add push button for column 3 (Delete row)
        push_button = QtWidgets.QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/b_icons/icons-black/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)            
        push_button.setIcon(icon)
        push_button.clicked.connect(lambda _: self.delete_row(self.ui.SequenceEditorTable.indexAt(push_button.mapTo(self.ui.SequenceEditorTable, push_button.pos())).row()-1))
        
        # Create a horizontal layout for the button
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignRight)  # Align the content to the left
        button_layout.addWidget(push_button)
        

        # Set the layout as the button's layout
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(button_layout)
        button_widget.setStyleSheet("border: none; background-color: transparent;")  
        self.ui.SequenceEditorTable.setCellWidget(row, 3, button_widget)    

    def import_csv_file(self):
        """ Look for CSV files to import for test Sequeneces"""
        options = QtWidgets.QFileDialog.Options()
        
        while True:
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        
            # Find if a file was selected. If not, return
            if not file_path:
                return
        
            # determine if the selected file is a CSV file. If not, raise error that it is not possible to import the file
            if not file_path.lower().endswith('.csv'):
                # Show a QMessageBox indicating that the selected file is not a valid CSV file
                QtWidgets.QMessageBox.critical(self, "Error", "Selected file is not a valid CSV file. Please select a valid CSV file.")
            else: 
                break # if a CSV file was selected, end the loop and start processing the file

        # Proceed with reading and processing the CSV file
        with open(file_path, 'r',encoding='utf-8-sig') as csvfile:
            
            csv_reader = csv.reader(csvfile)
            testSequence = []
            for row in csv_reader:
                if len(row) not in [2, 3]:  # Ensure at least two columns are present in each row, and not more that 3
                    QtWidgets.QMessageBox.critical(self, "Error", f"Invalid file format.")
                    return
                
                try: # try to convert the values of the file
                    time = float(row[0])
                    esc_trottle = int(row[1])
                    take_sample = 'x' if len(row) > 2 and row[2] == 'x' else ''  # If third column exists, use its value, else set to ''

                except ValueError:
                    QtWidgets.QMessageBox.critical(self, "Error", f"Invalid row detected: {row}")
                    return
                
                # If the values are correct, append it to the list
                testSequence.append((time, esc_trottle, take_sample))

        # if all the file is well formated, make StepTestSequence = sequence
             
        print(testSequence)

        # Copy the file to the table
        self.delete_table()
        self.delete_row(1)

        print(testSequence)
        for row in testSequence:
            print(row)
            self.add_row_to_table()

            time = QtWidgets.QTableWidgetItem(str(row[0]))
            esc_trottle = QtWidgets.QTableWidgetItem(str(row[1]))
            
            self.ui.SequenceEditorTable.setItem(self.ui.SequenceEditorTable.rowCount() -2, 0, time)
            self.ui.SequenceEditorTable.setItem(self.ui.SequenceEditorTable.rowCount() -2, 1, esc_trottle)

            # Get the widget in the third column of the current row
            cell_widget = self.ui.SequenceEditorTable.cellWidget(self.ui.SequenceEditorTable.rowCount() -2, 2)
            # Access the checkbox within the widget
            checkbox = cell_widget.findChild(QtWidgets.QCheckBox)
            # Update the check state based on the value in testSequence
            if row[2] == 'x':
                checkbox.setCheckState(QtCore.Qt.Checked)






    def update_test_sequence(self):
        """Update Sequence Preview based on the table data"""

        if self.check_sequence(): # if the sequence if valid compute the final 

            num_loops = int(self.ui.NumLoopsLEdit.text())

            if num_loops > 1:
                sequence_len = len(self.stepTestSequence)

                for i in range(num_loops-1):
                    sequence_end = len(self.stepTestSequence)
                    for j in range(1, sequence_len):
                        
                        self.stepTestSequence.append((self.stepTestSequence[j][0] + self.stepTestSequence[sequence_end-1][0], self.stepTestSequence[j][1]))

        #print(self.stepTestSequence)
        
        self.update_sequence_preview()

    def check_sequence(self):
        self.stepTestSequence.clear()

        for row in range(1, self.ui.SequenceEditorTable.rowCount() - 2):
            time = self.ui.SequenceEditorTable.item(row, 0)
            esc_trotlle = self.ui.SequenceEditorTable.item(row, 1)

            # check if all cells are not null
            if time == None or esc_trotlle == None:
                self.stepTestSequence.clear()
                return False

            # Check if all cells have appropriate values
            try:
                time = float(time.text())
                esc_trotlle = int(esc_trotlle.text())
            except ValueError:
                self.stepTestSequence.clear()
                return False
            
            # check if the esc trotlle values are within the limits:
            if 1000 > esc_trotlle or 2000 < esc_trotlle:
                self.stepTestSequence.clear()
                return False
            else:
                self.stepTestSequence.append((time, esc_trotlle))

        return True
        


        

        
                
            


    def update_sequence_preview(self):
        x_data = list()
        y_data = list()
        
        self.ui.PreviewTestGraphic.clear()  # Clear previous plot data
    
        for time in range(len(self.stepTestSequence) - 1):
            x_start, x_end = self.stepTestSequence[time][0], self.stepTestSequence[time + 1][0]
            y_value = self.stepTestSequence[time][1]  # Y-value is the throttle value from the list
            
            # Append data points to the lists
            x_data.extend([x_start, x_end])
            y_data.extend([y_value, y_value])

            # Plot horizontal line between x_start and x_end with y_value
            self.ui.PreviewTestGraphic.plot(x_data, y_data, pen=pg.mkPen(color=(255, 165, 0), width=2))




#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = stepTestWidget(Frame)
    Frame.show()
    sys.exit(app.exec_())




