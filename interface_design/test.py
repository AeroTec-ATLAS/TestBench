from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
from PyQt5.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a combo box
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])

        self.combo_box.highlighted.connect(self.on_combobox_activated)

        # Create a label to display the selected item
        self.label = QLabel(self)

        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setWindowTitle('Combo Box Example')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Capture the moment when the left mouse button is pressed
            print("Mouse click on QComboBox")
            # You can perform additional actions here if needed

        # Call the base class implementation
        super().mousePressEvent(event)

    def on_combobox_activated(self, index):
        selected_item = self.combo_box.itemText(index)
        self.label.setText(f'Selected item: {selected_item}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
