# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(501, 347)
        self.layoutWidget = QWidget(widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(23, 10, 441, 300))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 3)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.dateTimeEdit_1 = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_1.setObjectName(u"dateTimeEdit_1")

        self.gridLayout.addWidget(self.dateTimeEdit_1, 3, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.gridLayout.addWidget(self.dateTimeEdit_2, 4, 2, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("widget", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("widget", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430 2", None))

        self.label.setText(QCoreApplication.translate("widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.textEdit.setHtml(QCoreApplication.translate("widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0443\u0441\u0442\u043e \u043f\u043e\u043a\u0430</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

