from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Button to open file dialog
        self.openFileButton = QPushButton('Open File', self)
        self.openFileButton.clicked.connect(self.showFileDialog)
        layout.addWidget(self.openFileButton)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle('File Dialog Example')
        self.show()

    def showFileDialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print("Selected file:", file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
