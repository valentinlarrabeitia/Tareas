# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregar_tarea.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGridLayout,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_VentanaAgregarTarea(object):
    def setupUi(self, VentanaAgregarTarea):
        if not VentanaAgregarTarea.objectName():
            VentanaAgregarTarea.setObjectName(u"VentanaAgregarTarea")
        VentanaAgregarTarea.resize(305, 104)
        self.gridLayout = QGridLayout(VentanaAgregarTarea)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(VentanaAgregarTarea)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(VentanaAgregarTarea)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(VentanaAgregarTarea)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)


        self.retranslateUi(VentanaAgregarTarea)

        QMetaObject.connectSlotsByName(VentanaAgregarTarea)
    # setupUi

    def retranslateUi(self, VentanaAgregarTarea):
        VentanaAgregarTarea.setWindowTitle(QCoreApplication.translate("VentanaAgregarTarea", u"Agregar Tarea", None))
        self.label.setText(QCoreApplication.translate("VentanaAgregarTarea", u"Tarea:", None))
    # retranslateUi

