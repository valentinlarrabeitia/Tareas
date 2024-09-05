from PySide6 import QtWidgets
from UI.ui_tareas import Ui_VentanaPrincipal
from controlador_tareas import AdministradorTareas


class VentanaTareas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_VentanaPrincipal()
        self.ventana.setupUi(self)
        self.ventana.agregar_tarea.clicked.connect(self.agregar_tarea)
        self.ventana.eliminar_tarea.clicked.connect(self.eliminar_tarea)
        self.ventana.completar_tarea.clicked.connect(self.completar_tarea)

    def agregar_tarea(self):
        nueva_tarea = self.ventana.lineEdit.text()
        self.ventana.listWidget.addItem(nueva_tarea)
        self.ventana.lineEdit.clear()

    def eliminar_tarea(self):
        item_seleccionado = self.ventana.listWidget.currentRow()
        self.ventana.listWidget.takeItem(item_seleccionado)
