"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
from PySide6 import QtWidgets, QtCore

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.process = None

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButton = QtWidgets.QPushButton("Запуск процесса")

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.executeOtherProcess)

    def executeOtherProcess(self) -> None:
        """
        Запуск выполнения другого процесса

        :return: None
        """

        if self.process is None:
            self.plainTextEdit.appendPlainText("Запуск другого процесса")
            self.process = QtCore.QProcess()
            self.process.start("python", ['a_threads.py'])
            self.process.finished.connect(self.processFinished)

    def processFinished(self) -> None:
        """
        Действие при завершении другого процесса

        :return: None
        """

        self.plainTextEdit.appendPlainText("Другой процесс завершен")
        self.process = None


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

