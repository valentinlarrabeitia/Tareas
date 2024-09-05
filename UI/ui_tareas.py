# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tareas.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(397, 265)
        self.gridLayout = QGridLayout(VentanaPrincipal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(VentanaPrincipal)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)

        self.agregar_tarea = QPushButton(VentanaPrincipal)
        self.agregar_tarea.setObjectName(u"agregar_tarea")

        self.gridLayout.addWidget(self.agregar_tarea, 2, 0, 1, 3)

        self.titulo_de_app = QLabel(VentanaPrincipal)
        self.titulo_de_app.setObjectName(u"titulo_de_app")
        self.titulo_de_app.setEnabled(True)
        self.titulo_de_app.setLayoutDirection(Qt.LeftToRight)
        self.titulo_de_app.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.titulo_de_app, 0, 1, 1, 1)

        self.listWidget = QListWidget(VentanaPrincipal)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 3, 0, 1, 3)

        self.completar_tarea = QPushButton(VentanaPrincipal)
        self.completar_tarea.setObjectName(u"completar_tarea")

        self.gridLayout.addWidget(self.completar_tarea, 4, 2, 1, 1)

        self.eliminar_tarea = QPushButton(VentanaPrincipal)
        self.eliminar_tarea.setObjectName(u"eliminar_tarea")

        self.gridLayout.addWidget(self.eliminar_tarea, 4, 0, 1, 1)


        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Escriba su tarea...", None))
        self.agregar_tarea.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar Tarea", None))
        self.titulo_de_app.setText(QCoreApplication.translate("VentanaPrincipal", u"ToDo App", None))
        self.completar_tarea.setText(QCoreApplication.translate("VentanaPrincipal", u"Completada", None))
        self.eliminar_tarea.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
    # retranslateUi

