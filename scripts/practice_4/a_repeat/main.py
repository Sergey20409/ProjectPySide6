from note import Ui_widget
from PySide6 import QtWidgets, QtCore

class Window(QtWidgets.QWidget,Ui_widget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initSignals()


    def initSignals(self):
        self.pushButton.clicked.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self):
        self.textEdit.setText("1")





if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()