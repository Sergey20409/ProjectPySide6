"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

import time
from itertools import count

from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initSignals()


    def initSignals(self):
        self.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)
        self.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)
        self.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)
        self.pushButtonCenter.clicked.connect(self.onPushButtonCenterClicked)
        self.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)
        self.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)


    def onPushButtonMoveCoordsClicked(self):
        self.setGeometry(int(self.spinBoxX.text()), int(self.spinBoxY.text())+30, int(self.width()), int(self.height()))

    def onPushButtonLTClicked(self):
        self.setGeometry(0, 30, int(self.width()), int(self.height()))

    def onPushButtonRTClicked(self):
        self.setGeometry(QtGui.QGuiApplication.primaryScreen().availableGeometry().size().width()-self.width(), 30, int(self.width()), int(self.height()))

    def onPushButtonCenterClicked(self):
        self.setGeometry(QtGui.QGuiApplication.primaryScreen().availableGeometry().size().width()/2-self.width()/2,
                         QtGui.QGuiApplication.primaryScreen().availableGeometry().size().height()/2-self.height()/2+15, int(self.width()), int(self.height()))

    def onPushButtonLBClicked(self):
        self.setGeometry(0, QtGui.QGuiApplication.primaryScreen().availableGeometry().size().height()-self.height(), int(self.width()), int(self.height()))

    def onPushButtonRBClicked(self):
        self.setGeometry(QtGui.QGuiApplication.primaryScreen().availableGeometry().size().width()-self.width(),
                         QtGui.QGuiApplication.primaryScreen().availableGeometry().size().height()-self.height(), int(self.width()), int(self.height()))

    def onPushButtonGetDataClicked(self):
        self.plainTextEdit.setPlainText(f'{time.strftime("%H:%M:%S")}\n'
                                        f'Кол-во экранов - {QtGui.QGuiApplication.screens().__len__()}\n'
                                        f'Текущий основной монитор - {QtGui.QGuiApplication.primaryScreen().name()}\n'
                                        f'Разрешение экрана - {QtGui.QGuiApplication.primaryScreen().geometry().size().toTuple()}\n'
                                        f'Окно находится на экране - {self.screen().name()}\n'
                                        f'Размеры окна - {self.size().toTuple()}\n'
                                        f'Минимальные размеры окна - {self.minimumSize().toTuple()}\n'
                                        f'Текущее положение (координаты) окна - {self.pos().toTuple()}\n'
                                        f'Координаты центра приложения - {self.mapToGlobal(self.geometry().center()).toTuple()}\n'
                                        f'Состояния окна - {self.windowState()}\n')

    def moveEvent(self, event, /):
        print(time.strftime("%H:%M:%S"), f'Старая позиция - {event.oldPos().toTuple()}, Новая позиция - {event.pos().toTuple()}')

        return super().moveEvent(event)

    def resizeEvent(self, event, /):
        print(time.strftime("%H:%M:%S"), f'Новый размер - {event.size().toTuple()}')

        return super().resizeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
