from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        centralWidget = QWidget(self)
        layout = QVBoxLayout(centralWidget)
        
        self.tableWidget = QTableWidget(self)
        layout.addWidget(self.tableWidget)
        
        self.setCentralWidget(centralWidget)
        
        # Add rows and columns to the table
        self.tableWidget.setRowCount(3)  # Number of rows
        self.tableWidget.setColumnCount(3)  # Number of columns

        # Populate the table with data
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem("Row {} Col {}".format(row, col))
                self.tableWidget.setItem(row, col, item)

        # Disable editing for the first row
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(0, col)
            item.setFlags(item.flags() ^ 2)  # Disable the ItemIsEditable flag
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
