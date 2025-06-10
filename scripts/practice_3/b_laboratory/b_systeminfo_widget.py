"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from ui.b_systeminfo_widget_form import Ui_Form
from PySide6 import QtWidgets
from a_threads import SystemInfo
import re

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__initSignals()

    def __initSignals(self):
        self.thread.start()
        self.thread.systemInfoReceived.connect(self.__reportProgress)
        self.ui.delayLineEdit.textChanged.connect(self.__onsetdelay)

    def __onsetdelay(self):
        text = self.ui.delayLineEdit.text()
        if bool(re.fullmatch(r'^0*\.?0*',str(text))):
            pass
        else:
            try:
                self.thread.delay = float(text)
            except:
                pass

    def __setDelay(self):
        pass

    def __initThreads(self):
        self.thread = SystemInfo()

    def __reportProgress(self, data):
        self.ui.CpuLcdNumber.display(data[0])
        self.ui.RamLcdNumber.display(data[1][2])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()