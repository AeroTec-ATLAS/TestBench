import sys

#import Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

# Import GUI file
if __name__ == "__main__":
    from customizationInterface  import Ui_Frame
else:
    from stackWidgets.plotMenu.customizationInterface import Ui_Frame

    


# Main window class
class customizationFrame(QtWidgets.QWidget):
    def __init__(self, Frame):
        super().__init__()
        self.ui = Ui_Frame()  # Create an instance of the UI class
        self.ui.setupUi(Frame)  # Set up the UI elements on this QWidget instance
        self.setAcceptDrops(True)

        self.ui.thrustFrame =  DragFrame(self.ui.thrustFrame, "  Thrust", "ThrustBtn", "ThrustCheck")
        self.ui.currentFrame = DragFrame(self.ui.currentFrame, "  Current", "CurrentBtn", "CurrentChecked" )
    
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        widget = e.source()

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width() // 2:
                # We didn't drag past this widget.
                # insert to the left of it.
                self.blayout.insertWidget(n-1, widget)
                break

        e.accept()


class DragWidget(QWidget):
    """
    Create Tree Columns to organize 
    """

    orderChanged = pyqtSignal(list)

    def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
        super().__init__()
        self.setAcceptDrops(True)

        # Store the orientation for drag checks later.
        self.orientation = orientation

        if self.orientation == Qt.Orientation.Vertical:
            self.blayout = QVBoxLayout()
        else:
            self.blayout = QHBoxLayout()

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        widget = e.source()

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if self.orientation == Qt.Orientation.Vertical:
                # Drag drop vertically.
                drop_here = pos.y() < w.y() + w.size().height() // 2
            else:
                # Drag drop horizontally.
                drop_here = pos.x() < w.x() + w.size().width() // 2

            if drop_here:
                # We didn't drag past this widget.
                # insert to the left of it.
                self.blayout.insertWidget(n-1, widget)
                self.orderChanged.emit(self.get_item_data())
                break

        e.accept()

    def add_item(self, item):
        self.blayout.addWidget(item)

    def get_item_data(self):
        data = []
        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            data.append(w.data)
        return data


class DragFrame(QtWidgets.QFrame):

    def __init__(self, frame,clickedBtnText, clickedBtnName, checkBtnName):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/b_icons/icons-black/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clickBtn = QtWidgets.QPushButton(frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clickBtn.setFont(font)
        self.clickBtn.setIcon(icon)
        self.clickBtn.setText(clickedBtnText)
        self.clickBtn.setObjectName(clickedBtnName)
        self.horizontalLayout.addWidget(self.clickBtn)
        self.checkBtn = QtWidgets.QCheckBox(frame)
        self.checkBtn.setText("")
        self.checkBtn.setObjectName(checkBtnName)
        self.horizontalLayout.addWidget(self.checkBtn)
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime = QtCore.QMimeData()
            drag.setMimeData(mime)

            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)

        
#execute app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame =QtWidgets.QFrame()
    ui = customizationFrame(Frame)
    Frame.show()
    sys.exit(app.exec_())




