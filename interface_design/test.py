from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        # Create a QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(3, 3)
        layout.addWidget(self.tableWidget)

        # Connect the itemChanged signal to the custom method
        self.tableWidget.itemChanged.connect(self.handleItemChanged)

    def handleItemChanged(self, item):
        # Handle changes in the table
        row = item.row()
        column = item.column()
        new_value = item.text()
        print(f'Item at row {row}, column {column} changed to: {new_value}')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

