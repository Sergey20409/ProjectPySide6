# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b_systeminfo_widget_formdhJHnF.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(212, 107)
        Form.setMaximumSize(QSize(16777215, 107))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label)

        self.delayLineEdit = QLineEdit(Form)
        self.delayLineEdit.setObjectName(u"delayLineEdit")
        self.delayLineEdit.setMinimumSize(QSize(80, 0))
        self.delayLineEdit.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.delayLineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.CpuLcdNumber = QLCDNumber(Form)
        self.CpuLcdNumber.setObjectName(u"CpuLcdNumber")
        self.CpuLcdNumber.setMinimumSize(QSize(79, 25))
        self.CpuLcdNumber.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.CpuLcdNumber)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.label_3)

        self.RamLcdNumber = QLCDNumber(Form)
        self.RamLcdNumber.setObjectName(u"RamLcdNumber")
        self.RamLcdNumber.setMinimumSize(QSize(79, 25))
        self.RamLcdNumber.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.RamLcdNumber)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
    # retranslateUi

