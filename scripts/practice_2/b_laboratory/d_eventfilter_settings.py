"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initUi()
        self.initSignals()

        self.__loadSettings()

    def closeEvent(self, event):

        self.__saveSettings()

        return super().closeEvent(event)

    def __loadSettings(self):
        settings = QtCore.QSettings("setSettings")
        self.comboBox.setCurrentText(settings.value("comboBox", ""))
        self.lcdNumber.display(settings.value("lcdNumber", ""))

    def __saveSettings(self):
        settings = QtCore.QSettings("setSettings")
        settings.setValue("comboBox", self.comboBox.currentText())
        settings.setValue("lcdNumber", self.lcdNumber.value())

    def initUi(self):
        dialog_boxes = [
            "Oct",
            "Hex",
            "Bin",
            "Dec"]

        self.comboBox.addItems(dialog_boxes)




    def keyPressEvent(self, event, /):
        if event.text() == '+':
            self.dial.setValue(self.dial.value()+1)
        elif event.text() == '-':
            self.dial.setValue(self.dial.value()-1)
        print(f'Значение dial - {self.dial.value()}')

    def initSignals(self):
       self.horizontalSlider.valueChanged.connect(self.dial.setValue)
       self.dial.valueChanged.connect(self.horizontalSlider.setValue)
       self.dial.valueChanged.connect(self.lcdNumber.display)
       self.comboBox.currentTextChanged.connect(self.setLcdMode)

    def setLcdMode(self):
        if self.comboBox.currentText() == "Oct":
            self.lcdNumber.setOctMode()
        elif self.comboBox.currentText() == "Hex":
            self.lcdNumber.setHexMode()
        elif self.comboBox.currentText() == "Bin":
            self.lcdNumber.setBinMode()
        elif self.comboBox.currentText() == "Dec":
            self.lcdNumber.setDecMode()
        self.lcdNumber.display(self.lcdNumber.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
