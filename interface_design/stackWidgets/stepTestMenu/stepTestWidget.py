import sys

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Import GUI file
if __name__ == "__main__":
    from stepTestInterface import Ui_Frame 
else:
    from stackWidgets.stepTestMenu.stepTestInterface import Ui_Frame


# Main window class
class stepTestWidget(Ui_Frame):
    def __init__(self, Frame):
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance
        # List (of dictionaries) to store the data from ta table to the execution of the step test
        self.stepTestSequence = list()

        # Define Pattern functionalities:
        self.ui.stepAddNewLineBtn.clicked.connect(self.add_row_to_table)
        self.ui.stepClearTableBtn.clicked.connect(self.delete_table)
        self.ui.stepPreviewTestGraphic.setBackground('w')  # 'w' represents white color
        self.ui.stepPreviewTestGraphic.setMouseEnabled(x=False, y=False)

        # Define initial properties of the widget
        for row in range(self.ui.stepSequenceEditorTable.rowCount()):
            self.step_update_table(row)
        
        self.update_test_sequence()
        self.update_sequence_preview()

        

        # Connect the itemChanged signal from the table to to the custom method
        self.ui.stepSequenceEditorTable.itemChanged.connect(self.update_test_sequence)
        self.ui.stepNumLoopsLEdit.textChanged.connect(self.update_test_sequence)

        

    def step_update_table(self, row):

        """ Create rows in the table according to the format: line edit - checkbox - line edit - push btn """
        # Disable editing for the first row
        if row == 0:  
            item1 = self.ui.stepSequenceEditorTable.item(0, 0)
            item2 = self.ui.stepSequenceEditorTable.item(0, 1)
            item3 = self.ui.stepSequenceEditorTable.item(0, 3)
            
            item1.setFlags(item1.flags() ^ 2)  # Disable the ItemIsEditable flag
            item2.setFlags(item2.flags() ^ 2)
            item3.setFlags(item3.flags() ^ 2)

        # Add checkbox for column 2 (Save Sample)
        checkbox = QtWidgets.QCheckBox()
        checkbox_layout = QtWidgets.QHBoxLayout()
        checkbox_layout.setAlignment(QtCore.Qt.AlignLeft)  # Align the content to the left
        checkbox_layout.addWidget(checkbox)
        
        # Set the layout for checkbox
        checkbox_widget = QtWidgets.QWidget()
        checkbox_widget.setLayout(checkbox_layout)
        self.ui.stepSequenceEditorTable.setCellWidget(row, 2, checkbox_widget)

        # Add push button for column 3 (Delete row)
        if row != 0:
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
                time = float(time.text())
                esc_trotlle = int(esc_trotlle.text())
                self.stepTestSequence.append((time, esc_trotlle))

        num_loops = int(self.ui.stepNumLoopsLEdit.text())

        if num_loops > 1:
            sequence_len = len(self.stepTestSequence)

            for i in range(num_loops-1):
                sequence_end = len(self.stepTestSequence)
                for j in range(1, sequence_len):
                    
                    self.stepTestSequence.append((self.stepTestSequence[j][0] + self.stepTestSequence[sequence_end-1][0], self.stepTestSequence[j][1]))

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
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = stepTestWidget(Frame)
    Frame.show()
    sys.exit(app.exec_())




