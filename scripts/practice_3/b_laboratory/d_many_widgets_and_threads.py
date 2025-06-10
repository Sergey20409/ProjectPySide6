"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy, QSpacerItem


import b_systeminfo_widget
import c_weatherapi_widget

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.resize(600, 600)
        self.systeminfo_widget = b_systeminfo_widget.Window()
        self.weatherapi_widget = c_weatherapi_widget.Window()
        # self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        widget_layout = QtWidgets.QVBoxLayout()
        widget_layout.addWidget(self.systeminfo_widget)
        # widget_layout.addItem(self.verticalSpacer)
        widget_layout.addWidget(self.weatherapi_widget)

        self.setLayout(widget_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()