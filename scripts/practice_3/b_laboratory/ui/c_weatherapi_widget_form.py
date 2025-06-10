# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_weatherapi_widget_formHJvVsc.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 300)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.LatitudeLineEdit = QLineEdit(Form)
        self.LatitudeLineEdit.setObjectName(u"LatitudeLineEdit")
        self.LatitudeLineEdit.setMinimumSize(QSize(80, 0))
        self.LatitudeLineEdit.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.LatitudeLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.LongitudeLineEdit = QLineEdit(Form)
        self.LongitudeLineEdit.setObjectName(u"LongitudeLineEdit")
        self.LongitudeLineEdit.setMinimumSize(QSize(80, 0))
        self.LongitudeLineEdit.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.LongitudeLineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.TimeDelayLineEdit = QLineEdit(Form)
        self.TimeDelayLineEdit.setObjectName(u"TimeDelayLineEdit")
        self.TimeDelayLineEdit.setMinimumSize(QSize(80, 0))
        self.TimeDelayLineEdit.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.TimeDelayLineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WeatherPlainTextEdit = QPlainTextEdit(self.groupBox)
        self.WeatherPlainTextEdit.setObjectName(u"WeatherPlainTextEdit")

        self.verticalLayout_2.addWidget(self.WeatherPlainTextEdit)


        self.verticalLayout.addWidget(self.groupBox)

        self.WeatherPushButton = QPushButton(Form)
        self.WeatherPushButton.setObjectName(u"WeatherPushButton")

        self.verticalLayout.addWidget(self.WeatherPushButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u043e\u0433\u043e\u0434\u0430:", None))
        self.WeatherPushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
    # retranslateUi

